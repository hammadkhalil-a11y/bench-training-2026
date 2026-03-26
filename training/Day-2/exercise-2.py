
students = [{"name":"Hammad","scores":[77,88,99,64,100],"subject":"Database"},{"name":"Hamza","scores":[84,88,69,70,70],"subject":"Programming Fundamentals"},{"name":"Azaan","scores":[71,98,63,77,90],"subject":"OOP"}]

def calculate_average(scores):
    total=0
    for score in scores:
        total+=score

    return total/ len(scores)

def get_grade(avg):
    if avg>90:
        return "A"
    elif avg>80:
        return "B"
    elif avg>70:
        return "C"
    elif avg>60:
        return "D"
    else:
        return "F"


def class_topper(students):
    top_student = max(students, key=lambda s:calculate_average(s["scores"]))
    return top_student


topper =  class_topper((students))
print(f"{'Name':<10} | {'Avg Score':<9} | {'Grade'}")

for std in students:
    avg=calculate_average(std["scores"])
    grade=get_grade(calculate_average(std["scores"]))
    if std == topper:
        print( "***** TOP *****")
    line = f"{std['name']:<10} | {avg:9} | {grade}"
    print(line)