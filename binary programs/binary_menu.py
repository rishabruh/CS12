import pickle

# Defining all functions
def binaryWrite():
    student = {}
    append_fh = open("Student.dat", "ab")
    ans = "y"
    while ans == "y":
        rno = input("Enter roll no.: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        student["Roll no"] = rno
        student["Name"] = name
        student["Marks"] = marks
        pickle.dump(student, append_fh)
        ans = input("Do you wish to append more records? [y/n]")
    append_fh.close()


def binaryRead():
    read_fh = open("Student.dat", "rb")
    str = {}
    try:
        while True:
            str = pickle.load(read_fh)
            print(str)
    except EOFError:
        read_fh.close()


def binarySearch():
    student = {}
    found = 0
    search_fh = open("Student.dat", "rb")
    searchkey = []
    askkey = input("Enter roll no. to search for\n:")
    searchkey = [askkey]
    try:
        while True:
            student = pickle.load(search_fh)
            if student["Roll no"] in searchkey:
                print(student)
                found = 1
    except EOFError:
        if found == 1:
            print("Search Complete")
        else:
            print("Not found")
    search_fh.close()


def binaryNew():
    new_fh = open("Student.dat", "wb")
    student = {}
    ans = "y"
    while ans == "y":
        rno = input("Enter roll no.: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        student["Roll no"] = rno
        student["Name"] = name
        student["Marks"] = marks
        pickle.dump(student, new_fh)
        ans = input("Do you wish to add more records? [y/n]")
    new_fh.close()


def binaryInsert():
    insert_fh=open("Student.dat",'wb+')
    insert_fh.seek(0)
    record={}
    record["Roll no"]=input("Enter roll no: ")
    record["Name"]=input("Enter name: ")
    record["Marks"]=input("Enter marks: ")
    try:
        templist = []
        done = False

        while True:
            rec = pickle.load(insert_fh)
            if rec["Name"] > record["Name"] and not done:
                templist.append(record)
                done = True

            templist.append(rec)
    except EOFError:
        if not done:
            templist.append(record)
        # insert_fh.truncate(0)

        for i in templist:
            pickle.dump(i, insert_fh)

while True:
    prog = int(
        input(
            """Which program would you like to run?
    1 - Create New File
    2 - Write to file
    3 - Read
    4 - Search
    5 - Insert TODO
    6 - Modify
    Enter choice[1-5][0 to quit]:"""
        )
    )
    if prog == 0:
        exit()
    elif prog == 1:
        binaryNew()
    elif prog == 2:
        binaryWrite()
    elif prog == 3:
        binaryRead()
    elif prog == 4:
        binarySearch()
    elif prog == 5:
        binaryInsert()
    elif prog == 6:
        binaryModify()
