import random
def get_guess():
    while True:

        try:
            user_input = input("Enter a number: ")
            user_list = []
            for item in user_input:
                user_list.append(int(item))
            illegal_num1 = False
            illegal_num2 = False
            illegal_length = False
            for number in user_list:
                if number > 7 or number < 1:
                    illegal_num1 = True
                if user_list.count(number) > 1:
                    illegal_num2 = True
                if len(user_input) != 4:
                    illegal_length = True
            if illegal_num1:
                print "The number is not in range 1-7."
            if illegal_num2:
                print "The number should be unique."
            if illegal_length:
                print "The guess should have a length of 4."
            if not illegal_num1 and not illegal_num2 and not illegal_length:
                return user_list
        except ValueError:
            print "Please enter only numbers. Error 404!"


def check_values(list1, list2):
    response = []
    for number in list2:
        if number in list1:
            if list1.index(number)==list2.index(number):
                response.append("RED")
            else:
                response.append("WHITE")
        else:
            response.append("BLACK")
    print response
    return(check_win(response))

def check_win(response_list):
    num = 0
    for item in response_list:
        if item == "RED":
            num = num + 1
    if num == 4:
        print "You win"
    else:
        print "Incorrect. Try again if guesses left."

numlist = [1,2,3,4,5,6,7]
reallist = []
for i in range(4):
    selectnum = random.choice(numlist)
    numlist.remove(selectnum)
    reallist.append(selectnum)


def play_game():
    game_list = reallist
    total_guesses = 0
    while total_guesses < 5:
        print "Guesses remaining: " + str(5 - total_guesses)
        user_input = get_guess()
        if check_values(game_list, user_input) == 4:
            total_guesses = 6
            break
        total_guesses = total_guesses + 1
    if total_guesses == 5:
        print "Sorry! That's all the guesses you get!"
        print "This is the correct answer:"
        print game_list
    print "Thanks for Playing!"
play_game()   
