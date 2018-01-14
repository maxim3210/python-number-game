import random

def newgamegen():
  print("Welcome to Random Number Guesser. I will generate a random number between 0-999, and you will try to guess that number. With each guess, I will tell you if you are getting closer or farther!")
  rnumber = ''
  chars = "1234567890"
  if rnumber == '':
    for f in range(3):
      rnumber += random.choice(chars)
  
  if rnumber[0] and rnumber[1] == "0":
    rnumber = rnumber[2:]
  elif rnumber[0] == "0":
    rnumber = rnumber[1:]
    
  #print(rnumber)  
  
  userinput = ""
  numb = 0
  
  distance = ""
  while userinput != rnumber:
    wongame = 0
    if len(distance) >= 0:
      olddistance = distance
    userinput = input("Choose a number: ")
    while userinput == "" or not str.isdigit(userinput):
      print("Not a number. Try again.")
      userinput = input("Choose a number: ")

    
    distance = userinput
    distance = str(distance)
    olddistance = str(olddistance)
    numb = numb + 1
    if len(olddistance) >= 0 and olddistance != "":
      myList = [int(distance),int(olddistance)]
      myNumber = int(rnumber)
      closestDis = min(myList, key=lambda x:abs(x-myNumber))
      if str(closestDis) == distance : 
        print("You're getting closer.")
      elif str(closestDis) == olddistance:
        print("You're getting farther")
      else:
        print("You haven't moved.")
    
  tries = "tries"
  if numb == 1:
    tries = "try"
  if userinput == rnumber:
    print("You got the number! It was %s." % rnumber)
    print("It took you %s %s." % (numb, tries))
    wongame = 1
  playagain = ""
  while playagain != "Y" or "N":
    if wongame == 1:
      playagain = input("Would you like to play again? (Y/N) ")
      playagain = playagain.upper()
      if playagain == "Y":
        newgamegen()
      elif playagain == "N":
        print("Thank you for playing!")
        quit()
      else:
        print("Invalid answer.")
        
      
newgamegen()


  
  
    
    
    