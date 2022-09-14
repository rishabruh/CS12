import pickle
student={}
found=0
trycode=1
search_fh=open("Student.dat","rb")
ask=1
searchkey=[]
while ask==1:
    askkey=input("Enter search keys\n:")
    searchkey=[askkey]
    ask=0
#    confirm=input("Do you want to enter more search keys?")
try:
    while trycode==1:
        student=pickle.load(search_fh)
        if student['Roll no'] in searchkey:
            print(student)
            found=1
except EOFError:
    if found==1:
        print("Search Complete")
    else:
        print("Not found")
search_fh.close()
