# run main2 after running this file

import csv
import json
from playwright.sync_api import sync_playwright

url = "https://rtdms.cpcb.gov.in/data/industry-list?id=39&city=Bangalore"

# Define a function to handle the response and save data to CSV
def handle_response(response):
    if "api/industryList/45/39/Bangalore" in response.url:
        data = response.text()
        try:
            json_data = json.loads(data)
            save_to_csv(json_data)
        except json.JSONDecodeError:
            print("Response is not valid JSON")

# Function to save data to CSV
def save_to_csv(data):
    with open("./data/pcb_industry_data.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "id",
            "name",
            "status",
            "createdDate",
            "lastUpdateDate",
            "address",
            "latitude",
            "longitude",
            "city",
            "code",
            "zip",
            "timezone",
            "industryType_id",
            "industryType_type",
            "industryType_description",
            "industryType_status",
            "state_id",
            "state_name",
            "state_zone_id",
            "state_zone_name",
            "state_isGangaBasin",
            "contactEmail",
            "contactNo",
            "consumerLastDataAt",
            "spcbRegionalOffice",
            "listOfEntities",
            "gangaBasin",
            "isGangaBasin"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({
                "id": row["id"],
                "name": row["name"],
                "status": row["status"],
                "createdDate": row["createdDate"],
                "lastUpdateDate": row["lastUpdateDate"],
                "address": row["address"],
                "latitude": row["latitude"],
                "longitude": row["longitude"],
                "city": row["city"],
                "code": row["code"],
                "zip": row["zip"],
                "timezone": row["timezone"],
                "industryType_id": row["industryType"]["id"],
                "industryType_type": row["industryType"]["type"],
                "industryType_description": row["industryType"]["description"],
                "industryType_status": row["industryType"]["status"],
                "state_id": row["state"]["id"],
                "state_name": row["state"]["name"],
                "state_zone_id": row["state"]["zone"]["id"],
                "state_zone_name": row["state"]["zone"]["name"],
                "state_isGangaBasin": row["state"]["isGangaBasin"],
                "contactEmail": row["contactEmail"],
                "contactNo": row["contactNo"],
                "consumerLastDataAt": row["consumerLastDataAt"],
                "spcbRegionalOffice": row["spcbRegionalOffice"],
                "listOfEntities": row["listOfEntities"],
                "gangaBasin": row["gangaBasin"],
                "isGangaBasin": row["isGangaBasin"]
            })

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.on("response", handle_response)

    page.goto(url, wait_until="networkidle", timeout=90000)

    page.context.close()
    browser.close()
