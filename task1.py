'''
Решение задачи 1 практической части предпрофессионального экзамена

Переменные:
    stud_data - список значений из исходного файла
    class_statistic - словарь по классам, содержащий количество человек
    в классе и суммарный балл.
    stud_data_new - новый список со средними значениями балла по классу
'''
from csv import reader, writer

with open("students.csv") as data_file:
    stud_data = list(reader(data_file, delimiter=','))

for item in stud_data:
    if "Хадаров Владимир" in item[1]:
        print(f"Ты получил: {item[4]}, за проект - {item[2]}")

class_statistic = dict()
header_string = stud_data.pop(0)
for id, name, pr_id, school_class, score in stud_data:
    if score != 'None':
        if school_class not in class_statistic.keys():
            class_statistic[school_class] = [0, 0]
        class_statistic[school_class][0] += 1
        class_statistic[school_class][1] += int(score)

stud_data_new = []
for id, name, pr_id, school_class, score in stud_data:
    if score != 'None':
        score = class_statistic[school_class][1] / class_statistic[school_class][0]
        score = str(round(score, 3))
        stud_data_new.append([id, name, pr_id, school_class, score])

with open('students_new.csv', 'w') as data_file:
    file_data = writer(data_file, delimiter=',')
    file_data.writerows(stud_data_new)


