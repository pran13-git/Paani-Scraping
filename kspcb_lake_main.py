from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.common.exceptions import NoSuchElementException
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://tpro.telsys.in/tpportal/kspcblake")

ctr = 0
match_ctr=0

pg_no=1



WebDriverWait(driver,10).until(
EC.presence_of_element_located((By.CLASS_NAME, "table-condensed"))
)

table = driver.find_element(By.CLASS_NAME, "table-condensed")

rows = table.find_elements(By.TAG_NAME,"tr")

print(rows)

with open(f'./data/kpcb_scraped.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # Writing the headers (if necessary, adjust these to match the actual headers)
    # headers = rows[0]
    # writer.writerow(headers)

    # rows2.clear()
    # match_ctr=0

    # Skipping the header row of the table
    for row in rows:
        if(ctr==0):
            heads = row.find_elements(By.TAG_NAME,'th')
            heads = [head.text.replace('\n',' ') for head in heads]
            print(heads)
            writer.writerow(heads)
            ctr+=1
        else:
            cols = row.find_elements(By.TAG_NAME,'td')       
            cols = [col.text.strip() for col in cols]    
            print(cols)   
            writer.writerow(cols)


time.sleep(0)

driver.quit()
