import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

PATH = "C:\Program Files\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.cnnindonesia.com/')
print(driver.title)

search = driver.find_element(By.ID, 'nav_search').find_element(By.NAME, 'query')
search.send_keys('ekonomi')
search.send_keys(Keys.RETURN)

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.list.media_rows'))
  )
  articles = driver.find_element(By.CSS_SELECTOR, '.list.media_rows').find_elements(By.TAG_NAME, 'article')
  for article in articles:
    title = article.find_element(By.CLASS_NAME, 'title')
    print(title.text)
finally:
  driver.quit()