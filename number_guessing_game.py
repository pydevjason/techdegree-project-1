import random

def start_game():
    print("Welcome to the NUMBER GUESSING GAME!")
    num = random.randint(1,10)
    count = 1
    while num:
        try:
            prompt = int(input("Enter a number between 1 and 10: "))
            if prompt > 10 or prompt < 1:
                print("Number must be less than 11 and greater than 0")
            elif prompt > num:
                print("too high".capitalize())
            elif prompt < num:
                print("too low".capitalize())
            else:
                print(f"You got it ! You made {count} attempts in finding the number")
                print("The game is now over.\n")
                num = False
                play_again = input("Do you want to play again? ")
                if play_again == "n":
                    print("Thank you for playing!")
                    num = False
                elif play_again == "y":
                    start_game()
                else:
                    print("Invalid input.  The game will now restart.")
                    start_game()
            count += 1
            print()
        except ValueError:
            print("input must be a numeric value between 1 and 10 inclusive")

start_game()
