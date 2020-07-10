import requests


def check_success(url):
    r = requests.get(url)
    return "Success" if r.status_code == 200 else "Fail"