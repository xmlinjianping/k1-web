from calculator import  Count
import unittest

class testAdd(unittest.TestCase):
     def setUp(self):
         print("开始加法测试")

     def tearDown(self):
         print("加法测试结束")

     #跳过某个测试用例，也可以加在类上面，跳过整个类
     @unittest.skipIf(1>2,"当条件为真是执行测试用例")
     def test_add(self):
         j=Count(2,3)
         self.assertEquals(j.testcount(), 5)
         print("两个数相加之和测试通过")

if __name__ == "__main__":
    unittest.main()