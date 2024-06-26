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

driver.get("https://xgn.karnataka.gov.in/CSHARP/ALLConsentOrder.aspx")

ctr = 0
match_ctr=0

pg_no=1


while(True):

    WebDriverWait(driver,2).until(
    EC.presence_of_element_located((By.ID, "dgPro"))
    )

    table = driver.find_element(By.ID, "dgPro")

    rows = table.find_elements(By.TAG_NAME,"tr")

    with open(f'./data/page_{pg_no}.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Writing the headers (if necessary, adjust these to match the actual headers)
        headers = ['Inw', 'Industry Name', 'Industry Colour', 'Regional Office', 'Inw Dt', 'Inw Type', 'Inw Status', 'Insp ID', 'Grt Dt', 'Consent No', 'Uploaded Doc', 'Validity', 'e_outwardval']
        writer.writerow(headers)

        # rows2.clear()
        # match_ctr=0

        # Skipping the header row of the table
        for row in rows[2:]:
            cols = row.find_elements(By.TAG_NAME,'td')
            cols = [col.text.strip() for col in cols]
            # print('//////',cols)
            writer.writerow(cols)


        pg_no+=1

    try:
        
        link = driver.find_element(By.LINK_TEXT,str(pg_no))
    
    except NoSuchElementException:
        if pg_no==11:
            link = driver.find_elements(By.LINK_TEXT,'...')[0]
        else:
            if(len(driver.find_elements(By.LINK_TEXT,'...'))==2):
                link = driver.find_elements(By.LINK_TEXT,'...')[1]
            else:
                break

    link.click()
    




time.sleep(0)

driver.quit()
