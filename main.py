import random
import hangman_words, hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
guessed_letters = 0
print(hangman_art.logo)

display = []
for letter in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'The letter "{guess}" has been already guessed!')
    elif guess not in chosen_word:
        print(f'''The letter "{guess}" is not in this word. You lose a life.''')
        lives -= 1
    else:
        for letter in chosen_word:
            if guess == letter:
                position = chosen_word.find(letter)
                display[position] = guess
                guessed_letters += 1
    print(f"{' '.join(display)}")    
      
    print(hangman_art.stages[lives])
    
    if guessed_letters == word_length:
        end_of_game = True
        print("You win.")
    
    if lives == 0:
        end_of_game = True
        print("You lose.")