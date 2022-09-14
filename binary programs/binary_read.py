import pickle
f1=open("temp.dat","rb")
str={}
y="true"
try:
    while y=="true" :
        str=pickle.load(f1)
        print(str)
except EOFError:
    f1.close()
