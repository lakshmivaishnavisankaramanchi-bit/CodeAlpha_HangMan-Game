import random

words = ["apple", "banana", "orange", "python", "guitar"]
secret = random.choice(words)
guessed = set()
wrong_guesses = 0
max_wrong = 6

def masked_word(secret, guessed):
    return " ".join([c if c in guessed else "_" for c in secret])

while wrong_guesses < max_wrong and set(secret) - guessed:
    print("\nWord:", masked_word(secret, guessed))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    guess = input("Guess one letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    if guess in secret:
        guessed.add(guess)
        print("Nice! That letter is in the word.")
    else:
        wrong_guesses += 1
        guessed.add(guess)
        print("Nope. That letter is not in the word.")

if set(secret) - guessed:
    print(f"\nYou lost. The word was: {secret}")
else:
    print(f"\nYou won! The word was: {secret}")
