from selenium import webdriver
from selenium.webdriver.common.by import By
import re

with open('prices.txt', 'r') as file:
    data = []
    for line in file:
        line = line.rstrip()
        data.append(line)

print(data)
driver = webdriver.Chrome()

for i in range(0, len(data), 2):
    link = data[i]
    driver.get(link)
    prices = driver.find_elements(By.XPATH, "//*[contains(., '\xa0zł')][following-sibling::span[contains(., 'w tym VAT')]]")
    for price in prices:
        clean_price = re.match("\d+,\d+", price.text)
        if clean_price.group() <= data[i + 1]:
            print(True)
        else:
            print(False)