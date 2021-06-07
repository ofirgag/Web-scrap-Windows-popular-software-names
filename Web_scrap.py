from urllib.request import urlopen
from bs4 import BeautifulSoup

dict_of_common_software = {}

def scrap():
    for i in range(1, 20387):
        url = "https://download.cnet.com/s/software/{}/?platform=windows&sort=most-popular&page=%7B%7D".format(i)
        html = urlopen(url)
        print(list(dict_of_common_software.keys()))
        soup = BeautifulSoup(html, 'lxml')
        for tag in soup.find_all('h3',
                                 class_="c-productCard_title g-text-large g-text-bold g-outer-spacing-bottom-xsmall"):
            dict_of_common_software[tag.string] = 1


def create_file(dictionary):
    file = open('dict_of_common_software.txt', 'w+')
    for k in dictionary.keys():
        file.write(k + '\n')
    file.close()


if __name__ == '__main__':
    scrap()
    create_file(dict_of_common_software)
