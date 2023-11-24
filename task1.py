from csv import reader, writer

with open("students.csv") as data_file:
    stud_data = reader(data_file, delimiter=',')
    for item in stud_data:
        if "Хадаров Владимир" in item[1]:
            print(item)
    print(stud_data.line_num)
