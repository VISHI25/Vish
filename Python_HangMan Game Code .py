import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Use of while loop 
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6
lives = 6 

#TODO-2 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

length = len(chosen_word)

#TODO-2 Create Blank word
blank= []
for b in range(length):
  blank.append("_")
       
print(blank) 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while not end_of_game:
  guess = input("Guess the keyword: ").lower()
  print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
  else: 
      for pos in range(length):
        if guess == chosen_word[pos]:
          blank[pos] = guess

  #Join all the elements in the list and turn it into a String.

  print(f"{' '.join(blank)}")

  #Check if user has got all letters.

  if "_" not in blank:
     end_of_game = True
     print("You win.") 


  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

  print(stages[lives])

word = "".join(blank)
print(type(word))
print(word)


