#coding = utf-8
from selenium import webdriver
import  unittest
import time
import random
from login import login

class Beditplayer(unittest.TestCase):
    """编辑球员"""

    def setUp(self):
        self.driver = login()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_Beditplayer(self):
        """编辑球员"""
        driver = self.driver
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-navbar/div/nav/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-player/div/app-player-list/div/table/tbody/tr[1]/td[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//img[@class='edit-icon'][@alt='编辑']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='name'][@name='name']").clear()
        driver.find_element_by_xpath("//input[@id='name'][@name='name']").send_keys("编辑球员姓名")
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='player-adder']/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[contains(text(),'球员')] [@class='active']").click()
        #断言,判断是否有姓名是：编辑球员姓名的球员
        name = driver.find_element_by_xpath("//td[contains(text(),'编辑球员姓名')]").text
        print(name)
        self.assertEqual("编辑球员姓名",name)


#unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#if __name__ == "__main__":
#    unittest.main()