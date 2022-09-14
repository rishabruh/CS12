import pickle
# student={}
# stfile=open("Student.dat",'wb')
# ans='y'
# while ans=='y':
    # rno=input("Enter roll no.: ")
    # name=input("Enter name: ")
    # marks=input("Enter marks: ")
    # student['Roll no']=rno
    # student['Name']=name
    # student['Marks']=marks
    # pickle.dump(student,stfile)
    # ans=input("Do you wish to add more records? [y/n]")
# stfile.close()


student = {}
# try:
# check_fh = open("Student.dat", "rb")
# except FileNotFoundError:
    # write_fh = open("Student.dat", "wb")
    # ans = "y"
    # while ans == "y":
        # rno = input("Enter roll no.: ")
        # name = input("Enter name: ")
        # marks = input("Enter marks: ")
        # student["Roll no"] = rno
        # student["Name"] = name
        # student["Marks"] = marks
        # pickle.dump(student, write_fh)
        # ans = input("Do you wish to write more records? [y/n]")
    # write_fh.close()
# else:
append_fh = open("temp.dat", "ab")
ans="y"
while ans=="y":
    rno = input("Enter roll no.: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    student["Roll no"] = rno
    student["Name"] = name
    student["Marks"] = marks
    pickle.dump(student, append_fh)
    ans = input("Do you wish to append more records? [y/n]")
append_fh.close()
