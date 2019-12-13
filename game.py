# Import random number module
import random

# Intializing score variable
score = 0

# Function to alert error message
def alert(message, number):
  if message == 'correct':
    print('You guessed correctly!')
  if message == 'incorrect':
    print('You almost guessed it. The answer is ' + str(number))

# Function to alert error message
def awardAlert(star):
  print('Congrats you have been awarded a ' + star + ' star!')
  
# Function to check answer given by user
def checkAns():
  numRange = (1, 5)
  randNum = random.randint(numRange[0], numRange[1])
  userAns = float(input('What number between 1 and 5 am I thinking of: '))

  if userAns == randNum:
    global score 
    score += 1
    return alert('correct', randNum)
  if userAns + 2 or userAns + 1 == randNum:
    return alert('incorrect', randNum)
  if userAns - 2 or userAns - 1 == randNum:
    return alert('incorrect', randNum)

# Function to check the amount scored and return message
def checkScore(score):
  if score <= 1:
    awardAlert('plastic')
  if score > 1 and score < 4:
    awardAlert('silver')
  if score >= 4:
    awardAlert('gold')

# Function that initalizies the game
def initGame():
  num = 0
  message = 'You will get 5 chances to guess a number between 1 and 5'
  print(message)

  while num != 5:
    num += 1
    checkAns()
  
  checkScore(score)

initGame()
