# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:55
# @Author:whweia
# @File:test_add.py

import unittest
import requests
s = requests.session()
import random
from interface.school import School
name = random.randint(110000,10000000)
# print(name)


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.l = School(s)
        self.l.login('admin','660B8D2D5359FF6F94F8D3345698F88C')

    def test_add_success(self):
        r = self.l.add(name,'1','0','test')
        self.assertIn('学校创建成功', r.text)

    def test_add(self):
        r = self.l.add(name, '2', '0', '')
        self.assertIn('学校创建成功', r.text)

    # def test_add_remark_null(self):
    #     r = self.l.add(name,'2','0','')
    #     self.assertIn('学校创建成功', r.text)

    # def test_add_name_null(self):
    #     r = self.l.add('','2','0','test')
    #     self.assertNotIn('学校创建成功', r.text)


if __name__ == '__main__':
    unittest.main()
