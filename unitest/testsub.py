from calculator import Count
import  unittest

class testSub(unittest.TestCase):
    def setUp(self):
        print("开始减法测试")

    def tearDown(self):
        print("减法测试结束")

    def test_sub(self):
         j=Count(10,8)
         self.assertEquals(j.testsub(), 2)
         print("两个数相减测试通过")

if __name__ == "__main__":
    unittest.main()