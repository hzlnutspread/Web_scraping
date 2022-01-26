from bs4 import BeautifulSoup

with open('test_scraper.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.find_all('div', class_='card')  # finds all div tags and the class related to the divs
    for course in course_cards:
        course_name = course.h5.text  # .text gives only the text within the tags
        course_price = course.a.text.split()[-1]  # this takes the last element in the string

        print(f'{course_name} costs: {course_price}')

    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)
