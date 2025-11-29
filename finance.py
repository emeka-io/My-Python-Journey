
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from datetime import datetime
import csv
import os
import math

# matplotlib for charts
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DB_FILE = "finance.db"

# -------------------------
# Database handler
# -------------------------
class DB:
    def __init__(self, db_path=DB_FILE):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL, -- "Expense" or "Income"
            note TEXT
        )
        """)
        self.conn.commit()

    def add_transaction(self, date_iso, amount, category, tx_type, note):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO transactions (date, amount, category, type, note) VALUES (?, ?, ?, ?, ?)",
            (date_iso, amount, category, tx_type, note)
        )
        self.conn.commit()
        return cur.lastrowid

    def update_transaction(self, tx_id, date_iso, amount, category, tx_type, note):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE transactions SET date=?, amount=?, category=?, type=?, note=? WHERE id=?",
            (date_iso, amount, category, tx_type, note, tx_id)
        )
        self.conn.commit()

    def delete_transaction(self, tx_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM transactions WHERE id=?", (tx_id,))
        self.conn.commit()

    def fetch_transactions(self, limit=None, order_by="date DESC"):
        cur = self.conn.cursor()
        q = "SELECT id, date, amount, category, type, note FROM transactions ORDER BY " + order_by
        if limit:
            q += f" LIMIT {int(limit)}"
        cur.execute(q)
        rows = cur.fetchall()
        return rows

    def fetch_transactions_between(self, start_iso, end_iso):
        cur = self.conn.cursor()
        cur.execute("SELECT id, date, amount, category, type, note FROM transactions WHERE date BETWEEN ? AND ? ORDER BY date", (start_iso, end_iso))
        return cur.fetchall()

    def summary_month(self, year, month):
        # returns total income, expense
        cur = self.conn.cursor()
        prefix = f"{year:04d}-{month:02d}-"
        cur.execute("SELECT type, SUM(amount) FROM transactions WHERE date LIKE ? GROUP BY type", (prefix + "%",))
        data = dict(cur.fetchall())
        income = float(data.get("Income") or 0.0)
        expense = float(data.get("Expense") or 0.0)
        return income, expense

    def spending_by_category_last_n_months(self, months=6):
        cur = self.conn.cursor()
        cutoff = datetime.now().replace(day=1)
        # compute earliest month iso
        month = cutoff.month - months + 1
        year = cutoff.year
        while month <= 0:
            month += 12
            year -= 1
        start_iso = f"{year:04d}-{month:02d}-01"
        cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' AND date >= ? GROUP BY category ORDER BY SUM(amount) DESC", (start_iso,))
        return cur.fetchall()

    def get_monthly_totals(self, months=6):
        # returns list of (YYYY-MM, income, expense)
        results = []
        now = datetime.now()
        for i in range(months-1, -1, -1):
            ym = (now.month - i - 1) % 12 + 1
            y = now.year + ((now.month - i - 1) // 12)
            if now.month - i - 1 < 0:
                # adjust year back
                y = now.year - 1
            income, expense = self.summary_month(y, ym)
            results.append((f"{y:04d}-{ym:02d}", income, expense))
        return results

# -------------------------
# Helper functions
# -------------------------
def parse_date_input(date_text):
    # accepts YYYY-MM-DD or DD/MM/YYYY or YYYY/MM/DD or "today"
    date_text = date_text.strip()
    if date_text.lower() in ("today", "now"):
        return datetime.now().date().isoformat()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date_text, fmt).date().isoformat()
        except Exception:
            pass
    # last fallback: try parse by splitting
    try:
        d = datetime.fromisoformat(date_text)
        return d.date().isoformat()
    except Exception:
        raise ValueError("Date format not recognized. Use YYYY-MM-DD or DD/MM/YYYY")

# -------------------------
# GUI Application
# -------------------------
class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Dashboard — EMEKA's Finance")
        self.geometry("1100x700")
        self.minsize(920, 600)

        self.db = DB()
        self.style_name = "light"  # or "dark"

        self._setup_styles()
        self._create_widgets()
        self.refresh_transactions()
        self.draw_charts()

    def _setup_styles(self):
        self.style = ttk.Style(self)
        # base theme
        default_font = ("Segoe UI", 10)
        self.style.configure(".", font=default_font)
        # light colors
        self.colors = {
            "light": {
                "bg": "#f6f8fa",
                "card": "#ffffff",
                "text": "#0f1724",
                "muted": "#6b7280",
                "accent": "#2d6cdf",
                "positive": "#0f5132",
                "negative": "#8b1d1d",
                "treebg": "#ffffff",
            },
            "dark": {
                "bg": "#0b1220",
                "card": "#0f1724",
                "text": "#e6eef8",
                "muted": "#9aa7b5",
                "accent": "#58a6ff",
                "positive": "#7ee787",
                "negative": "#ff7b7b",
                "treebg": "#0b1220",
            }
        }
        self.apply_theme(self.style_name)

    def apply_theme(self, name):
        c = self.colors[name]
        self.configure(bg=c["bg"])
        self.style.configure("Card.TFrame", background=c["card"])
        self.style.configure("Header.TLabel", background=c["bg"], foreground=c["text"], font=("Segoe UI", 14, "bold"))
        self.style.configure("SubHeader.TLabel", background=c["card"], foreground=c["muted"], font=("Segoe UI", 10))
        self.style.configure("TLabel", background=c["card"], foreground=c["text"])
        self.style.configure("TButton", background=c["card"], foreground=c["text"])
        self.style.configure("Treeview", background=c["treebg"], fieldbackground=c["treebg"], foreground=c["text"])
        self.style.map("TButton",
                       foreground=[('active', c["text"])])
        # for Treeview headings
        self.style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def _create_widgets(self):
        # Top header
        header = ttk.Frame(self, style="Card.TFrame")
        header.place(relx=0, rely=0, relwidth=1, height=60)
        ttk.Label(header, text="Personal Finance Dashboard", style="Header.TLabel").pack(side="left", padx=16, pady=10)
        # theme toggle
        self.theme_btn = ttk.Button(header, text="Switch to Dark", command=self.toggle_theme)
        self.theme_btn.pack(side="right", padx=10, pady=12)

        # Main panes
        left_pane = ttk.Frame(self, style="Card.TFrame")
        left_pane.place(relx=0, rely=0.09, relwidth=0.37, relheight=0.9)

        right_pane = ttk.Frame(self, style="Card.TFrame")
        right_pane.place(relx=0.37, rely=0.09, relwidth=0.63, relheight=0.9)

        # -----------------------
        # Left pane: controls + table
        # -----------------------
        form = ttk.LabelFrame(left_pane, text="Add / Edit Transaction", style="Card.TFrame")
        form.pack(fill="x", padx=12, pady=8)

        # Date
        ttk.Label(form, text="Date (YYYY-MM-DD)").grid(row=0, column=0, sticky="w", padx=8, pady=6)
        self.date_var = tk.StringVar(value=datetime.now().date().isoformat())
        ttk.Entry(form, textvariable=self.date_var).grid(row=0, column=1, sticky="ew", padx=8, pady=6)

        # Amount
        ttk.Label(form, text="Amount").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.amount_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.amount_var).grid(row=1, column=1, sticky="ew", padx=8, pady=6)

        # Type
        ttk.Label(form, text="Type").grid(row=2, column=0, sticky="w", padx=8, pady=6)
        self.type_var = tk.StringVar(value="Expense")
        ttk.Combobox(form, values=("Expense", "Income"), textvariable=self.type_var, state="readonly").grid(row=2, column=1, sticky="ew", padx=8, pady=6)

        # Category
        ttk.Label(form, text="Category").grid(row=3, column=0, sticky="w", padx=8, pady=6)
        self.category_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.category_var).grid(row=3, column=1, sticky="ew", padx=8, pady=6)

        # Note
        ttk.Label(form, text="Note").grid(row=4, column=0, sticky="w", padx=8, pady=6)
        self.note_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.note_var).grid(row=4, column=1, sticky="ew", padx=8, pady=6)

        form.columnconfigure(1, weight=1)

        # Buttons
        btn_frame = ttk.Frame(left_pane, style="Card.TFrame")
        btn_frame.pack(fill="x", padx=12, pady=4)
        ttk.Button(btn_frame, text="Add Transaction", command=self.on_add).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Update Selected", command=self.on_update).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Delete Selected", command=self.on_delete).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Import CSV", command=self.on_import).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Export CSV", command=self.on_export).pack(side="left", padx=6)

        # Transaction table
        table_frame = ttk.LabelFrame(left_pane, text="Transactions", style="Card.TFrame")
        table_frame.pack(fill="both", expand=True, padx=12, pady=8)

        cols = ("id", "date", "amount", "category", "type", "note")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings", selectmode="browse")
        for c in cols:
            self.tree.heading(c, text=c.title())
            self.tree.column(c, anchor="w", stretch=True)
        self.tree.column("id", width=40, anchor="center")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # vertical scrollbar
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, side="left")

        # -----------------------
        # Right pane: summary + charts
        # -----------------------
        summary_frame = ttk.Frame(right_pane, style="Card.TFrame")
        summary_frame.pack(fill="x", padx=12, pady=8)

        # cards: income, expense, balance
        cards = ttk.Frame(summary_frame, style="Card.TFrame")
        cards.pack(fill="x")

        self.income_label = ttk.Label(cards, text="Income: ₦0.00", style="SubHeader.TLabel")
        self.income_label.pack(side="left", padx=8, pady=6)

        self.expense_label = ttk.Label(cards, text="Expense: ₦0.00", style="SubHeader.TLabel")
        self.expense_label.pack(side="left", padx=8, pady=6)

        self.balance_label = ttk.Label(cards, text="Balance: ₦0.00", style="SubHeader.TLabel")
        self.balance_label.pack(side="left", padx=8, pady=6)

        # Chart area
        chart_frame = ttk.LabelFrame(right_pane, text="Charts", style="Card.TFrame")
        chart_frame.pack(fill="both", expand=True, padx=12, pady=8)

        # Use matplotlib Figure
        self.fig = Figure(figsize=(6,4), tight_layout=True)
        # two subplots: top time series, bottom category bar
        self.ax_ts = self.fig.add_subplot(211)
        self.ax_cat = self.fig.add_subplot(212)

        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # small controls under chart
        chart_ctrl = ttk.Frame(right_pane, style="Card.TFrame")
        chart_ctrl.pack(fill="x", padx=12)
        ttk.Button(chart_ctrl, text="Refresh Charts", command=self.draw_charts).pack(side="left", padx=6)
        ttk.Button(chart_ctrl, text="Show Last 12 Months", command=lambda: self.draw_charts(months=12)).pack(side="left", padx=6)
        ttk.Button(chart_ctrl, text="Show Last 6 Months", command=lambda: self.draw_charts(months=6)).pack(side="left", padx=6)

    # -----------------------
    # Actions
    # -----------------------
    def on_add(self):
        try:
            date_iso = parse_date_input(self.date_var.get())
            amount = float(self.amount_var.get())
            category = self.category_var.get().strip() or "Uncategorized"
            tx_type = self.type_var.get()
            note = self.note_var.get().strip()
            if tx_type not in ("Expense", "Income"):
                raise ValueError("Type must be Expense or Income")
            if tx_type == "Expense" and amount > 0:
                # make expenses positive in DB but treat as expense
                pass
            # store positive amounts; handling type is separate
            tx_id = self.db.add_transaction(date_iso, amount, category, tx_type, note)
            self.refresh_transactions()
            self.clear_form()
            self.draw_charts()
        except Exception as e:
            messagebox.showerror("Add transaction", f"Failed to add: {e}")

    def on_update(self):
        sel = self._selected_tx()
        if not sel:
            messagebox.showinfo("Update", "Select a transaction to update.")
            return
        tx_id = sel[0]
        try:
            date_iso = parse_date_input(self.date_var.get())
            amount = float(self.amount_var.get())
            category = self.category_var.get().strip() or "Uncategorized"
            tx_type = self.type_var.get()
            note = self.note_var.get().strip()
            self.db.update_transaction(tx_id, date_iso, amount, category, tx_type, note)
            self.refresh_transactions()
            self.clear_form()
            self.draw_charts()
        except Exception as e:
            messagebox.showerror("Update transaction", f"Failed to update: {e}")

    def on_delete(self):
        sel = self._selected_tx()
        if not sel:
            messagebox.showinfo("Delete", "Select a transaction to delete.")
            return
        tx_id = sel[0]
        if messagebox.askyesno("Delete", "Delete selected transaction?"):
            self.db.delete_transaction(tx_id)
            self.refresh_transactions()
            self.clear_form()
            self.draw_charts()

    def on_export(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")])
        if not path:
            return
        rows = self.db.fetch_transactions(order_by="date ASC")
        try:
            with open(path, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id","date","amount","category","type","note"])
                writer.writerows(rows)
            messagebox.showinfo("Export", f"Exported {len(rows)} rows to {path}")
        except Exception as e:
            messagebox.showerror("Export", f"Failed to export: {e}")

    def on_import(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv"), ("All files","*.*")])
        if not path:
            return
        try:
            imported = 0
            with open(path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    try:
                        date_iso = parse_date_input(r.get("date") or r.get("Date") or r.get("DATE"))
                        amount = float(r.get("amount") or r.get("Amount") or 0)
                        category = r.get("category") or r.get("Category") or "Imported"
                        tx_type = r.get("type") or r.get("Type") or "Expense"
                        note = r.get("note") or ""
                        self.db.add_transaction(date_iso, amount, category, tx_type, note)
                        imported += 1
                    except Exception:
                        continue
            messagebox.showinfo("Import", f"Imported {imported} transactions.")
            self.refresh_transactions()
            self.draw_charts()
        except Exception as e:
            messagebox.showerror("Import", f"Failed to import: {e}")

    def on_tree_select(self, event):
        sel = self._selected_tx()
        if not sel:
            return
        # sel = (id, date, amount, category, type, note)
        tx_id, date_iso, amount, category, tx_type, note = sel
        self.date_var.set(date_iso)
        self.amount_var.set(str(amount))
        self.category_var.set(category)
        self.type_var.set(tx_type)
        self.note_var.set(note)

    def _selected_tx(self):
        sid = self.tree.selection()
        if not sid:
            return None
        item = self.tree.item(sid)
        vals = item.get("values")
        if not vals:
            return None
        return vals  # id, date, amount, category, type, note

    def refresh_transactions(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        rows = self.db.fetch_transactions(order_by="date DESC")
        for r in rows:
            # r is (id, date, amount, category, type, note)
            display = list(r)
            display[2] = f"₦{display[2]:,.2f}"
            self.tree.insert("", "end", values=display)
        # update summary cards with current month totals
        now = datetime.now()
        income, expense = self.db.summary_month(now.year, now.month)
        balance = income - expense
        self.income_label.config(text=f"Income: ₦{income:,.2f}")
        self.expense_label.config(text=f"Expense: ₦{expense:,.2f}")
        self.balance_label.config(text=f"Balance: ₦{balance:,.2f}")

    def clear_form(self):
        self.date_var.set(datetime.now().date().isoformat())
        self.amount_var.set("")
        self.category_var.set("")
        self.type_var.set("Expense")
        self.note_var.set("")

    def toggle_theme(self):
        self.style_name = "dark" if self.style_name == "light" else "light"
        self.apply_theme(self.style_name)
        self.theme_btn.config(text="Switch to Light" if self.style_name == "dark" else "Switch to Dark")

    def draw_charts(self, months=6):
        # Clear axes
        self.ax_ts.clear()
        self.ax_cat.clear()

        # Time series: monthly totals
        monthly = self.db.get_monthly_totals(months=months)
        months_labels = [m for (m, i, e) in monthly]
        incomes = [i for (m, i, e) in monthly]
        expenses = [e for (m, i, e) in monthly]

        # convert months_labels to shorter names
        x = list(range(len(months_labels)))
        self.ax_ts.plot(x, incomes, marker="o", label="Income")
        self.ax_ts.plot(x, expenses, marker="o", label="Expense")
        self.ax_ts.set_xticks(x)
        self.ax_ts.set_xticklabels(months_labels, rotation=30, fontsize=8)
        self.ax_ts.set_title("Monthly Income vs Expense")
        self.ax_ts.legend()
        self.ax_ts.grid(True, alpha=0.2)

        # Category bar chart for last N months
        cat = self.db.spending_by_category_last_n_months(months=months)
        categories = [c for (c, s) in cat][:10]
        sums = [s for (c, s) in cat][:10]
        if categories:
            self.ax_cat.barh(categories[::-1], sums[::-1])
            self.ax_cat.set_title(f"Spending by Category (last {months} months)")
        else:
            self.ax_cat.text(0.5, 0.5, "No expense data", ha="center", va="center")

        self.fig.tight_layout()
        self.canvas.draw()

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
