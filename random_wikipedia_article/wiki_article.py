import webbrowser
import requests
import bs4

wikipedia_random_address = 'https://en.wikipedia.org/wiki/Special:Random'


def get_wiki_page():
    response = requests.get(wikipedia_random_address)
    html = bs4.BeautifulSoup(response.text, 'lxml')

    return html.title.text, response.url


def main():
    while True:
        (page_title, page_url) = get_wiki_page()
        read = input(f'Would you like to read about {page_title}?')

        if read == 'y' or read == 'Y':
            webbrowser.open(page_url)

        ans = input('Another article?[Y/N]')
        if ans == 'y' or ans == 'Y':
            print('Getting the next article...')
        elif ans == 'n' or ans == 'n':
            print('Bye!')
            break
        else:
            print('Kernel Panic!')
            break


if __name__ == '__main__':
    main()
