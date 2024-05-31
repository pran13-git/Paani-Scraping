# Paani-Scraping

This repository contains the code and setup instructions for various web scraping tasks related to environmental data.

## Websites Scraped

1. **Consent Orders** - [XGN Karnataka](https://xgn.karnataka.gov.in/CSHARP/ALLConsentOrder.aspx)
2. **CPCB Bangalore Industries** - [CPCB Data](https://rtdms.cpcb.gov.in/data/industry-list?id=39&city=Bangalore)
3. **KSPCB Lake Data** - [KSPCB Lake](https://tpro.telsys.in/tpportal/kspcblake)
4. **KSPCB River Data** - [KSPCB River](https://tpro.telsys.in/tpportal/kspcbriver)

## Technologies Used

- **Selenium**: Used for scraping dynamic content from websites.
- **Playwright**: Used for handling XHR requests and scraping Angular.js based websites.

## Setup Instructions

### Prerequisites

- Python 3.x
- Chromium WebDriver for Selenium
- Required Python packages (specified in `requirements.txt`)

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/paani-scraping.git
   cd paani-scraping
Install Dependencies

sh
Copy code
pip install -r requirements.txt
Download and Place Chromium Driver

Download the appropriate Chromium driver for your operating system from Chromium Downloads.
Place the driver executable in the directory containing your main.py files.
Running the Scraping Tasks
Each respective folder contains a main.py file. To run a scraping task, navigate to the folder and execute the main.py file.

Consent Orders

sh
Copy code
cd consent-orders
python3 main.py
CPCB Bangalore Industries

sh
Copy code
cd cpcb-bangalore-industries
python3 main.py
KSPCB Lake Data

sh
Copy code
cd kspcb-lake
python3 main.py
KSPCB River Data

sh
Copy code
cd kspcb-river
python3 main.py
Additional Notes

Chromium Driver: Ensure the Chromium driver version matches the version of the Chromium browser installed on your machine.
Error Handling: Scripts include basic error handling, but additional logging and exception management can be implemented for robustness.
Configuration: Modify the configuration settings in the respective main.py files to match any changes in the website structure or scraping requirements.
Contribution

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License. See the LICENSE file for details.





