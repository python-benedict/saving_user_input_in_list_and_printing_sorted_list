listOfUsersInput = []

while True:
    user_input = int(input("Enter a number : "))
    if user_input != 0:
        listOfUsersInput.append(user_input)
    else:
        listOfUsersInput.sort()
        print(listOfUsersInput)
        break