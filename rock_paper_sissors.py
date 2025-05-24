import random
print("Rock, Paper, Sissors\n"
      + "Rock = 1 \n"
     + "Paper = 2 \n" 
     + "Sissors = 3")
options = {}
def main():
 while True:
  
  #User enters number from 1-3 symbolizing rock paper sissors
   user_option = int(input("Enter your weapon of choice: "))
   while user_option > 3 or user_option < 1:
       user_option = int(input("Please enter a number from the objects listed above!: "))
   

   if user_option == 1:
     user_device = 'rock'
   elif user_option == 2:
     user_device = 'paper'
   elif user_option == 3:
       user_device = 'sissors'
   print('Your choice:', user_device)
  
   #Computer randomly selects number from 1-3
   computer = random.randint(1, 3)
   if computer == 1:
     comp_device = 'rock'
   elif computer == 2:
     comp_device = 'paper'
   elif computer == 3:
       comp_device = 'sissors'
   print("Computer chooses", comp_device)

   if user_option == 1 and computer == 2:
     print("Computer Wins! Paper beats Rock")
   if user_option == 1 and computer == 3:
     print("User wins. Rock smashes sissors!")
   if user_option == 2 and computer == 1:
     print("User wins. Paper covers rock!")

   if user_option == 2 and computer == 3:
    print("You Lose. Sissors beats paper!")
   if user_option == 3 and computer == 1:
    print("You lose. Rock beats sissors!")
   if user_option == 3 and computer == 2:
    print("you win. Sissors beats paper")
   if user_option == computer:
      print("You have a draw. Please play again.")
    
   play = input("Would you like to play again? y/n?").lower()
   if play != "y":
    print("Game Overrr!")
    break
  
   
if __name__ == "__main__":
    main()

