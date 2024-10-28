"""
CS3080 Project - Task 1
This program will scrape a website,
https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/, for the top 1000
English words. The program will take these words and put them into an Excel sheet. This Excel
sheet will then be used as input to create a hangman-like word game where the user has a limited
number of guesses to guess each letter in the random word out of the Excel sheet.
"""
import requests, bs4, openpyxl, random

file = "Test.xlsx"

# select_word function to randomly select a word from an Excel file
def select_word(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet 1']

    word = [cell.value for cell in sheet['A'] if cell.value is not None]

    selected_word = random.choice(word)
    return selected_word

print(select_word(file))

#def main():

#if __name__ == "__main__":
    #main()