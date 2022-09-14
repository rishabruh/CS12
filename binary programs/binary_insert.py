import pickle
student={}
temp={}
insMain_fh = open("Student.dat", "rb")
# insTemp_fh = open("temp.dat", "wb")
searchkey = []
askkey = input("Enter search key to insert after\n:")
searchkey = [askkey]
try:
    while True:
        student = pickle.load(insMain_fh)
        if student["Roll no"] in searchkey:
            temp=student
            # print(temp)
except EOFError:
    insMain_fh.close()
