queue=[]
r=-1
f=0
n=len(queue)

def help_menu():
    print('''What operation would you like to perform?
[0] Quit
[1] Push
[2] Pop
[3] Display Help''')

def push():
    global r, f, n
    n=len(queue)
    item=input("Enter item: ")
    if r>n:
        print("Overflow")
    else:
        r+=1
        f=0
    queue.insert(r,item)
    print(queue)

def pop():
    global r, f, n
    n=len(queue)
    if r==-1:
        print("Underflow")
    else:
        queue.pop(f)
        r-=1
        print(queue)

help_menu()
while True:
    op=int(input('>  '))
    if op==0:
        exit()
    elif op==1:
        push()
    elif op==2:
        pop()
    elif op==3:
