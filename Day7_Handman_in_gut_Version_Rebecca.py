from wonderwords import RandomWord 

wordgenerator = RandomWord()

lives = 10

def getWord(): 
    newWord = wordgenerator.word(word_min_length=5, include_parts_of_speech=["noun"])
    return newWord

word = getWord().lower()

guessedLetters = []
def getLetterFromUser(): 
    letter = ""
    while len(letter) != 1 or letter in guessedLetters:
        letter = input("Give me one letter!").lower()
    guessedLetters.append(letter)
    return letter

def obscureWord(unobscuredWord, lettersToDisplay): 
    obscuredWordList = []
    unobscuredLetterList = list(unobscuredWord.lower())
    for letter in unobscuredLetterList: 
        if letter in lettersToDisplay: 
            obscuredWordList.append(letter)
        else: 
            obscuredWordList.append("_")
    return " ".join(obscuredWordList)

def printCurrentState(): 
    obscuredWord = obscureWord(word, guessedLetters)
    print(obscuredWord, "\t\t\t guessed already", guessedLetters)

while lives > 0 and "_" in obscureWord(word, guessedLetters): 
    printCurrentState()
    newLetter = getLetterFromUser()
    if newLetter in word: 
        print(f"{newLetter} is in the word!")
    else: 
        lives -= 1
        print(f"lives remaining: {lives}")

if lives == 0: 
    print(f"YOU DIED. The word was: {word}")
else: 
    print(f"Congratulations! The word was indeed {word}")

# print(obscureWord("Testfall", ["x", "a", "T", "e"]))