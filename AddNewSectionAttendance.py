import csv
import datetime
import os
from findP_or_A import find
from findfile import checkfile
def newSection():
    sectionfile = input("Enter Section Number:")
    filext = sectionfile +".csv"
    for f in os.listdir("sections"):
        if filext == f:
            print("\nThis section file Already exit...! \n")
            return
    sectionfile = "sections/" + sectionfile +".csv"
    studentfile = input("Enter Student File(with .csv) Name:")
    attendencefile = input("Enter Todays Attendance File(with .csv) Name:")
    s= checkfile(studentfile)
    a = checkfile(attendencefile)
    if s == False or a == False:
        print("\nFiles are not found...!")
        print("Added files and try again...!\n")
        return
    stufile = open(studentfile, 'r')
    stureader = csv.DictReader(stufile)
    tday = datetime.date.today()
    final = []
    sno = 1
    for srow in stureader:
        t = find(srow,attendencefile)
        if t == 1:
            dis = {"Sno":sno,"Regno": srow['Regno'], "Name": srow['Name'], tday: "p"}
            final.append(dis)
            sno +=1
        else:
            dis = {"Sno":sno,"Regno": srow['Regno'], "Name": srow['Name'], tday: "A"}
            final.append(dis)
            sno += 1

    fields = ["Sno","Regno", "Name", tday]

    with open(sectionfile, 'w') as newfile:
        writer = csv.DictWriter(newfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(final)
        newfile.close()
    stufile.close()
    os.remove(studentfile)
    os.remove(attendencefile)
    print("\nAdded New section and Updated Today's Attendance successfully...\n")
    return

# newSection()
