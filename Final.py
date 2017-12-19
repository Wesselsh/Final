import random

first_sentence = "Flanigan shows his dark, thick, glutes for Ames, Padjen, and his horse"

capital_alphabet = ['B','C','D','F','G','H','J','K','L','N','P','Q','R','S','T','V','W','M','X','Y','Z']

def slangify(first_sentence):
	word_list = split_sentence(first_sentence)
	sentence = ''
	n = 0
	
	for word in range(len(word_list)):
		word = word_list[n]
		post_word = changerfy(word)
		sentence = sentence + " " + post_word
		post_word = ''
		word= ''
		n = n + 1
		
	print sentence

def changerfy(word):
	word = b_ify(word)
	word = c_ify(word)
	
	return word
	
def b_ify(word):
	if word == "and":
		return word
	
	if word == "for":
		return word 
		
	if word == "his":
		return word
		
	if len(word) < 1: #checks to see if its a word to begin with
		return "not a valid word"
	
	if len(word) == 1: #checks to see if not one letter
		return word
	
	chance = random.randint(1,3)
	
	if is_vowel_name(word):  #if its a name starts with a vowel, then it will definitely replace with a B
		word = "B" + word[0].lower() + word[1:]
		return word

	if is_consonant_name(word): # if name, it will definetly replace with a b
		word = "B" + word[1:]
		return word

	if starts_with_a_vowel(word): #if a normal vowel-starting word, theres a 1 in 3 chance that it gets b'ed
		if chance == 1:
			word = "b" + word
			return word
			
		if chance == 2 or 3:
			return word

	if starts_with_a_consonant(word):#if a normal consonant-starting word, theres a 1 in 3 chance that it gets b'ed
		if chance == 1:
			word = "b" + word[1:]
		if chance == 2 or 3:
			return word
def c_ify(word):
	letter_list = split_word(word) # splits the word into a letter list 
	word = ''
	for i in letter_list: # turns any c or k into two c's except if the word starts with a c
		if i != 1:
			if i == "c":
				word = word + "cc"
			elif i == "k":
				word = word + "cc"
			else:
				word = word + i 
		if i == 1:
			word = word + i
			
	return word

def split_word(word):
	split_word = []
	n = 0
	for i in range(len(word)):
		letter = word[n]
		split_word.append(letter)
		n = n + 1
	return split_word
def is_consonant_name(word):
	if len(word) < 1:
		return False
	first_letter = word[0]
	if first_letter == "A" or first_letter == "E" or first_letter == "I" or first_letter == "O" or first_letter == "U":
		return False
	else:
		for letter in range(len(capital_alphabet)):
			if word[0] not in capital_alphabet:
				return False
			else:
				return True

def split_sentence(first_sentence):
	first_sentence += ' '
	word = ''
	split_list = []
	for i in range(len(first_sentence)):
		if first_sentence[i] != ' ':
			word += first_sentence[i]

		else:
			split_list.append(word)
			word = ''

	return split_list

def is_vowel_name(word):
	if len(word) < 1:
		return False
	first_letter = word[0]
	if first_letter == "A" or first_letter == "E" or first_letter == "I" or first_letter == "O" or first_letter == "U":
		return True

def starts_with_a_consonant(word):
	if len(word) < 1:
		return False
	first_letter = word[0].lower()
	if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
		return False
	else:
		return True

def starts_with_a_vowel(word):
	if len(word) < 1:
		return True
	first_letter = word[0].lower()
	if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
		return True
	else:
		return False
		
slangify(first_sentence)
