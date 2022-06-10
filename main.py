from time import sleep
print("\n") ; sleep(0.1)
print("===== Welcome to the Vegas Video Game Character Machine =====")
print("===== Enter in an amount of money you have, then type in the name of a famous game character, and see how much money you win or lose ===== \n") ; sleep(1)

dollars = int(input("How much money do you have? $"))

tryAgain = "Y"


while (tryAgain == "Y"):
  VGCharacter = input("What video game character do you choose? ")
    
  print("\n") ; sleep(1)

  if VGCharacter == "Sonic" or VGCharacter == "Tails":
    print(" > Good call, I will double your money. \n") ; sleep(2)
    winnings = dollars * 2
    print("You win " + str(winnings) + " dollars!")

  elif VGCharacter == "Mario" or VGCharacter == "Luigi":
    print(" > Good call, I will triple your money. \n") ; sleep(2)
    winnings = dollars * 3
    print("You win " + str(winnings) + " dollars!")

  elif VGCharacter == "Pikachu" or VGCharacter == "Yoshi":
    print(" > Great call, I will quadruple your money. \n") ; sleep(2)
    winnings = dollars * 4
    print("You win " + str(winnings) + " dollars!")

  elif VGCharacter == "Daxter":
    print(" > Like Professor Nimri, he thought he was funny, but wasn't.  You lose $5. \n") ; sleep(2)
    winnings = dollars - 5
    print("You leave with " + str(winnings) + " dollars.")

  elif VGCharacter == "Bubsy":
    print(" > I\'ll forget you mentioned him for 10 dollars. \n") ; sleep(2)
    winnings = dollars - 10
    print("You leave with " + str(winnings) + " dollars.")

  elif VGCharacter == "Herobrine":  
    print(" > He technically isn\'t official.  You lose 25 dollars. \n") ; sleep(2)
    winnings = dollars - 25
    print("You leave with " + str(winnings) + " dollars.")

  elif VGCharacter == "Baldi":  
    print(" > No.  Lose 100 dollars. \n") ; sleep(2)
    winnings = dollars - 100
    print("You leave with " + str(winnings) + " dollars.")

  elif VGCharacter == "Donkey Kong" or VGCharacter == "Bowser":
    print(" > Good call, but Mario is better.  I'll call Mario for you. \n") ; sleep(1.5)
    print(" > \"It\'s-a me!  Mario!  Let me triple your money!  Yahoo!\" \n") ; sleep(2)
    winnings = dollars * 3
    print("You win " + str(winnings) + " dollars!")

  else:
    print(" > Character is not recognized. \n") ; sleep(1)
    winnings = dollars
    print("You leave with what you started with, which is " + str(winnings) + " dollars.")
  dollars = winnings
  if dollars <= 0:
    print("\n") ; sleep(1)
    print ("===== You lose, good day. =====")
    break
  print("\n") ; sleep(1)
  tryAgain = input(" Play again? Y/N: ")
  print("\n") ; sleep(1)

else:
  print("===== Thanks for playing! =====")


