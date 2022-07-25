import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))
computer = random.randint(0, 2)
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("Hey User! Please select the appropriate number between 0 and 1")
if computer == 0:
    print("Computer's choice is rock")
    print(rock)
elif computer == 1:
    print("Computer's choice is paper")
    print(paper)
elif computer == 2:
    print("Computer's choice is scissors")
    print(scissors)
else:
    print("Wrong selection by computer")
if (user == computer):
    print("game is draw.")
if ((user == 0 and computer == 1) or (user == 1 and computer == 2)
        or (user == 2 and computer == 0)):
    print("computer won, user lost")
if ((user == 1 and computer == 0) or (user == 0 and computer == 2)
        or (user == 2 and computer == 1)):
    print("computer lost, user won")
