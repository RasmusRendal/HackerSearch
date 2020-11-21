import requests
import csv
import io
import os

so_list = None
so_list_location = "/tmp/solist.txt"

def load_list():
    so_list = []
    if not os.path.isfile(so_list_location):
        return None
    with open(so_list_location, "r") as f:
        for line in f.readlines():
            so_list.append(clean_keyword(line))
    assert len(so_list) > 10
    return so_list


def save_list(so_list):
    with open(so_list_location, "w") as f:
        for word in so_list:
            f.write(word + "\n")


def clean_keyword(keyword):
    return keyword.replace(chr(10), '')

def fetchlist():
    r = requests.get("https://data.stackexchange.com/stackoverflow/csv/490877")
    reader = csv.reader(r.text.split("\n"))
    so_list = []
    for row in reader:
        keyword = row[0]
        keyword = keyword[:-1]
        keyword = clean_keyword(keyword)
        so_list.append(keyword)
    save_list(so_list)
    return so_list


def get_so_list():
    global so_list
    if so_list != None:
        return so_list
    so_list = load_list()
    if so_list != None:
        return so_list
    return fetchlist()


def is_keyword(word):
    li = get_so_list()
    return word in get_so_list()
