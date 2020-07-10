import re
import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
init()


def get_tab_id(name_of_site: str):
    tab_id = name_of_site
    if name_of_site.startswith("http"):
        tab_id = name_of_site[8:]

    tab_id = re.sub(r"(.*)\.\w+", r"\1", tab_id)
    return tab_id


def save_to_file(name_of_site, site_text):
    name_of_file = name_dir + "\\" + name_of_site
    my_tabs[name_of_site] = name_of_file
    with open(name_of_file, "w", encoding='utf-8') as f:
        f.write(site_text)


def read_site_from_file(inp):
    with open(my_tabs[inp]) as f:
        print(f.read())


d = deque([])
my_tabs = {}
list_tags = ["title", "p", "a", "ul", "ol", "li"]
name_dir = os.getcwd() + "\\" + sys.argv[1]
if not os.path.exists(name_dir):
    os.mkdir(name_dir)


while True:
    user_inp = input()
    back = False

    if user_inp == "back":
        back = True
        if len(d) < 2:
            continue
        else:
            d.pop()
            user_inp = d.pop()
    elif user_inp == "exit":
        break

    tab_name = get_tab_id(user_inp)

    if tab_name in my_tabs:
        read_site_from_file(tab_name)
        if not back:
            d.append(tab_name)
    else:
        if not user_inp.startswith("http"):
            user_inp = f"https://{user_inp}"

        try:
            r = requests.get(user_inp)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                text_tags = []

                for tag in soup.find_all(list_tags, text=True):
                    tag_text = tag.text.strip()
                    if tag.name == "a":
                        print(Fore.BLUE + tag_text)
                    else:
                        print(Fore.BLUE + tag_text)
                    text_tags.append(tag_text)
                res_text = "\n".join(text_tags)

                print(res_text)
                save_to_file(tab_name, res_text)
        except requests.exceptions.ConnectionError:
            print("Error: Incorrect URL")
