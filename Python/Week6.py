grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25,8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(class_name):
    list1=list(class_name.keys())
    return list1
def student_score(class_name,student_name):
    sum1=(sum(class_name[student_name]))
    return student_name,sum1
def students_count(class_name):
    names=list(class_name.keys())
    count=len(names)
    return count

while True:
    a=input("Choose one: students_names, student_score, students_count: ")
    if a=='students_names':
        class_name=input('enter your class name: ')
        if class_name=='grade_one':
            list1=list(grade_one.keys())
        elif class_name=='grade_two':
            list1=list(grade_two.keys())
        elif class_name=='grade_three':
            list1=list(grade_three.keys())
        print(list1)
    elif a=='student_score':
        class_name=input('enter your class name: ')
        student_name=input('enter your student name: ')
        if class_name=='grade_one':
            sum1=(sum(grade_one[student_name]))
        elif class_name=='grade_two':
            sum1=(sum(grade_two[student_name]))
        elif class_name=='grade_three':
            sum1=(sum(grade_three[student_name]))
        print(student_name,sum1)

    elif a=='students_count':
        class_name=input('enter your class name: ')
        if class_name=='grade_one':
            count=len(grade_one)
        elif class_name=='grade_two':
            count=len(grade_two)
        elif class_name=='grade_three':
            count=len(grade_three)
        print(count)
    b=input("if you are finish enter done if not enter more: ")
    if b =="done":
        break
    
