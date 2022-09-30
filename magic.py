#!/usr/bin/env python3
"""Alice Huh - pyton If logic - Project 1 """

# import time module
import time

# ask user to think of any number from 1-15, ask the user to write it down somewhere   
def start():

    valid_input = False

    while (not valid_input) :
        start = input(" Do you want to continue?  Please, select 1. Yes 2. No : \n ")
        if start == "1" :
            run = True
            valid_input = True
        elif start == "2" :
            print(" See you again! \n")
            valid_input = True
            run = False
        else: 
            print(" Please, type valid number. \n")
            valid_input = False

    return run


# asking user if the number is in displayed lists, and return the user input 
def get_answer(list):

    answer = input(f" Is your number in this list? {list} please, select 1. Yes 2. No : \n ")
    
    valid_input = False
    while (not valid_input) :
        if answer == "1" :
            answer = "1"
            valid_input = True
        elif answer == "2" :
            answer = "0"
            valid_input = True
        else :
            print()
            answer = input(f" Please, type valid number. Is your number in this list? {list} 1. Yes 2. No : \n ") 
            valid_input = False

    return answer


# display result - if the guess is incorrect, ask user if he wants to play again. if yes, run the game again, if no, end the loop
def get_result(guess):
    
    valid_confirm = False
    while(not valid_confirm) :  
        confirm = input(f" Is {guess} correct number? please, select 1. Yes 2. No : \n ") 
        if confirm == "1":
            valid_confirm = True
            print(" Thank you. I see lots of great things coming to your life. Good luck! \n ")
            run = False        
        elif confirm == "2":
            valid_confirm = True
            valid_replay = False
            while(not valid_replay):
                replay = input(" Hmm.. Are you sure? Please, double check your number! Do you want to try again? please, select 1. Yes 2. No : \n ")
                if replay == "1":
                    run = True
                    valid_replay = True
                elif replay == "2":
                    print(" Thank you! See you again! \n ")
                    run = False
                    valid_replay = True
                else : 
                    valid_replay = False
                    print(" Please, type valid number. \n ")
                                    
        else: 
            print(" Please, type valid number. \n ")
    return run



def main():

    # lists displayed to user 
    list_a = [10,8,12,15,9,11,13,14]
    list_b = [4,14,7,6,12,13,5,15]
    list_c = [2,11,6,3,14,7,15,10]
    list_d = [11,1,13,5,7,3,9,15]

    # answer dictionary to find the user's number
    answer_dict={'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', 
                '8' : '1000', '9' : '1001', '10' : '1010', '11' : '1011', '12' : '1100', '13' : '1101', '14' : '1110', '15' : '1111'}
    
    # user input will be appended into this list
    answer_list=[]

    # Intro
    user_name = input(" Weclome! what is your name? \n ")
    time.sleep(1)
    print(f" Okay, {user_name}! I can read your mind with 4 random questions. Please think of any number between 0-15, and write it down somewhere near. \n")
    time.sleep(3)

    # start game by calling function start   
    run = start()

    while run:

        answer_list=[]
        
        # disply list of numbers A, and ask if the number is in this list and        
        answer = get_answer(list_a)
        answer_list.append(answer)
        time.sleep(1)
    
        answer = get_answer(list_b)
        answer_list.append(answer)
        time.sleep(1)

        answer = get_answer(list_c)
        answer_list.append(answer)
        time.sleep(1)

        answer = get_answer(list_d)
        answer_list.append(answer)
        time.sleep(1)    

        # find the number from the answer dictionary 
        guess = list(answer_dict.keys())[list (answer_dict.values()).index(''.join(answer_list))]
        
        
        print(f" hmmm.. I see what you have in your mind, {user_name} ... \n ")
        time.sleep(1)
    
        print(" ..... \n")
        time.sleep(1)

        print(" You have ... \n")
        time.sleep(2)

        print ( f" {guess} in your mind. \n")

        time.sleep(1)

        # display the result and ask user to confirm the result, and ask if the user wants to play again
        run = get_result(guess)
        
    return 



if __name__ == "__main__":
    main()


