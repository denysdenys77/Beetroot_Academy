import wikipedia


def print_links(links):
    i = 0
    for link in links:
        print(f'{i} -- {link}')
        i += 1


def recursive_search(search_link, search_set=None, i=0):
    if i == 0:
        search_result = wikipedia.search(search_link)
        print_links(search_result)
        chosen_page = int(input('Enter: '))
        recursive_search(chosen_page, search_result, i+1)
    elif i < 7:
        page = wikipedia.page(search_set[search_link])
        search_result = page.links[0:7]
        print_links(search_result)
        chosen_page = int(input('Enter: '))
        recursive_search(chosen_page, search_result, i+1)
    else:
        print('You lose.')
        return



start_input = input('Enter: ')
recursive_search(start_input)
