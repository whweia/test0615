# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:55
# @Author:whweia
# @File:test_login.py

import unittest
from interface.school import School
import requests
s = requests.session()


class TestLogin(unittest.TestCase):
    def setUp(self):                   # 前置条件
        self.l = School(s)

    # 账号密码正确
    def test_login_success(self):
        r = self.l.login('admin', '660B8D2D5359FF6F94F8D3345698F88C')
        self.assertIn('退出登录', r.text)

    # 账号为空，密码正确
    def test_login_username_null(self):
        r = self.l.login('', '660B8D2D5359FF6F94F8D3345698F88C')
        self.assertNotIn('退出登录', r.text)

    # 账号正确，密码为空
    def test_login_pwd_null(self):
        r = self.l.login('admin', '')
        self.assertNotIn('退出登录', r.text)

    # 账号密码都为空
    def test_login_null(self):
        r = self.l.login('', '')
        self.assertNotIn('退出登录', r.text)

    # 账号错误，密码正确
    def test_login_username_false(self):
        r = self.l.login('admin1', '660B8D2D5359FF6F94F8D3345698F88C')
        self.assertNotIn('退出登录', r.text)

    # 账号正确，密码错误
    def test_login_pwd_false(self):
        r = self.l.login('admin', '660B8D2D5359FF6F94F8D3345698F88C1')
        self.assertNotIn('退出登录', r.text)


# 调试
if __name__ == '__main__':
    unittest.main()