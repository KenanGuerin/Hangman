word=""
guessed_letter=[ "_" for i in range (0,len(word))]
wrong_letter=""
guessed_word=""
known_letter=[]
shown_word=""
for char in guessed_letter:
	guessed_word+=char
	shown_word+=char
	shown_word+=" "
Hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def ask(letter):
	global wrong_letter,guessed_word,shown_word
	if letter in word:
		known_letter.append(letter)
		guessed_word=""
		shown_word=""
		for char in word:
			if char in known_letter:
				guessed_word+=char
				shown_word+=char
				shown_word+=" "
			else:
				guessed_word+="_"
				shown_word+="_"
				shown_word+=" "
	else:
		wrong_letter+=letter
	return guessed_word,shown_word

def play():
	global shown_word,wrong_letter,guessed_word,word
	word=(str(input(" Type a word ")))
	word=word.lower()
	for i in range (0,100):
		print("")
	print("           ",shown_word)
	print(Hangman[len(wrong_letter)])
	print(wrong_letter)
	while len(wrong_letter) < 6 and guessed_word != word:
		guessed_word,shown_word=ask(str(input(" Type a letter ")))
		print("           ",shown_word)
		print(Hangman[len(wrong_letter)])
		print(wrong_letter)
	if len(wrong_letter) < 6 :
		print("Guesser won")
	else:
		print("Guesser lose")
play()

