import random
#This allows the use of our randint() function
exitChoice = "Nothing"
#This is our condition for the while loop
while exitChoice != "EXIT":
  print("You are in a dark room in a mysterious castle.")
  #This sets the scene.
  print("In front of you there are four doors. You must Choose one.")
  playerChoice = input("Choose 1, 2, 3 or 4...")
  #This gives the player an option between three doors.
  #This if statement tests if the user typed in 1,
  if playerChoice == "1":
    #This tells the program what to do when that happens.
    print("You find a room full of treasure. You're rich!")
    print("GAME OVER, YOU WIN!")
  #This if statement tests if the user typed in 2,
  elif playerChoice == "2":
    #This tells the program what to do when that happens.
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE!")
  #This if statement tests if the user typed in 3,
  elif playerChoice == "3":
    #This tells the program what to do when that happens.
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to exit.")
    #The next sequence creates another option,
    dragonChoice = input("Type 1 or 2... ")
    if dragonChoice == "1":
      #This if statement tests if the user typed in 1,
      print("The dragon wakes up and eats you. You are delicious.")
      print("GAME OVER, YOU LOSE!")
      #This tells the program what to do when that happens.
    elif dragonChoice == "2":
      #This if statement tests if the user typed in 2,
      print("You sneak around the dragon and excape the castle, blinking in the sunshine.")
      print("GAME OVER! YOU WIN!")
      #This tells the program what to do when that happens.
    else:
      #Otherwise, this will happen when the ifs inside of this elif are incorrect.
      print("Sorry, you didn't enter 1 or 2!")
  #This if statement tests if the user typed in 4,
  elif playerChoice == "4":
    #This tells the program what to do when that happens.
    print("You enter a room with a sphinx.")
    print("It asks you to guess what number it is thinking of, between 1 and 10.")
    number = int(input("What number do you choose? "))
    #The next sequence creates another option,
    if number == random.randint(1, 10):
      print("The sphinx hisses in disappointment. You Guessed Correctly.")
      print("She must let you go free.")
      print("GAME OVER. YOU WIN!")
      #You have to randomly guess the numbers 1-10 in order to win
    else: 
      print("The sphinx tells you that your guess is incorrect.")
      print("You are now her prisoner forever.")
      print("GAME OVER, YOU LOSE!")
      #Or else, you lose.
  else:
    #Otherwise, this will happen when the ifs above are incorrect
    print("Sorry, you didn't enter 1, 2, 3 or 4!")
  #Then this will print to prompt the user to restart the game
  exitChoice = input("Press return to play again, or type EXIT to leave.")