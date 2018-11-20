grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25,8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(class_name):
    if class_name=='grade_one':
        list1=list(grade_one.keys())
    elif class_name=='grade_two':
        list1=list(grade_two.keys())
    elif class_name=='grade_three':
        list1=list(grade_three.keys())
    return list1
def student_score(class_name,student_name):
    if class_name=='grade_one':
        sum1=(sum(grade_one[student_name]))
    elif class_name=='grade_two':
        sum1=(sum(grade_two[student_name]))
    elif class_name=='grade_three':
        sum1=(sum(grade_three[student_name]))
    return student_name,sum1
def students_count(class_name):
    return len(class_name)

a=input("Choose one: students_names, student_score, students_count: ")
if a=='students_names':
    class_name=input('enter your class name: ')
    print(students_names(class_name))
elif a=='student_score':
    class_name=input('enter your class name: ')
    student_name=input('enter your student name: ')
    print(student_score(class_name,student_name))
elif a=='students_count':
    class_name=input('enter your class name: ')
    print(students_count(class_name))

b=input("if you are finish enter done if not enter more: ")
while b=='more':
    a=input("Choose one: students_names, student_score, students_count: ")
    if a=='students_names':
        class_name=input('enter your class name: ')
        print(students_names(class_name))
        b=input("if you are finish enter done if not enter more: ")
    elif a=='student_score':
        class_name=input('enter your class name: ')
        student_name=input('enter your student name: ')
        print(student_score(class_name,student_name))
        b=input("if you are finish enter done if not enter more: ")
    elif a=='students_count':
        class_name=input('enter your class name: ')
        print(students_count(class_name))
        b=input("if you are finish enter done if not enter more: ")
if b=='done':
    print('finish')
