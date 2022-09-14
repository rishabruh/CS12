import pickle
student={}
found=0
f1=open("Student.dat","rb")
askmarks=int(input("Enter the marks threshold: "))
try:
    while found==0:
        student=pickle.load(f1)
        if int(student["Marks"]) >askmarks:
            print(student)
            found=1
except EOFError:
    if found==1:
        print("Search Complete")
    else:
        print("Not found")
f1.close()
