import random

# List of country names
countries = ["canada", "brazil", "japan", "australia", "egypt"]

# Dictionary of hangman stages
hangman_game = {
    0: ("  ", "  ", "  "),
    1: (" o ", "  ", "  "),
    2: (" o ", " | ", "  "),
    3: (" o ", "/| ", "  "),
    4: (" o ", "/|\\", "  "),
    5: (" o ", "/|\\", "/ "),
    6: (" o ", "/|\\", "/ \\"),
}

def display_man(wrong_guesses):
    print("*********")
    for line in hangman_game[wrong_guesses]:
        print(line)
    print("*********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"The country was: {answer}")

def main():
    answer = random.choice(countries)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("Congratulations! You've guessed the country!")
            is_running = False
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print("Game over! You've run out of guesses.")
            display_answer(answer)
            is_running = False

if __name__ == "__main__":
    main()