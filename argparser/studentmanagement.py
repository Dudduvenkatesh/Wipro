import os
from datetime import datetime
FILE='student.txt'
LOG_FILE="log.txt"

def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def add_students():
    sid=input("Enter student id:")
    sname=input("Enter student name:")
    course=input("Enter a course:")
    with open(FILE,'a') as f:
        f.write(f"{sid},{sname},{course}\n")
    print("Student details added successfully!")
    write_log(f"ADD: {sid},{sname},{course}")


def view_students():
    if not os.path.exists(FILE):
        print("No student records found!")
        write_log("VIEW FAILED: student.txt not found")
        return

    with open(FILE,"r") as f:
        data=f.read()
        print("\n== All employees===")
        print(data)
    write_log("VIEW: Displayed all students")

def search_student():
    sid=input("enter stduent ID to search:")
    if not os.path.exists(FILE):
        print("No data found")
        write_log("SEARCH FAILED: File missing")

        return
    with open(FILE,"r") as f:
        for line in f:
            if line.startswith(sid+","):
                print("Record found:",line)
                write_log(f"SEARCH SUCCESS: {sid}")
                return 
    print("Student not found")
    write_log(f"SEARCH FAILED: {sid}")
 


def delete_student():
        sid = input("Enter student ID to delete: ")
 
        if not os.path.exists(FILE):
            print("No data found!")
            write_log("DELETE FAILED: File missing")
            return
 
        with open(FILE, "r") as f:
            lines = f.readlines()
 
        found = False
 
        with open(FILE, "w") as f:
            for line in lines:
                if line.startswith(sid + ","):
                    found = True
                    continue
                f.write(line)
 
        if found:
            print("student deleted successfully!")
            write_log(f"DELETE SUCCESS: {sid}")
        else:
            print("student ID not found. No records deleted.")
            write_log(f"DELETE FAILED: {sid} not found")



def menu():
    while True:
        print("\n==== Student Management ====")
        print("1. Add Student")
        print("2. View All students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
 
        choice = input("Enter choice: ")
 
        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        else:
            write_log("PROGRAM EXITED")
            break
 
menu()