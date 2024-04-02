import re
import requests
from bs4 import BeautifulSoup


def snipe_price():
    # =========== LOADING PREVIOUS DATA FROM TXT ==========
    with open('prices.txt', 'r') as file:
        old_price_list = []
        existing_data = file.readlines()
        for line in existing_data:
            old_price = re.search(r"'(\d+.\d+)'", line)
            if old_price:
                old_price_list.append(old_price.group(1))
    print(old_price)
    # =========== REWRITING FILES NEED TO KEEP EMPTY LINE AFTER LAST TARGET PRICE ==========
    with open('prices.txt', 'w') as file:
        for line in existing_data:
            if len(line) == 1:
                break
            else:
                file.write(line)
        data = []
        user_price = []
        for line in existing_data:
            line = line.rstrip()
            if line.startswith('https://'):
                data.append(line)
            else:
                user_price.append(line)
        # ========== FOR EACH LINK IN TXT SEARCHING FOR PRICE =========
        for i in range(len(data)):
            link = data[i]
            target_price = user_price[i]
            response = requests.get(link)

            if old_price_list:
                lowest_price = old_price_list[i]
            else:
                lowest_price = None

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                target_element = soup.find('span', string='w tym VAT')
                if target_element:
                    previous_element = target_element.find_previous_sibling()
                    clean_price = re.match("\d+,\d+", previous_element.text)
                    if clean_price:
                        current_price = float(clean_price.group().replace(",", "."))
                        if lowest_price is None or current_price < float(lowest_price):
                            lowest_price = current_price

            # =========== WHEN PRICE WAS FOUND CREATING A NAME OF PRODUCT ==========
                    if clean_price is not None:
                        product_name = re.search(r"\.\w+/(.+).html", link)
                        if product_name:
                            product_name = product_name.group(1)
                        product_name = product_name.split('-')
                        name = ''
                        # ====== LAST TWO PARTS OF URL ARE NOT USEFULL ======
                        for i in range(len(product_name) - 4):
                            name += str(product_name[i]) + ' '
                        name += str(product_name[-3])

                        # =========== WRITING MARK FOR DATA WHEN SNIPER HITS ==========
                        if float(target_price) >= float(current_price):
                            file.write(
                                f"\nBUY!!!!!!!!! TARGET ACHIVED!!!! \nproduct: {name} \n{target_price} lowest price: '{lowest_price}'\n")
                            print(f"Added last checked price for {link}: {lowest_price}")
                        else:
                            file.write(
                                f"\nproduct: {name} \n{target_price} lowest price: '{lowest_price}'\n")
                            print(f"Added last checked price for {link}: {lowest_price}")
