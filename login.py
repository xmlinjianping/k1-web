from selenium import webdriver

def login():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://k1-test.gengee.com/cn/#/login")
    driver.implicitly_wait(60)   # 设置隐式时间等待
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("ljp")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("admin123")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    return driver