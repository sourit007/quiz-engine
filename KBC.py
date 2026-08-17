print("WELCOME TO KAUN BANEGA CROREPATI!!!!!")
A = [
    "Q.1) What is the capital of India? \n a: Kolkata \n b: Delhi",
    "Q.2) What is the capital of Uttar Pradesh? \n a: Lucknow \n b: Delhi",
  "Q.3) What is the capital of Maharashtra? \n a: Mumbai \n b: Ajmer",
  "Q.4) What is the capital of Bihar? \n a: Dhanbad \n b: Patna",
  "Q.5) What is the capital of Rajasthan? \n a: Jaipur \n b: Udaipur"
]

for i in range(5):
    if i == 0:
        print(A[i])
        ans = input("Enter your answer: ")
        if ans == "b":
            print("Congratulations! You have won Rs.10,000")
        else:
            print("Sorry! You have lost the game")
            break
    elif i == 1:
        print(A[i])
        ans = input("Enter your answer: ")
        if ans == "a":
            print("Congratulations! You have won Rs.25,000")
        else:
            print("Sorry! You have lost the game")
            break
    elif i == 2:
        print(A[i])
        ans = input("Enter your answer: ")
        if ans == "a":
            print("Congratulations! You have won Rs.50,000")
        else:
            print("Sorry! You have lost the game")
            break
    elif i == 3:
        print(A[i])
        ans = input("Enter your answer: ")
        if ans == "b":
            print("Congratulations! You have won Rs.10,00,000")
        else:
            print("Sorry! You have lost the game")
            break
    else:
        print(A[i])
        ans = input("Enter your answer: ")
        if ans == "a":
            print("Congratulations! You have won Rs.1,00,00,000")
            print("You are the winner!!!")
        else:
            print("Sorry! You have lost the game")

print("\n 'Thank you for playing KBC'")