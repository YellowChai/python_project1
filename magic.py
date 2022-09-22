
# lists displayed to user 
list_a = [8,9,10,11,12,13,14,15]
list_b = [4,5,6,7,12,13,14,15]
list_c = [2,3,6,7,10,11,14,15]
list_d = [1,3,5,7,9,11,13,15]

# answer dictionary to find the user's number
answer_dict={'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', 
            '8' : '1000', '9' : '1001', '10' : '1010', '11' : '1011', '12' : '1100', '13' : '1101', '14' : '1110', '15' : '1111'}


# function 

def read_mind():
    answer_list=[]
    run = start()

# let the user think of any number user like from 1-15, ask them to write down somewhere 
# disply list of numbers A, and ask if the number is in this list    
# save the answer in the list (yes=1 no=0)
    while run:
        answer_list=[]
        answer = get_answer(list_a)
        answer_list.append(answer)
    
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

        guess = list(answer_dict.keys())[list (answer_dict.values()).index(''.join(answer_list))]
        print ( f" You have {guess} in your mind. ")

# ask user to confirm the result, and ask if the user wants to play again
        run = get_result(guess)
        
    return 


def start():
    print(" I can read your mind. Please think of any number between 1-15, and write it down somewhere near. ")
    valid_input = False
# ask if user wants to start  
    while (not valid_input) :
        start = input(" Do you want to continue? Please, type number 1. Yes 2. No : ")
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


# asking user if the number is in displayed lists, and return the answer
def get_answer(list):

    answer = input(f" Is your number in this list? {list} please, type number 1. Yes 2. No : ")
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


# if the guess is incorrect, ask user if he wants to play again. if yes, run the game again, if no, exit the loop
def get_result(guess):
    
    valid_confirm = False
    while(not valid_confirm) :  
        confirm = input(f" Is {guess} correct number? please, type number 1. Yes 2. No : ")  
        if confirm == "1":
            valid_confirm = True
            print(" Thank you. I see lots of great things coming to your life. Good luck! ")
            run = False        
        elif confirm == "2":
            valid_confirm = True
            valid_replay = False
            while(not valid_replay):
                replay = input(" Hmm.. Are you sure? Please, double check your number! Do you want to try again? please, type number 1. Yes 2. No : ")
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

read_mind()


