queue=[]
r=-1
f=-1
n=len(queue)

def main():
    op=int(input('>  '))
    if op==0:
        exit()
    elif op==1:
        push()
        main()
    elif op==2:
        pop()
        main()
    elif op==3:
        help_menu()
        main()

def help_menu():
    print('''What operation would you like to perform?
[0] Quit
[1] Push
[2] Pop
[3] Display Help''')

def push():
    global r
    global f
    global n
    item=input("Enter item: ")
    if r>n:
        print("Overflow")
    else:
        r=r+1
        f=0
    queue.insert(r,item)
    print(queue)

def pop():
    global r
    global f
    global n
    if f==-1:
        print("Underflow")
    else:
        queue.pop(f)
        r=r-1
        print(queue)

help_menu()
main()
