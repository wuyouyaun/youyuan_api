import requests


def register(s, username="test335",
             password="123456",
             mail="test335@qq.com"):
    '''注册'''
    # s = requests.session()
    url = "http://49.235.92.12:6009/api/v1/register"

    body = {
        "username": username,
        "password": password,
        "mail": mail
    }
    r = s.post(url, json=body)
    # print(r.text)
    # print(r.json())
    return r

if __name__ == '__main__':
    s = requests.session()
    r = register(s)
    print(r.json())

