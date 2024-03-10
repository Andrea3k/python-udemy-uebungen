# flow chart programming
# .drawio 
# RandomWord() is a class and has methods  wordgenerator.word()

# generate a random word

from wonderwords import RandomWord
wordgenerator = RandomWord()

r = wordgenerator.word(word_min_length=5, include_parts_of_speech=["nouns"])
print(r)

word = []
for x in range(0, len(r)): 
    word.append("_")
print(f"This is the word we are searching for: {word}\n Please choose a letter")

guessedLetters = []
def getLetterFromUser():
    guessedLetter = input("Give me a letter!")
    guessedLetter = guessedLetter.lower()
    guessedLetters.append(guessedLetter)
    print("Guessed letters so far are", guessedLetters)
    
getLetterFromUser()

def
lives = 10
i = 0
letterInWord = False
for letter in r:
    # letter wird nach einander g, e, s, t, u, r, e sein

    if letter == guessedLetter: 
        letterInWord = True
        if letterInWord == True: 
            while i < len(r): 
                if guessedLetter == r[i]:
                    word[i] = guessedLetter
                i += 1
            print(f"This is the current status of the word we are searching for: {word}\n Please choose the next letter.")
        else: 
            guessedLetters = guessedLetters.append(guessedLetter)
            lives = lives - len(guessedLetters)
            if lives == 0:
                print(f"YOU DIED\nThis is the word you didnt guessed: {r}")
            elif "_" in word:  
                print(f"These are the letters you have already guessed and are wrong: {guessedLetters}\n You have {lives} left. Please chose your next letter.")     
            else: 
                print(f"YOU WON!!! This is the word you guessed correctly: {word}")

# Wort überprüfen
# def obscureWord(word, guessedLetters): 
# gibt das Wort mit "versteckten" Buchstaben zurück
# also "Esel" und guessedLetters  ? ["s"] -> "_ s _ _"



