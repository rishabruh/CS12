stack=[]
top=-1
n=len(stack)

def main():
    while True:
        op=int(input('>  '))
        if op==0:
            exit()
        elif op==1:
            push()
        elif op==2:
            pop()
        elif op==3:
            print(f'The Stack has {n} items. Currently on index {n-1}')
        elif op==4:
            help_menu()

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
