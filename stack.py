stack=[]
top=-1
n=len(stack)

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
        print(f'The Stack has {n} items. Currently on index {n-1}')
        main()
    elif op==4:
        help_menu()
        main()

def help_menu():
    print('''What operation would you like to perform?
[0] Quit
[1] Push
[2] Pop
[3] Show Stack Size
[4] Display Help''')

def push():
    global top
    global n
    item=input("Enter item: ")
    if top>n:
        print("Overflow")
    else:
        top+=1
        stack.insert(top,item)
        n=len(stack)
        print(stack)

def pop():
    global top
    global n
    if top==-1:
        print("Underflow")
    else:
        stack.pop(top)
        top=top-1
        n=len(stack)
        print(stack)

help_menu()
main()
