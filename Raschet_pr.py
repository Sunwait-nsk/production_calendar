import datetime


def day_theory_func(theory: int) -> int:
    if theory % 8 == 0:
        result = theory // 8
    else:
        result = theory // 8 + 1
    return result


result = []
with open("pr_cal.txt", 'r') as name:
    text = name.read()
i = text.find('2022 = ')
result = text[i + 8: len(text)-1]
result_list = result.split("', '")
day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
date1 = input("дата начала!!! в виде: 04.04.2022: ")
date2 = []
pr_date1 = date1.split('.')
#date2.append(('.'.join([pr_date1[2], pr_date1[1], pr_date1[0]])))
date_t = ''
h_total = int(input('общее количество часов: '))
t = 8
theory = int(input('количество часов теории: '))
day_theory = day_theory_func(theory)
consultation = int(input('количество часов консультации: '))
ekzamen = int(input('количество часов экзамена: '))
day, month, year = date1.split('.')
print("Производится расчет календаря. Ждите...")
ind_1 = result_list.index(('.'.join([pr_date1[2], pr_date1[1], pr_date1[0]])))
i = 0
date2.append(result_list[ind_1])
date_p = ''
while t < h_total:
    i += 1
    t += 8
    date2.append(result_list[ind_1 + i])
    if t >= theory and date_p == '':
        date_t = result_list[ind_1 + i - 1]
        date_p = result_list[ind_1 + i]
        print("начало практики {}".format(date_p))
row = "theory: {}\n practic: {}\n Consult: {}\n exam: {}".format(date2[0] + '- ' + date_t,
                                                                 date_p + '- ' + date2[len(date2) - 3],
                                                                 date2[len(date2) - 2],
                                                                 date2[len(date2) - 1])
print(row)