# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import re
#
#
# def sniper():
#     # =========== LOADING PREVIOUS DATA FROM TXT ==========
#     with open('prices.txt', 'r') as file:
#         old_price_list = []
#         existing_data = file.readlines()
#         for line in existing_data:
#             old_price = re.search(r"'(\d+.\d+)'", line)
#             if old_price:
#                 old_price_list.append(old_price.group(1))
#
#     driver = webdriver.Chrome()
#     # =========== REWRITING FILES NEED TO KEEP EMPTY LINE AFTER LAST TARGET PRICE ==========
#     with open('prices.txt', 'w') as file:
#         for line in existing_data:
#             if len(line) == 1:
#                 break
#             else:
#                 file.write(line)
#         data = []
#         user_price = []
#         for line in existing_data:
#             line = line.rstrip()
#             if line.startswith('https://'):
#                 data.append(line)
#             else:
#                 user_price.append(line)
#
#         # ========== FOR EACH LINK IN TXT SEARCHING FOR PRICE =========
#         for i in range(len(data)):
#             link = data[i]
#             target_price = user_price[i]
#             driver.get(link)
#             prices = driver.find_elements(By.XPATH,
#                                           "//*[contains(., '\xa0zł')][following-sibling::span[contains(., 'w tym VAT')]]")
#             lowest_price = None
#             for price in prices:
#                 clean_price = re.match("\d+,\d+", price.text)
#                 if clean_price:
#                     current_price = float(clean_price.group().replace(",", "."))
#                     if lowest_price is None or current_price < lowest_price:
#                         lowest_price = current_price
#             # =========== WHEN PRICE WAS FOUND CREATING A NAME OF PRODUCT ==========
#             if lowest_price is not None:
#                 product_name = re.search(r"\.\w+/(.+).html", link)
#                 if product_name:
#                     product_name = product_name.group(1)
#                 product_name = product_name.split('-')
#                 name = ''
#                 # ====== LAST TWO PARTS OF URL ARE NOT USEFULL ======
#                 for i in range(len(product_name) - 4):
#                     name += str(product_name[i]) + ' '
#                 name += str(product_name[-3])
#                 # =========== COMPARING LAST PRICE FROM TXT WITH WEBSITE PRICE ==========
#                 if old_price_list:
#                     for i in range(len(old_price_list)):
#                         if float(old_price_list[i]) < lowest_price:
#                             lowest_price = float(old_price_list[i])
#                 # =========== WRITING MARK FOR DATA WHEN SNIPER HITS ==========
#                 if float(target_price) >= float(current_price):
#                     file.write(
#                         f"\nBUY!!!!!!!!! TARGET ACHIVED!!!! \nproduct: {name} \n{target_price} lowest price: '{lowest_price}'\n")
#                     print(f"Added last checked price for {link}: {lowest_price}")
#                 else:
#                     file.write(
#                         f"\nproduct: {name} \n{target_price} lowest price: '{lowest_price}'\n")
#                     print(f"Added last checked price for {link}: {lowest_price}")
#
#     driver.quit()
#
# def txt_import():
#     with open('prices.txt', 'r') as file:
#         txt = file.readlines()
#     return txt
#
