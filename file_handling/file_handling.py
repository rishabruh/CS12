def write_rec():
    number=int(input("How many records to enter: "))
    rec_fh=open("abc.txt","a+")
    for i in range(number):
        rno=str(input("Enter rno: "))
        name=str(input("Enter name: "))
        marks=str(input("Enter marks: "))
        rec=(f'{rno}, {name}, {marks}')
        rec_fh.write(rec+'\n')
    rec_fh.close()

def split():
    split_fh=open("abc.txt",'r')
    str=''
    while str:
        str=split_fh.readline()
    for word in str.split():
        print(word,end='#')
        print(str)
    split_fh.close()

def size():
    size_fh=open("abc.txt",'r')
    str=' '
    size=0
    totalsize=0
    while str:
        str=size_fh.read()
        totalsize+=len(str)
        size+=len(str.strip())
    print(f'Total size is {totalsize} and size after strip is {size}')

def count_vc():
    count_fh=open("abc.txt",'r')
    ch=' '
    vowels=0
    consonants=0
    while ch:
        ch=count_fh.read(1)
        if ch.upper() in ['A','E','I','O','U']:
            vowels+=1
        else:
            consonants+=1
    count_fh.close()
    print(f'{vowels} vowels and {consonants} consonants')

def write():
    write_fh=open("abc.txt",'a+')
    write_num=int(input("Enter number of lines to write: "))
    for i in range(write_num):
        x=str(input("Enter a string: "))
        write_fh.write(x+"\n")
    write_fh.close()
    print("Done")

def read():
    try:
        read_fh=open("abc.txt",'r')
        x=read_fh.read()
        read_fh.close()
        print(x)
    except:
        print("File does not exist")

def help_menu():
	print('''[0] Quit
[1] Read
[2] Write
[3] Writing records
[4] Split with #
[5] Count vowels and consonants
[6] Show file size
[7] Display help menu''')

help_menu()
while True:
    choice=int(input("> "))
    if choice==0:
        exit()
    elif choice==1:
        read()
    elif choice==2:
        write()
    elif choice==3:
        write_rec()
    elif choice==4:
        split()
    elif choice==5:
        count_vc()
    elif choice==6:
        size()
    elif choice==7:
        help_menu()
    else:
        print("Choose a valid option!")


