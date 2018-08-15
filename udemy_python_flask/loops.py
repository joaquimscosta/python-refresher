my_variable = "hello"
for char in my_variable: # interables are strings, lists, sets, tuples, and more...
    print(char)

my_list = [1, 2, 3, 4, 7, 9]
for number in my_list:
    print(number ** 2)

users_wants_number = True
while users_wants_number == True:
    print(10)
    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        users_wants_number = False