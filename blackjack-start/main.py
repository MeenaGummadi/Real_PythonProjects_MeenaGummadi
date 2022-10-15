############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from art import logo
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list):
  if sum(list) == 21 and len(list) == 2:
    return 0
  if sum(list) > 21 and 11 in list:
    list.remove(11)
    list.append(1)
  return sum(list)
  
def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Game is draw")
    elif computer_score == 0:
        print("Computer Win with a blackjack")
    elif user_score == 0 :
        print("User Win with a blackjack")
    elif user_score > 21:
      print("You went over the score. Computer win")
    elif computer_score > 21:
      print("Computer went over the score. You win")
    elif computer_score > user_score:
      print("Computer Win")
    else:
      print("User Win")
def play_game():  
  is_gameEnd = False
  print(logo)
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  
  
  while (is_gameEnd == False):
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
    
      print(f"user cards are {user_cards}, user_score is {user_score}")
      print(f"computer's first card is {computer_cards[0]}")
  
      if user_score == 0 or computer_score == 0 or user_score > 21:
        is_gameEnd = True
      else:
        user_another_card = input("Do you want another card? Type 'y' or 'n': ")
        if user_another_card == 'y':
          user_cards.append(deal_card())
        else:
          is_gameEnd = True
            
  while (computer_score < 17 and computer_score != 0):
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"\nUser's final cards are : {user_cards} and user_score is {user_score} ")
  print(f"computer's final cards are: {computer_cards} and computer_score is {computer_score}")
  
  if is_gameEnd == True:
      compare(user_score, computer_score)


while(input("\nDo you want to play the game of Blackjack? Type 'y' or 'n': ") == 'y'):
  clear()
  play_game()