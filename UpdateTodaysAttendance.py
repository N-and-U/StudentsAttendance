import csv
import datetime
import os
from findP_or_A import find
from findfile import checkfile
def UpdateAttendence():
    print("....List of all sections....")
    i =0
    for f in os.listdir("sections"):
        i += 1
        print(i,end='')
        print("."+f)
    choice = int(input("\nEnter choice of Section:"))
    if choice > i or choice < 1:
        print("Wrong section choice...!\n")
        return
    allFiles = os.listdir("sections")
    sectionfilename = allFiles[choice-1]
    changepath = "sections/" + sectionfilename
    attendencefilename = input("Enter Todays Attendance File(.csv) Name:")
    c = checkfile(attendencefilename)
    if c == False:
        print("\nFile are not found...!")
        print("Added file and try again..!\n")
        return
    sectionfile = open(changepath, 'r')
    sectionreader = csv.DictReader(sectionfile)
    tday = datetime.date.today()
    r = []
    for srow in sectionreader:
        t=find(srow,attendencefilename)
        if t == 1:
            srow[tday] = "p"
            r.append(srow)
        else:
            srow[tday] = "A"
            r.append(srow)
    fields =r[0].keys()
    with open("sections/output.csv", 'w') as newfile:
        writer = csv.DictWriter(newfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(r)
        newfile.close()
    sectionfile.close()
    os.remove(changepath)
    os.rename("sections/output.csv", changepath)
    os.remove(attendencefilename)

    print("\nToday's Attendance is updated successfully...!\n")

# UpdateAttendence()