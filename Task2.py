# Nicholas Sylvester
# CS3080 Python Programming
# Task 2

import requests
import bs4
import openpyxl

LINK_2022 = r'https://openaccess.thecvf.com/CVPR2022?day=all'
LINK_2023 = r'https://openaccess.thecvf.com/CVPR2023?day=all'
LINK_2024 = r'https://openaccess.thecvf.com/CVPR2024?day=all'

def find_contributors(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
    except Exception as e:
        # If requests can not connect to the link, display error and quit program
        print(f"ERROR: {e}\nCheck Internet Connection")
        quit()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div = soup.find('div', {'id' : 'content'})

    authors = list(div.select('input[type=hidden]'))

    author_counts = {}

    for element in authors:
        value = element.get("value")

        if value in author_counts:
            author_counts[value] += 1
        else:
            author_counts[value] = 1

    return author_counts



def main():
  contributors_2022 = find_contributors(LINK_2022)
  contributors_2023 = find_contributors(LINK_2023)
  contributors_2024 = find_contributors(LINK_2024)

  print(contributors_2022)
  print(contributors_2023)
  print(contributors_2024)



if __name__ == "__main__":
    main()