# GUESSING GAME, EACH FAILURE GIVES AN HINT, AND REDUCES THE FINAL SCORE
hint = [' ', 'The number is even', 'The number is a multiple of 5', 'The number is a multiple of 10', 'The number is a multiple of 7']
mark = ['100%', '80%', '60%', '40%', '20%']

x = 350
count = 0

while count <= 4:
    count += 1
    guess = int(input("Enter your guess number: "))
    if guess == x:
        print(f"You're correct, you aced it in {count} trial(s). Your final score is {mark[count]}")
    else:
        print(f"You're incorrect, you've used up {count}/4 trials. Here's a hint for you '{hint[count]}'")