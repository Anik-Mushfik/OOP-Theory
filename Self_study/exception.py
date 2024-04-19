try:
    print(5/0)
except ZeroDivisionError:
    print('Learn Math First You Eddiot!!')


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\nFirst Number: ")
    if first_num == "q":
        break
    second_num = input("Second Number: ")
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: print(answer)