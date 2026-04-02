#MUHAMMAD SYAHDIQ ASYRAF BIN TIPILIL @ RAPAHIL
#C02
#LAB TEST 3: IMPORTING CSV FILE, CALCULATING THE AVERAGE 
#AND APPENDING NEW DATA

#IMPORTING CSV
import csv

#FIRST FUNCTION (READ FILE AND CALCULATE AVERAGE)
def read_file(file):

    filename = open(file, "r")
    reader = csv.reader(filename)
    next(reader)
    count = 0
    total = 0

    for row in reader:
        print(row)

        total = total + float(row[1])
        count += 1
    
    avg = total / count
    print("Height Average", avg)
    filename.close()

#SECOND FUNCTION (APPENDING NEW DATA)
def add_file(file):
    gender = input("Enter gender :")
    height = input("Enter height :")
    weight = input("Enter weight :")
    bmi = input("Enter bmi :")

    filename = open(file, "a", newline="")
    writer = csv.writer(filename)

    writer.writerow([gender,height,weight,bmi])

    filename.close()

    print("/nUpdated Files:")

    filename = open(file, "r")
    reader = csv.reader(filename)

    for row in reader:
        print(row)

    filename.close()

    

read_file("bmi.csv")
add_file("bmi.csv")