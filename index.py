import random 

print("Welcome to RPS")

user_score=0
comp_score=0
ties=0

name=input("Enter your Name here: ")
print ( """
Winning Rules:
1. Paper vs Rock > Paper
2. Rock vs Scissors > Rock
3. Scissor vs Paper > Scissor""" )
print()

print ("""Choices are:
       1. Rock
       2. Paper
       3.Scissor""")

choice=int(input("Enter your choice from 1-3: "))
print ()
while choice > 3 or choice < 1:
    choice =int(input("Enter valid input"))

if choice == 1 :
  user_choice = "Rock"
elif choice == 2 :
  user_choice = "Paper"
else:
  user_choice = "Scissor"

print ("The user's choice is",user_choice )
print ("Now it is Computer's turn")

computer = random.randint(1,3)
if computer == 1 :
       comp_choice = "Rock"
elif computer == 2 :
       comp_choice  = "Paper"
else:
        comp_choice = "Scissor"

print ("The computer's choice is",comp_choice)

if ((user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Rock")):
         print("Paper Win!")
         result = "Paper"
elif ((user_choice == "Scissor" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissor")):
         print("Rock Win!")
         result = "Rock"   
elif(user_choice==comp_choice): 
   print("It's a tie!")
   result = "Tie"       
else:
    print("Scissor Win!")
    result = "Scissor"   

if result == "Tie":
      ties +=1
elif result == user_choice:
      print ("user wins")
      user_choice +=1
else:
    print ("computer wins")
    comp_choice +=1

print ("Scores are")
print (name, "'s score is", user_score)
print ("computer's score is", comp_score)
print ("Ties are", ties)