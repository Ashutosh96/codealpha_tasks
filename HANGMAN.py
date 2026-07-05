import random

# Predefined list of words
words = ["apple", "table", "chair", "house", "plant"]

# Randomly choose a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess:", " ".join(guessed_word))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)

