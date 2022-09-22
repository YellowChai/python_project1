import random

# variable: user_input(string), user_answer(list), answer_dict(dictionary number(1-15):answer_list), listA(list), listB(list), listC(list), listD(list)
list_a = [8,9,10,11,12,13,14,15]
list_b = [4,5,6,7,12,13,14,15]
list_c = [2,3,6,7,10,11,14,15]
list_d = [1,3,5,7,9,11,13,15]

answer_dict={'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000',
            '9': '1001', '10' : '1010', '11' : '1011', '12' : '1100', '13' : '1101', '14' : '1110', '15' : '1111'}


def read_mind():
    answer_list=[]
    print(" I can read your mind. Please think of any number between 1-15, and write it down somewhere near. ")
    start_game = input(" Do you want to continue? Please, type number 1. Yes 2. No ")
    if start_game == "1" :
        run = True
    elif start_game == "2" :
        print(" Plase, visit again! ")
        run = False
# let the user think of any number user like from 1-15, ask them to write down somewhere 
# disply list of numbers A, and ask if the number is in this list    
# save the answer in the list (yes=1 no=0)
    while run:
        answer_list=[]
        answer = get_answer(list_a)
        answer_list.append(answer)
        print(answer_list)
    
# display list of numbers B, and ask if the number is in this list
# append the answer to the answer list (yes=1 no=0)
        answer = get_answer(list_b)
        answer_list.append(answer)
    
# display list of number C, and ask if the number is in this list
# append the answer to the answer list (yes=1 no=0)
        answer = get_answer(list_c)
        answer_list.append(answer)

# display list of number D, and ask if the number is in this list 
# append the answer to the answer list (yes=1 no=0)
        answer = get_answer(list_d)
        answer_list.append(answer)

# check the dictionary for the guessing number (key= user_number value= answer_list) 
# display the answer from the dict and ask the user if the answer is correct. if aswer is correct, exit the while loop
# if user say the answer is incorrect, ask user if he wants to play again. if yes, run the game again, if no, exit the loop
        print ( f"You have {list(answer_dict.keys())[list (answer_dict.values()).index(''.join(answer_list))]} in your mind. ")
        confirm = input(" Is this correct? please, type number 1. Yes 2. No : ")
        if confirm == "1":
            print(" Thank you. I see lots of great things coming to your life. Good luck! ")
            # run = False
            break        
        elif confirm == "2":
            replay = input(" Hmm.. Are you sure? Please, double check your number! Do you want to try again? please, type number 1. Yes 2. No: ")
            if replay == "1":
                run = True
            elif replay == "2":
                run = False               

    return 


def get_answer(list):
    # user_answer=[]
    answer = input(f" Is your number in this list? {list} please, type number 1. Yes 2. No : ")
    if answer == "1" :
        answer = "1"
    elif answer == "2" :
        answer = "0"
    else :
        print("Please, type valid number.")
        answer = input(" Is your number in this list? please, type number 1. Yes 2. No : ")
    print(answer)
    return answer

read_mind()

# possible errors
# invalid input 
# A. number input when needed yes or no - can be solved by 1. provide both options or 2. error message to choose the word yes or no 
# B. Capital letter input - make all lowercase 
# C. Y or YES - allow both input
# D. invalid letters - error message(A can be solved with this)
