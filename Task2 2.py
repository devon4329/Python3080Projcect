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
from openpyxl.styles import Alignment
import bs4
import requests



test_dict1 = dict({'bill': 2, "jill": 3, "frank": 1})
test_dict2 = dict({'bill': 8, "jill": 7, "frank": 9, "hank": 10})
test_dict3 = dict({'bill': 8, "jill": 7, "frank": 9, "mary": 10})



def count_totals(dict1, dict2, dict3):
    the_total = {}
    for key, values in dict1.items():
        if key in the_total:
            the_total[key] += values
        else:
            the_total[key] = values
    for key, values in dict2.items():
        if key in the_total:
            the_total[key] += values
        else:
            the_total[key] = values
    for key, values in dict3.items():
        if key in the_total:
            the_total[key] += values
        else:
            the_total[key] = values

    return list(the_total.items())

final_count = count_totals(test_dict1, test_dict2, test_dict3)

def sort_and_reverse(mylist):
    first = len(mylist)
    for i in range(0, first):
        for j in range(0, first - i - 1):
            if mylist[j][1] < mylist[j+1][1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp

    return mylist

print(sort_and_reverse(final_count))

def create_sheet(aList):
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
            cell2022.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell2022 = sheet.cell(row=i+2, column=1, value = "Total")
            cell2022.alignment = Alignment(horizontal="center")


    # Add names to sheet
    for i in range(3):
        cell = sheet.cell(row= 1, column = i+2, value = aList[i][0])
        cell.alignment = Alignment(horizontal="center", vertical="center")
    for i in range(3):
        cell2 = sheet.cell(row=2, column=i+2, value= aList[i][1])
        cell2.alignment = Alignment(horizontal="center", vertical="center")

    top_con.save('Task2.xlsx')

create_sheet(final_count)
