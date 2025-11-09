# GUESSING GAME, EACH FAILURE GIVES AN HINT, AND REDUCES THE FINAL SCORE
hint = [' ', 'The number is even', 'The number is a multiple of 5', 'The number is a multiple of 10', 'The number is a multiple of 7']
mark = ['0%', '100%', '80%', '60%', '40%']

x = 350
count = 0

while count <= 4:
    guess = int(input("Enter your guess number: "))
    count += 1
    if guess == x:
        print(f"You're correct, you aced it in {count} trial(s). Your final score is {mark[count]}")
        break
    elif count == 3 and guess != x:
        print(f"You're incorrect, you've used up {count}/4 trials. Here's a hint for you '{hint[count]}'")
        print('NOTE: You have 1 trial left')
    else:
        print(f"You're incorrect, you've used up {count}/4 trials. Here's a hint for you '{hint[count]}'")
    if count == 4 and guess != x:
        print("Game failed, sorry you've used up all your trials")
        break