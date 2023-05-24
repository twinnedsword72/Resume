"""
Author: Ishaan Singh
Purpose: Hangman game in which user selects number of letters they want in their word and then guesses either letter by letter or the full word in which they
try to get the word before 15 tries.
"""
#Make lists which contain the words which are either 5,6, or 7 letters
import random
hangmanWordsFive = ['giant', 'slice', 'brand', 'heart', 'dance']
hangmanWordsSix = ['obtain', 'reject', 'wealth', 'button', 'decade']
hangmanWordsSeven = ['academy', 'battery', 'captain', 'diamond', 'economy']
#Function which runs the game asking user to select number of letters and guess either letter by letter or word. Every time they try, one attempt is used.
def gameCode():
    numOfLetters = int(input("How many letters would you like to be in your word? Pick either 5,6,or 7: "))
    if numOfLetters==5:
        playerWord = random.choice(hangmanWordsFive)
    elif numOfLetters==6:
        playerWord = random.choice(hangmanWordsSix)
    else:
        playerWord = random.choice(hangmanWordsSeven)
    #Initialize variables
    numOfTries = 15
    attempt = False
    listOfLetters = []
    #Displays to user the number of letters in the word
    print('This word has', len(playerWord), 'letters.')
    print(len(playerWord)*'^')
#While loop that runs only if user has not guessed the word yet and they still have tries
    while attempt == False and numOfTries > 0:
        print("You have", str(numOfTries), 'tries')
        userGuess = input("Enter a letter or the word if you think you got it: ").lower()
#If statement which checks to see if the letter guessed is in the word and adds it to the word
        if len(userGuess) == 1:
            if userGuess in playerWord:
                print("That letter is in the word. Great job!")
                listOfLetters.append(userGuess)
                numOfTries-=1

            else:
                print("Sorry, try again!")
                listOfLetters.append(userGuess)
                numOfTries -= 1

#If user guesses the word by just typing in the full word, they win the game and are then prompted if they want to play again or not
        elif userGuess == playerWord:
         print("Congratulations. You guessed the word correctly!")
         attempt == True
         playAgain = input("Type 'play' to play again or 'end' to end the program: ")
         if playAgain == 'play':
          gameCode()
         else:
          print("Thanks for playing the game!")
          attempt = True
          exit()
        messageToUser = ''
#Adds letters to the word if the letter is correct
        if attempt == False:
            for letter in playerWord:
                if letter in listOfLetters:
                    messageToUser += letter
                else:
                    messageToUser += '^'
            print(messageToUser)
#If they end up getting the word after guessing letter by letter, they win and are then prompted to play if they want to again.
        if messageToUser == playerWord:
            print("Congrats, you guessed the word!")
            attempt = True
            playGame()
#If they guess the word by typing in the full word, and it is not correct. Then they lose a try and continue the game.
        elif len(userGuess) == len(playerWord) and userGuess is not playerWord:
            print("Sorry, that is not the word. Please try again.")
            numOfTries-=1
#When tries is equal to 0, user is told if they want to play again or not.
    if numOfTries==0:
        print("Sorry, you ran out of tries.")
        playGame()


#Function which asks user to either play or end the game. If they want to play, this function will start the game.
def playGame():
    startHangman = input("Type in 'start' to begin the game or 'end' to stop playing: ")
    if startHangman == 'start':
        gameCode()
    else:
        print("Thanks for playing Hangman!")

print("Hello, welcome to the Hangman game \n The rules of the game are as follows: \n 1. You will be asked to choose how many letters you want to be in your word \n 2. You can either guess letter by letter or type in the full word \n "
      "3. Try to get the word before 15 tries. Good luck!")
playGame()
























