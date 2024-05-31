

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Example usage:
filename = './data/pcb_industry_data.csv'
csv_data = read_csv(filename)



# Path to chromedriver executable
chromedriver_path = './chromedriver'

# Start a Selenium WebDriver session
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# url = "https://rtdms.cpcb.gov.in/data/industry-list?id=39&city=Bangalore"

# # Navigate to the webpage
# driver.get(url)

# Wait until the table elements are present
# wait = WebDriverWait(driver, 10)
# links = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pointer")))

# Initialize an empty list to store data
data = []

for x in range(len(csv_data)-1):
    print(csv_data[1+x][0])
    
    driver.get(f"https://rtdms.cpcb.gov.in/data/industry-public?id={csv_data[1+x][0]}")
    
    time.sleep(4)
    wait = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cell.station-param.bg-color-white")))
    station_table=driver.find_elements(By.CLASS_NAME, "cell.station-param.bg-color-white")

    for element in station_table:

        station_name = element.find_element(By.TAG_NAME, "h4").text
        rows = element.find_elements(By.TAG_NAME, "tr")
        
        # Loop through each row
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            
            # Extract data from cells
            if len(cells) > 1:
                try:
                    param_name = cells[0].find_element(By.TAG_NAME, "div").text
                except:
                    param_name = "N/A"
                try:
                    param_value = cells[2].find_element(By.TAG_NAME, "span").text
                except:
                    param_value = "N/A"
                try:
                    param_unit = cells[2].find_element(By.TAG_NAME, "small").text
                except:
                    param_unit = "N/A"
                try:
                    param_time = cells[5].find_element(By.TAG_NAME, "span").text
                except:
                    param_time = "N/A"
                
                
                # Append data to the list
                data.append({
                    "Industry Id":csv_data[1+x][0],
                    "Industry Name":csv_data[1+x][1],
                    "Station Name": station_name,
                    "Parameter Name": param_name,
                    "Value": param_value,
                    "Unit": param_unit,
                    "Time": param_time
                })

    driver.back()

driver.quit()

# Write data to CSV file
csv_file_path = "./data/complete_data.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Industry Id","Industry Name","Station Name", "Parameter Name", "Value", "Unit", "Time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("Data extracted and saved to", csv_file_path)

