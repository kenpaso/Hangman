
alphabet = {}
#input for what word to guess
def ask_word():
  print("-----Hangman-----")
  hangman_word = input("What is the Hangman Word:  ")
  return hangman_word

def guest_letetr():
  print("guest letter")

def play_game(hangman_word):
  print("hand over to new person")
  char_list = list(hangman_word)
  print(char_list)

hangman_word = ask_word()
play_game(hangman_word)