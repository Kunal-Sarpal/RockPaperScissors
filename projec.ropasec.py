import random
scissor = '''
 _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

paper = '''

8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                         

'''

rock = '''
              
                       
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  


'''
games_images = [rock, scissor,paper]
User_choice = int(input("What do you choose? Type 0 for rock , 1 for Paper or 2 for Scissors.\n"))
if User_choice >=3 or User_choice < 0:
    print("you type an invalid number, you lose!.")
else:
    print(games_images[User_choice])
computer_choice  = random.randint(0,2)
print("computer choose: ")
print(games_images[computer_choice])



if User_choice == 0 and computer_choice == 2:
    print("You Wins")
elif computer_choice == 0 and User_choice == 2:
    print("you lose") 
elif computer_choice > User_choice:
    print("You lose")
elif User_choice > computer_choice :
    print("You Wins")
elif computer_choice == User_choice:
    print("It's Draw")
elif User_choice >=3 or User_choice < 0:
    print("you type an invalid number, you lose")


