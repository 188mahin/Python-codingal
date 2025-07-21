student_names=[]
student_marks=[]
student_medals=[]
for i in range(10):
    name=input("enter name of the student:")
    marks=int(input("enter the amount of marks that student has scored:"))
    student_names.append(name)
    student_marks.append(marks)
avg=int(sum(student_marks)/10)
avgL=[avg,avg,avg,avg,avg,avg,avg,avg,avg,avg]
for i in student_marks:
    if i>=80:
        student_medals.append("gold medal")
    elif i<80 and i>=50:
        student_medals.append("silver medal")
    elif i<50 and i>=40:
        student_medals.append("bronze medal")
    elif i<40:
        student_medals.append("participation certificate")
    else:
        print("invalid input")
print(list(zip(student_names,
               student_marks,
               student_medals,
               avg)))

    
#print student name,average score,marks,medal
#zip method
