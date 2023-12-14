# test_app.py

import unittest
from app import app


class BasicTests(unittest.TestCase):

    # 在测试前执行的设置
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # 测试首页是否返回状态码 200
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # 测试 "关于我们" 页面是否返回状态码 200
    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
