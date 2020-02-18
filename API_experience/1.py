# https://wikipedia.readthedocs.io/en/latest/quickstart.html
# Given some initial subject from the user, the program searches through all of the available pages about it
# The user chooses one and the program then makes a WikipediaPage object out of it, and gives back the first 7 links in the text
# The user chooses one of them, and the previous step is repeated until the player has reached the wikipedia page for Python (or any other pre-chosen page)
# If the user manages to get to the final page within 7 links from the original he/she wins.


import wikipedia


def print_links(links):
    i = 0
    for link in links:
        print(f'{i} -- {link}')
        i += 1




start_input = input('Enter: ')

search_result = wikipedia.search(start_input)
page = ''


count = 0
while count >= 7:
    if 'python' in str(page.title).lower():
        print('You won!')
        break
    else:
        print_links(search_result)
        chosen_page = int(input('Enter: '))
        page = wikipedia.page(search_result[chosen_page])
        search_result = page.links[0:7]
        count +=1
else:
    print('You lose.')


