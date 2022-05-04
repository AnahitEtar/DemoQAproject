from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = executable_path = './chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys('Julia')
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys('ahj.23@gmail.com')
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys('3232 Thompson Ave')
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys('555 Lower Detroit Rd')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.find_element(By.XPATH, "//button[@id='submit']").click()

driver.close()
driver.quit()
