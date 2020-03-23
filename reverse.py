def reverse_number():
    number = int(input("Enter a five digit number number"))
    reverse = 0
    while(number > 0):
        reminder = number % 10
        reverse = (reverse*10) + reminder
        number = number//10
    print("The reverse of the number is",reverse)
reverse_number()

