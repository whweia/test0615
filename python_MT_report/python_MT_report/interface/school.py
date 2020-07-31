# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:54
# @Author:whweia
# @File:school.py

import requests
import random
name = random.randint(110000,10000000)

class School(object):
    def __init__(self, s):
        self.s = s
        self.host = 'http://47.113.116.171:8082'

    def login(self, username, pwd):
        url = self.host + '/recruit.students/login/in'
        par = {
            'account':username,
            'pwd': pwd
        }
        r = self.s.get(url=url,params=par)
        return r

    def add(self, sname, typeid, canRecruit, remark):
        url = self.host + '/recruit.students/school/manage/addSchoolInfo'
        body = {
            'schoolName':sname,
            'listSchoolType[0].id':typeid,
            'canRecruit':canRecruit,
            'remark':remark,
        }
        r = self.s.post(url=url,data=body)
        return r


# if __name__ == '__main__':
#     s = requests.session()
#     l = School(s)
#     l.login('admin', '660B8D2D5359FF6F94F8D3345698F88C')
#     r = l.add(name,'2','0','')
#     print(r.text)
    # print(r.text)
