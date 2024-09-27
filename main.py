import os
import random
from hangman_words_list import word_list
from hang_stages import stages,logo


print(logo)

play =input("you want's to play hangman ??? Y or N\n").upper()
if play =="Y":
    print("welcome to guessing game")
else:
    play =input("you want's to play hangman Y or N\n").upper()

end_of_game = False
lives = len(stages) - 1

choosen_word = random.choice(word_list)
n = len(choosen_word)
print(choosen_word)


display = []
for _ in range(n):
  display += "_"

print(display)


while not end_of_game:
  guess = input("guess the letter\n").lower()

  os.system('cls||clear')
  print(logo)

  if guess in display:
    print(f"you already guessed: {guess}")

  for position in range(n):
    letter = choosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in choosen_word:
    lives -= 1
    print(f"you guess a wrong word!! you loos a life...lifes left {lives} !!")
    if lives == 0:
      end_of_game = True
      print("you loose!!!")    

  if "_" not in display:
    end_of_game = True
    print("you win!!")

  print(stages[lives])

  print(f"{' '.join(display)}")




