#coding = utf-8
from selenium import webdriver
import  unittest
import time
import random
from login import login

class Addplayer(unittest.TestCase):
    """新增球员"""

    #@classmethod
    #def setUpClass(self): #测试类的开始与结束时被执行,而setup()是测试用例开始与结束时执行，所以有几个测试用例，setup方法就会被执行几次。
    #    self.driver = login()
    #    self.driver.maximize_window()
    #    self.driver.get("https://k1-test.gengee.com/cn/#/login")

    #@classmethod
    #def tearDownClass(self):
    #   time.sleep(1)
    #   self.driver.quit()

    def setUp(self):
        self.driver = login()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    #增加球员
    def test_Aaddplayer(self):
        """新增球员"""
        driver = self.driver
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-navbar/div/nav/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button").click()
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-player/div/div/dropdown-adder/div/ul/li[1]").click()
        time.sleep(1)
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys('自动化.添 加·球员1')
        time.sleep(1)
        driver.find_element_by_id("identity").clear()
        driver.find_element_by_id("identity").send_keys(random.randint(10,10000))
        #driver.find_element_by_xpath("(//small[@id='triangle'])[4]").click()
        #driver.find_element_by_xpath("//div[@id='player-adder']/div/form/div[2]/div[2]/section/p[3]/dropdown/div/ul/li[2]").click()
        driver.find_element_by_id("height").clear()
        driver.find_element_by_id("height").send_keys("204")
        driver.find_element_by_id("weight").clear()
        driver.find_element_by_id("weight").send_keys("100")
        driver.find_element_by_xpath("//div[@id='player-adder']/div/div/button").click()
        time.sleep(2)
        #断言 判断是否包含自动化的球员
        name = driver.find_element_by_xpath("//td[contains(text(),'自动化')]").text
        print(name)
        self.assertIn("自动化",name)



#unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#if __name__ == "__main__":
#    unittest.main()