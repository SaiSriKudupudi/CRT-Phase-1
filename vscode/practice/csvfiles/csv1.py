import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentId","rollno","name","mobileno"])
studentid=int(input("enter studentid:"))
rollno=int(input("enter rollno:"))
name=input("enter name:")
mobileno=int(input("enter mobileno:"))
a.writerow([studentid,rollno,name,mobileno])
