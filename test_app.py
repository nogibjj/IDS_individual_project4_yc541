# test_app.py

import unittest
from app import app


class BasicTests(unittest.TestCase):

    # 在测试前执行的设置
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # test 200
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
