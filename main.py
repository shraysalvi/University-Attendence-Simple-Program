iid = "1234"
pas = "@1234"


def file_open():
    file = "Student_list"
    a = open(f'{file}.csv', 'r')
    x = a.readlines()
    a.close()
    all_student = [_.split() for _ in x]
    x_student = []
    for _ in all_student:
        x_student.append([__.split(',') for __ in _])
    return [_[0] for _ in x_student]


def id_pas():
    new_id = input("ENTER NEW ID: ")
    new_pas = input("ENTER NEW PASSWORD: ")
    global iid
    iid = new_id
    global pas
    pas = new_pas


def new_student():
    a = 1
    while a == 1:
        new_roll = input("Enter ROLL NUMBER: ")
        new_name = input("Enter NAME in Capital letter: ")
        new_sur = input("Enter SURNAME in Capital letter: ")
        if new_roll.isdigit() and new_name.isupper() and new_sur.isupper():
            return str(new_roll).strip()+"-"+new_name.strip()+"-"+new_sur.strip()
        else:
            print("Enter ROLL NUMBER as a number and Name and Surname in Capital Letter")


def doing(std):
    print("Add Student in Class: 1")
    print("Delete Student from Student List: 2")
    i = int(input('>>'))
    if i == 1:
        std.append([new_student()])
        print(f"Student Added Successfully")
        return std
    if i == 2:
        out_student = new_student()
        for _ in std:
            if out_student == _[0]:
                std.remove(_)
                print(f"{_[0]} Deleted Successfully")
                break
        else:
            print("No Student with this name and roll number\n")
        return std


def check():
    a = 1
    while a == 1:
        string = input(">>")
        if string in ['A', 'P', 'L', 'SUN', 'SUS']:
            a = 0
            return string
        else:
            print(10*"-"+"\nWrong choice! Again \n---------Press for Task---------\nA: Absent\nP: Present\nL: Leave\nSUN: Sunday\nSAT: Saturday\nSUS: Suspend\n"+10*"-")


def attend(n_student):
    for _ in n_student:
        print(_[0], end=":")
        _.append(check())
    return n_student


def writen(n_student):
    with open(r'Student_list.csv', 'w') as file:
        for _ in n_student:
            for __ in _:
                if len(__) > 0:
                    file.write(__ + ",")
            file.write("\n")


def search(stu):
    search_roll = input("Enter Roll number: ")
    search_name = input("Enter Name in Capital Letter: ")
    search_surname = input("Enter Surname in Capital Letter: ")
    search_student = search_roll.strip()+"-"+search_name.strip()+"-"+search_surname.strip()
    for _ in stu:
        if search_student == _[0]:
            print(f"{search_name, search_surname} founded \nEnter date to check {search_student} coming or not:")
            date = int(input())
            if _[date] == "P":
                print(f"Student {search_student} was Present on date {date}")
                break
            elif _[date] == "A":
                print(f"Student {search_student} was Absent on date {date}")
                break
            elif _[date] == "SUS":
                print(f"Student {search_student} was Suspended on date {date}")
                break
            elif _[date] == "SUN":
                print(f"SUNDAY on date {date}")
                break
            elif _[date] == "L":
                print(f"Student {search_student} on Leave that day({date})")
                break
    else:
        print("\nWRONG ROLL or NAME or SURNAME")


def search_all(stud):
    for _ in stud:
        for __ in _:
            print(__, end=", ")
        print()


print("Enter Your ID and Password to Access Ahead")
_id = input("ID: ")
_pas = input("PASSWORD: ")
run = 1
if _id == iid and _pas == pas:
    while run == 1:
        print("*"*10+"\nPress Button for\n\nSetting: 1")
        print("Student Attendance: 2")
        print("Exit: 0")
        _student = file_open()
        choice = int(input(">>"))
        if choice == 1:
            _student = doing(_student)
            writen(_student)
            input()
        elif choice == 2:
            print("Press Button for\n\nAttendance: 1\nDetails: 2")
            achoice = int(input(">>"))
            if achoice == 1:
                _student = attend(_student)
                writen(_student)
                input()
            elif achoice == 2:
                _student = file_open()
                print("Press Button for\n\nSearch Student and see particular detail of the day: 1\nDetails of all student of all day till now!: 2")
                _choice = int(input(">>"))
                if _choice == 1:
                    search(_student)
                    input()
                elif _choice == 2:
                    search_all(_student)
                    input()
                else:
                    print("! Error")
        else:
            run = 0
else:
    print("! Wrong ID or PASSWORD")