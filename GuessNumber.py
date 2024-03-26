import random
MysteryNumber = random.randint(1,10)
guess = input("Guess a number between 1 to 10! We'll tell you if it's lower or higher, and you only get three tries!: ")

for x in range(3):
    if int(guess) == MysteryNumber:
        print("Good job! You guessed it right!")
        break
    else:
        if x == 2:
            print(f"You didn't manage to guess the number. The mystery number is {MysteryNumber}!")
        else:
            if int(guess) > MysteryNumber:
                print("Think lower!")
                guess = input(f"Guess number {x+2}: ")
            else:
                print("Think higher!")
                guess = input(f"Guess number {x+2}: ")