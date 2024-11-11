"""
CS3080 Python - Project 1 - Task 2
This program will scrape three websites, https://openaccess.thecvf.com/CVPR2022?day=all,
https://openaccess.thecvf.com/CVPR2023?day=all, and https://openaccess.thecvf.com/CVPR2024?day=all,
and obtain the top three contributors (authors or researchers) in a conference for the last three years.
(2022, 2023, and 2024). The results will be saved into an Excel spreadsheet that shows how many times each
author contributed to a paper separated by the year.
"""
import openpyxl
from numpy.core.defchararray import center
from openpyxl.styles import Alignment, Font
import bs4
import requests



dict2022 = dict({'bill': 2, "jill": 3, "frank": 1})
dict2023 = dict({'bill': 8, "jill": 7, "frank": 9, "hank": 10})
dict2024 = dict({'bill': 8, "jill": 7, "frank": 9, "mary": 10})

# Counts Totals of all lists
def count_totals(dict1, dict2, dict3):
    the_total = {}

    def add_totals(key, values):

        if key in the_total:
            the_total[key][0].append(values)
            the_total[key][1] += values
        else:
            the_total[key] = [[values], values]

    for dict_in in [dict1, dict2, dict3]:
        for key, value in dict_in.items():
            add_totals(key, value)

    sorted_list = sorted_list = sorted([(key, values[0], values[1])
                                        for key, values in the_total.items()], key=lambda x: x[2], reverse=True)

    return sorted_list



final_count = count_totals(dict2022, dict2023, dict2024)


# Sorts and reverses A list's values from highest to lowest
def sort_and_reverse(mylist):
    first = len(mylist)
    for i in range(0, first):
        for j in range(0, first - i - 1):
            if mylist[j][2] < mylist[j+1][2]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist


#final_count = sort_and_reverse(final_count)
print(final_count)
'''
list_1 = sort_and_reverse((list(test_dict1.items())))
list_2 = sort_and_reverse(list(test_dict2.items()))
list_3 = sort_and_reverse(list(test_dict3.items()))

print(list_1)
print(list_2)
print(list_3)
print(final_count)

def create_sheet(aList, list2022, list2023, list2024):
    top_con = openpyxl.Workbook()
    print(top_con.sheetnames)
    sheet = top_con.active
    sheet.title = "CVF Top 3 Contributors"
    print(top_con.sheetnames)

    # Add years and total to sheet
    start_year = 2022
    for i in range(4):
        if i < 3:
            cell2022 = sheet.cell(row=i+2,column=1, value = start_year + i )
            cell2022.font = Font(bold=True)
            cell2022.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell2022 = sheet.cell(row=i+2, column=1, value = "Total")
            cell2022.font = Font(bold=True)
            cell2022.alignment = Alignment(horizontal="center")


    # Add names
    for i in range(3):
        cell = sheet.cell(row= 1, column = i+2, value = aList[i][0])
        cell.alignment = Alignment(horizontal="center", vertical="center")

    #Add year 2022 values to sheet
    for i in range(3):
        cell2 = sheet.cell(row=2, column=i+2, value= list2022[i][1])
        cell2.alignment = Alignment(horizontal="center", vertical="center")

    top_con.save('Task2.xlsx')

create_sheet(final_count, list_1, test_dict2, test_dict3)
'''