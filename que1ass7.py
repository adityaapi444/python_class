#(use of UDF )wap t0 create student marks calculator input: total no.of subs,marks of each subjectoutput: percentage and grade
def per_grade(marks):
    per=sum(marks.values())/len(marks)
    if per>=75:
        grade='A'
    elif per>=60:
        grade='B'
    elif per>=40:
        grade='C'
    else:
        grade='FAIL'
    print("percentage = ",round(per,2),"%   Grade = ",grade)
#input
m={}
roll_no=int(input("enter roll no"))
name=input("enter student name")
total_sub=int(input("enter no. of subjects"))
print("enter sub_name with their marks\nIn format>sub_name=marks")

for i in range(total_sub):
    a,b=input().split("=")
    m.update({a:float(b)})
    

per_grade(m)
