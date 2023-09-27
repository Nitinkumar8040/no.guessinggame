while True:
 import random
 cn = random.randrange(0,9)
 choice = input("if are quit then type 'Q' or 'q' otherwise press enter---")
 if choice == "Q" or choice == "q":
     break
 un = int(input("guess a number :"))
 if cn>un:
      print("draw number is :",cn)
      print(("sorry , your number is too high."))
 elif cn<un:
      print("draw number is :", cn)
      print(("sorry , your number is too low."))
 else:
     print("draw number is :", cn)
     print("congratulation, you are win")
