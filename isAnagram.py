def sortWord (word):
	word = word.lower()
	sorted_word = []
	for char in word:
		sorted_word.append(char)
	sorted_word = sorted(sorted_word)
	return tuple(sorted_word)
#print(sortWord("stew"))
#output: ('e', 's', 't', 'w')


#takes string of words seperated by "\n" and outputs array of one-word strings 
def organize (words):
	ar = []
	
	word = ""
	for char in words:
		if (char != "\n"):
			word += char 
		else:
			ar.append(word.lower())
			word = ""

	ar = sorted(ar)
	return ar



mostCommonWords = open("1-10000.txt", "r")
arWords = organize(mostCommonWords.read())
mostCommonWords.close()

#sortWord for each word in arWords 
dictionary = list(map(lambda word: [sortWord(word), word], arWords))




def isAnagram (word, dictionary):
	sorted_word = sortWord(word)
	anagrams = []
	for x in dictionary:
		if sorted_word == x[0]:
			if (x[1] != word): anagrams.append(x[1])


	if len(anagrams) > 0:
		return [True, anagrams]
	else:
		return False

print( isAnagram("pot", dictionary) )

