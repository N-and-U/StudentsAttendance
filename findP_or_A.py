import csv
def find(srow,attendencefile):
    temp = int(srow['Regno']) % 100000
    t = 1
    attfile = open(attendencefile, 'r')
    attreader = csv.DictReader(attfile)
    for arow in attreader:
        t = int(arow['Regno'])
        if t == temp:
            t = 1
            break
        else:
            t = 0
    attfile.close()
    return t