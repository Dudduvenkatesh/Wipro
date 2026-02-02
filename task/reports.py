def generate(name, marks_list, total, percentage, grade):
    print("\n-------- STUDENT REPORT --------")
    print("Name:", name)
    print("Marks:", marks_list)
    print("Total Marks:", total)
    print("Percentage:", format(percentage, ".2f") + "%")
    print("Grade:", grade)
    print("--------------------------------")
