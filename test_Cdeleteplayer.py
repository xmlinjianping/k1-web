#coding = utf-8
from selenium import webdriver
import  unittest
import time
import random
from login import login
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Cdeleteplayer(unittest.TestCase):
    """删除球员"""
    def setUp(self):
        self.driver = login()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_Cdeleteplayer(self):
        """删除球员"""
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-navbar/div/nav/ul/li[2]").click()
        time.sleep(1)
        driver.find_element_by_css_selector("input[type=\"text\"]").clear()
        driver.find_element_by_css_selector("input[type=\"text\"]").send_keys(u"编辑球员姓名")
        time.sleep(1)
        driver.find_element_by_css_selector("input[type=\"text\"]").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='player']/div/button").click() #点击删除球员
        driver.find_element_by_xpath("/html/body/app-root/app-home/div/app-player/div/app-player-list/div/table/thead/tr/th[1]/checkbox/label/span[1]/span").click() #点击单选
        time.sleep(1)
        driver.find_element_by_xpath("//button[1] [@class='btn btn-primary']").click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/app-root/app-home/div/app-player/app-alert/div/div/footer/button[1]").click()


#unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
#if __name__ == "__main__":
#    unittest.main()