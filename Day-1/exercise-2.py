def result(marks):
    if marks > 90:
        return "Distinction"
    elif  60<=  marks <=90:
        return "Pass"
    else:
        return "Fail"

print(result(23))
print(result(75))
print(result(93))

marks = [45, 72, 91, 60, 38, 85]

for value in marks:
    if value > 90 :
        print("Result for this",value," is",result(value))
    elif  60<= value <=90 :
        print("Result for this",value," is",result(value))
    else:
        print("Result for this",value," is",result(value))
