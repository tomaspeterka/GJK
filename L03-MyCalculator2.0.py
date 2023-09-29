def float_input (text):
    # Parameter text defines what will be shown when asking for user input
    while True:
            try:
                user_input = float(input(text))
                return user_input
                break
            except ValueError:
                print("Invalid Input. Try again...")

print ("This is simple calculator created by Tomas Peterka")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
        
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            
            #num1 = float(input("Enter first number: "))
            #num2 = float(input("Enter second number: "))

            num1 = float_input("Enter first number: ")
            num2 = float_input("Enter second number: ")

            if num1 + num2 > 10:
                print ("Are you crazy? This will take me at least 4 minutes to count.")
                guess = float_input("To speed up the process of counting, write your estimated result here: ")


            if choice == '1':
                main_result = num1 + num2
                print(num1, "+", num2, "=", main_result)

            elif choice == '2':
                main_result = num1 - num2
                print(num1, "-", num2, "=", main_result)

            elif choice == '3':
                main_result = num1 * num2
                print(num1, "*", num2, "=", main_result)

            elif choice == '4':
                main_result = num1 / num2
                print(num1, "/", num2, "=", main_result)


            if num1 + num2 <= 10:
                guess = main_result

            if num1 + num2 > 10:
                if guess == main_result:
                    print ("You've been right! Congrats :) ")
                if guess != main_result:
                    print ("You constantly need everything fast. And If you do it, it's not right!")
                

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                print("I understand you want to continue :)")
                break


        else:
            print("Invalid Input")


