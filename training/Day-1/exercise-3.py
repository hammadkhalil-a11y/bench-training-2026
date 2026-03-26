def table(number):
    for i in range(1,11):
        print(number," x ",i,"=",number*i)


while(True):
    number = int(input("Please enter a number in a range of 1 - 12:"))

    if 1<= number <=12:
        table(number)
        break
    else:
        number = input("Please enter a valid number in a range of 1 - 12:")
        continue
