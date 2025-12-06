import tkinter as tk
from tkinter import ttk, messagebox
import random

GAMES = {
    1: "Chelsea VS Man U",
    2: "Atalanta VS Napoli",
    3: "Bayern VS Frankfurt",
    4: "Barcelona VS Elche"
}


class Score:
    @staticmethod
    def ft():
        return random.randint(0, 7), random.randint(0, 7)


class PredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Score Prediction Game")

        # --- FULL SCREEN + responsive layout ---
        self.root.geometry("1100x650")
        self.root.minsize(950, 600)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.dark_mode = tk.BooleanVar(value=False)
        self.history = []

        self.style = ttk.Style()

        # Root container expands fully
        self.container = ttk.Frame(self.root, padding=25)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.columnconfigure(0, weight=1)

        self.build_ui()
        self.apply_theme()

    # -----------------------------------
    # BUILD UI
    # -----------------------------------
    def build_ui(self):

        # ---- Title ----
        title = ttk.Label(
            self.container, 
            text="Score Prediction Game",
            font=("Segoe UI", 22, "bold")
        )
        title.grid(row=0, column=0, pady=(0, 25), sticky="n")

        # ---- Form Section ----
        form = ttk.Frame(self.container)
        form.grid(row=1, column=0, sticky="ew", pady=10)
        form.columnconfigure(1, weight=1)

        # Name
        ttk.Label(form, text="Your name:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="w", pady=8)
        self.name_entry = ttk.Entry(form, font=("Segoe UI", 11))
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=10)

        # Match
        ttk.Label(form, text="Pick a Match:", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="w", pady=8)
        self.game_var = tk.StringVar()
        self.game_dropdown = ttk.Combobox(form, textvariable=self.game_var, state="readonly", font=("Segoe UI", 11))
        self.game_dropdown["values"] = list(GAMES.values())
        self.game_dropdown.grid(row=1, column=1, sticky="ew", padx=10)

        # ---- Score Row (fixed alignment) ----
        score_frame = ttk.Frame(form)
        score_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=15)

        score_frame.columnconfigure(0, weight=1)
        score_frame.columnconfigure(1, weight=1)
        score_frame.columnconfigure(2, weight=1)
        score_frame.columnconfigure(3, weight=1)

        ttk.Label(score_frame, text="Home goals:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="e")
        self.h_spin = tk.Spinbox(score_frame, from_=0, to=15, width=6, justify="center", font=("Segoe UI", 11))
        self.h_spin.grid(row=0, column=1, sticky="w", padx=10)

        ttk.Label(score_frame, text="Away goals:", font=("Segoe UI", 11)).grid(row=0, column=2, sticky="e")
        self.a_spin = tk.Spinbox(score_frame, from_=0, to=15, width=6, justify="center", font=("Segoe UI", 11))
        self.a_spin.grid(row=0, column=3, sticky="w", padx=10)

        # ---- Buttons ----
        btn_frame = ttk.Frame(self.container)
        btn_frame.grid(row=2, column=0, pady=15)
        btn_frame.columnconfigure(0, weight=1)

        self.submit_btn = ttk.Button(
            btn_frame, 
            text="Submit Prediction (Generate Final)", 
            command=self.submit,
            width=45
        )
        self.submit_btn.grid(row=0, column=0, pady=6)

        self.play_again_btn = ttk.Button(
            btn_frame, 
            text="Reset Fields", 
            command=self.reset_fields,
            width=45
        )
        self.play_again_btn.grid(row=1, column=0)

        # ---- Result Section ----
        result_box = ttk.LabelFrame(self.container, text="Result", padding=15)
        result_box.grid(row=3, column=0, sticky="ew", pady=20)
        result_box.columnconfigure(0, weight=1)

        self.result_label = ttk.Label(result_box, text="No prediction yet.", anchor="center", justify="center")
        self.result_label.grid(row=0, column=0, sticky="ew")

        # ---- History Section ----
        history_box = ttk.LabelFrame(self.container, text="History (latest at top)", padding=15)
        history_box.grid(row=4, column=0, sticky="nsew")
        history_box.columnconfigure(0, weight=1)
        self.container.rowconfigure(4, weight=1)  # Makes history expand

        self.history_listbox = tk.Listbox(history_box, height=10, font=("Segoe UI", 10))
        self.history_listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(history_box, orient="vertical", command=self.history_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.history_listbox.configure(yscrollcommand=scrollbar.set)

        # ---- Dark mode toggle ----
        ttk.Checkbutton(
            self.container, 
            text="Dark Mode", 
            variable=self.dark_mode, 
            command=self.apply_theme
        ).grid(row=5, column=0, pady=15, sticky="w")

    # -----------------------------------
    # SUBMIT
    # -----------------------------------
    def submit(self):
        name = self.name_entry.get().strip()
        match = self.game_var.get().strip()

        if not name:
            messagebox.showwarning("Missing Information", "Enter your name.")
            return
        if not match:
            messagebox.showwarning("Missing Information", "Pick a match.")
            return

        home_pred = int(self.h_spin.get())
        away_pred = int(self.a_spin.get())
        pred = (home_pred, away_pred)
        final_score = Score.ft()

        if pred == final_score:
            outcome = "🎉 Correct prediction!"
        else:
            outcome = "❌ Incorrect prediction."

        result_text = (
            f"Player: {name}\n"
            f"Match: {match}\n"
            f"Your prediction: {pred}\n"
            f"Final score: {final_score}\n\n"
            f"{outcome}"
        )

        self.result_label.config(text=result_text)
        messagebox.showinfo("Result", result_text)

        self.history.insert(0, f"{name} — {match} — P:{pred} F:{final_score}")
        self.refresh_history()

    def refresh_history(self):
        self.history_listbox.delete(0, tk.END)
        for entry in self.history:
            self.history_listbox.insert(tk.END, entry)

    def reset_fields(self):
        self.name_entry.delete(0, tk.END)
        self.game_dropdown.set("")
        self.h_spin.delete(0, tk.END)
        self.h_spin.insert(0, "0")
        self.a_spin.delete(0, tk.END)
        self.a_spin.insert(0, "0")
        self.result_label.config(text="No prediction yet.")

    # -----------------------------------
    # THEME
    # -----------------------------------
    def apply_theme(self):
        if self.dark_mode.get():
            bg = "#1e1e1e"
            fg = "white"
            field_bg = "#2c2c2c"
        else:
            bg = "white"
            fg = "black"
            field_bg = "white"

        self.root.configure(background=bg)
        self.container.configure(style="TFrame")

        self.style.configure("TFrame", background=bg)
        self.style.configure("TLabelFrame", background=bg, foreground=fg)
        self.style.configure("TLabel", background=bg, foreground=fg)
        self.style.configure("TCheckbutton", background=bg, foreground=fg)
        self.style.configure("TEntry", fieldbackground=field_bg, foreground=fg)
        self.style.configure("TCombobox", fieldbackground=field_bg, foreground=fg)
        self.style.configure("TButton", background=bg)

        self.history_listbox.configure(background=field_bg, foreground=fg)
        self.result_label.configure(background=bg, foreground=fg)


if __name__ == "__main__":
    root = tk.Tk()
    PredictionApp(root)
    root.mainloop()
