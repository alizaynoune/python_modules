from random import randint
secret = randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99\
to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!\n")
i = 1
while True:
    guess = input("What's your guess between 1 and 99?\n")
    if guess == 'exit':
        print("Goodbye!")
        break
    if not guess.isnumeric():
        print("That's not a number.")
    else:
        if int(guess) == secret:
            if i == 1:
                print(
                    "The answer to the ultimate question of life,\
the universe and everything is %d." % secret)
                print("Congratulations! You got it on your first try!")
                break
            else:
                print("Congratulations, you've got it!\
You won in %d attempts!" % i)
                break
        elif int(guess) < secret:
            print("Too low!")
        elif int(guess) > secret:
            print("Too high!")
    i += 1
