# Nicholas Sylvester
# CS3080 Python Programming
# Task 1

""" Task 1 - Simple Word Game.
This program will scrape a website, 
https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/, for the top 1000 English words. 
The program will take these words and put them into an excel sheet. 
This excel sheet will then be used as input to create a hangman-like word game where the 
user has a limited number of guesses to guess each letter in the random word out of the excel sheet.

"""

import requests, bs4, openpyxl, os

class Game():
    def select_word():
        pass

    def display_word():
        pass


def get_words():
    response = requests.get('https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/')
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div = soup.find('div', {'class': 'field-item even'})

    paragraphs = div.find_all('p')

    words = paragraphs[1].text
    words = words.split()

    return words


def create_sheet(words):
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    for row, word in enumerate(words, start=1):
        sheet.cell(row, 1, word)
    
    wb.save('Task1.xlsx')
        
        
def main_game():
    pass


def main():
    print(os.getcwd())
    word_bank = get_words()
    create_sheet(word_bank)


if __name__ == "__main__":
    main()