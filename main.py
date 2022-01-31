from UpdateTodaysAttendance import UpdateAttendence
from AddNewSectionAttendance import newSection
import os

if __name__ == '__main__':
    print("Note:")
    print("Fields Names of Student file should be sno,Regno,Name")
    print("and Attendance file should be Regno\n")
    diname = True
    for f in os.listdir():
        if f == "sections":
            diname = True
            break
        else:
            diname = False
    if not diname:
        os.mkdir("sections")
    while True:
        choice = int(input("1.AddNewSection\n2.UpdateToday's Attendance\n3.Exit\n"))
        if choice == 1:
            newSection()
        elif choice == 2:
            UpdateAttendence()
        elif choice == 3:
            print("...THANKS YOU...")
            break
        else:
            print("Wrong choice...!")
            print("Try Again\n\n")