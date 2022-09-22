import time

# lists displayed to user 
list_a = [10,8,12,15,9,11,13,14]
list_b = [4,14,7,6,12,13,5,15]
list_c = [2,11,6,3,14,7,15,10]
list_d = [11,1,13,5,7,3,9,15]


# answer dictionary to find the user's number
answer_dict={'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', 
            '8' : '1000', '9' : '1001', '10' : '1010', '11' : '1011', '12' : '1100', '13' : '1101', '14' : '1110', '15' : '1111'}


# function 
def read_mind():
    answer_list=[]
    run = start()

    # let the user think of any number user like from 1-15, ask them to write down somewhere 

    while run:
        answer_list=[]
        # answer_str = ""

    # disply list of numbers A, and ask if the number is in this list    
    # save the answer in the list (yes=1 no=0)
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
        time.sleep(1)
        print(" hmmm.. I see what you have in your mind")
        time.sleep(1)
        print(" .....")
        time.sleep(1)
        print(" You have ... ")
        time.sleep(1)
        print ( f" {guess} in your mind. ")
        time.sleep(1)

# display the result and ask user to confirm the result, and ask if the user wants to play again
        run = get_result(guess)
        
    return 


# start game 
def start():
    print(" I can read your mind with 4 random questions. Please think of any number between 0-15, and write it down somewhere near. ")
    time.sleep(2)
    valid_input = False

    while (not valid_input) :
        start = input(" Do you want to continue?  Please, select 1. Yes 2. No : ")
        if start == "1" :
            run = True
            valid_input = True
        elif start == "2" :
            print(" See you again! ")
            valid_input = True
            run = False
        else: 
            print(" Please, type valid number. ")
            valid_input = False

    return run


# asking user if the number is in displayed lists, and return the user input 
def get_answer(list):

    answer = input(f" Is your number in this list? {list} please, select 1. Yes 2. No : ")
    valid_input = False
    while (not valid_input) :
        if answer == "1" :
            answer = "1"
            valid_input = True
        elif answer == "2" :
            answer = "0"
            valid_input = True
        else :
            print(" Please, type valid number.")
            answer = input(f" Please, type valid number. Is your number in this list? {list} 1. Yes 2. No : ") 
            valid_input = False

    return answer


# display result - if the guess is incorrect, ask user if he wants to play again. if yes, run the game again, if no, end the loop
def get_result(guess):
    
    valid_confirm = False
    while(not valid_confirm) :  
        confirm = input(f" Is {guess} correct number? please, select 1. Yes 2. No : ")  
        if confirm == "1":
            valid_confirm = True
            print(" Thank you. I see lots of great things coming to your life. Good luck! ")
            run = False        
        elif confirm == "2":
            valid_confirm = True
            valid_replay = False
            while(not valid_replay):
                replay = input(" Hmm.. Are you sure? Please, double check your number! Do you want to try again? please, select 1. Yes 2. No : ")
                if replay == "1":
                    run = True
                    valid_replay = True
                elif replay == "2":
                    print(" Thank you! See you again! ")
                    run = False
                    valid_replay = True
                else : 
                    valid_replay = False
                    print(" Please, type valid number. ")                
        else: 
            print(" Please, type valid number. ")
    return run

if __name__ == "__main__":
    read_mind()


#TODO int('1111',2)