from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://www.zalando.pl/adidas-originals-gazelle-bold-sneakersy-niskie-collegiate-red-lucid-pink-core-white-ad111a25a-g14.html"

driver.get(url)
price = driver.find_element(By.CSS_SELECTOR,"span.sDq_FX._4sa1cA.FxZV-M.HlZ_Tf")

print(price.text)
time.sleep(5)


