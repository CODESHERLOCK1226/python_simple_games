rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_choice=[rock,paper,scissors]
print("Enter 0 for rock, 1 for paper, 2 for scissors")
user=int(input())
if user<=2 and user>=0:
  print(game_choice[user])

else:
  print("U have entered a invalid character")

if user>=0 and user <=2:
  import random
  computer_choice=random.randint(0,2)
  print(game_choice[computer_choice])

  if user==computer_choice:
    print("Voila! It's a draw")
  elif (user==0 and computer_choice==1) :
    print("You lose") 
  if user==1 and computer_choice==2:
    print("You lose")
  if user==2 and computer_choice==0:
    print("You lose")
  else:
    print("You Win.")

  
