import random

def hangman():
    words = ["apple", "table", "chair", "water", "pizza", "cat", "dog", "pen", "book", "phone"] 
    # Score tracking
    wins = 0
    losses = 0
    
    while True: 
        # Choose difficulty
        difficulty = input("\nChoose difficulty (easy/hard): ").lower()
        if difficulty == "easy":
            word_list = [w for w in words if len(w) >= 5]
        elif difficulty == "hard":
            word_list = [w for w in words if len(w) <= 4]
        else:
            print("⚠️ Invalid choice!Enabling Easy mode.")
            word_list = [w for w in words if len(w) >= 5]
        word = random.choice(word_list)
        guessed = ["_"] * len(word)
        attempts = 6
        guessed_letters = []

        first_letter = word[0]
        for i, letter in enumerate(word):
            if letter == first_letter:
                guessed[i] = first_letter
        guessed_letters.append(first_letter)

        print("\n🎮 Welcome to Hangman!")
        print(f"Difficulty: {difficulty.capitalize()}")
        print(f"💡 Hint: The word starts with '{first_letter}'")
        print("Guess the word:", " ".join(guessed))

        while attempts > 0 and "_" in guessed:
            print("Guessed letters:", ", ".join(guessed_letters))
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print(f"✅ Good job! '{guess}' is in the word.")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed[i] = guess
            else:
                attempts -= 1
                print(f"❌ Wrong! '{guess}' is not in the word. Attempts left: {attempts}")

            print("Word progress:", " ".join(guessed))
            print("-" * 40)

       
        if "_" not in guessed:
            print("🎉 Congratulations! You guessed the word:", word)
            wins += 1
        else:
            print("💀 Game Over! The word was:", word)
            losses += 1


        print(f"📊 Score → Wins: {wins} | Losses: {losses}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("\n👋 Thanks for playing Hangman!")
            print(f"Final Score → 🏆 Wins: {wins} | ❌ Losses: {losses}")
            break


hangman()
