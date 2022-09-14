def write():
    write_fh=open("abc.txt",'w')
    x=str(input("Enter a string: "))
    write_fh.write(x+"\n")
    write_fh.close()
    print("Done")

def append():
    append_fh=open("abc.txt",'a')
    x=str(input("Enter a string: "))
    append_fh.write(x+"\n")
    append_fh.close()
    print("Done")

def read():
    read_fh=open("abc.txt",'r')
    x=read_fh.read()
    read_fh.close()
    print(x)

#list=["Computer Science","Physics","Chemistry","Maths"]
#for i in range(3):
#    myfile.write(list[i]+"\n")
#    print(i)
#myfile.close()
