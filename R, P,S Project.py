import random
# تعریف تصاویر
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper ='''    
_______
---'    ____)____
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

choices = ["rock", "paper", "scissors"]
ascii_art = {"rock":rock, "paper":paper, "scissors":scissors}

user_input = input("what do you chose? Type 0 for rock, 1 for paper,or 2 for scissors:")

if user_input in ["0", "1", "2"]:
    user_index = int(user_input)
    user_choice = choices[user_index]
computer_choice = random.choice(choices)
if user_choice in choices:
    print("\nYou chose:")
    print(ascii_art[user_choice])

    print("Computer chose:")
    print(ascii_art[computer_choice])

if user_choice == computer_choice:
    print("It is a draw")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("You typed an Invalid number,You lose!")


    






