
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
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download and Place Chromium Driver**
   
   Download the appropriate Chromium driver for your operating system from [Chromium Downloads](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/chromedriver.md).

   Place the driver executable in the directory containing your `main.py` files.

### Running the Scraping Tasks

Each task is associated with a `main.py` file. To run a scraping task, execute the respective `main.py` file in a local directory. Ensure the chromium driver is present in it and have a data directory created inside the directory too.

#### Consent Orders
   ```sh
   python3 consent_main.py
   ```

#### CPCB Bangalore Industries
   ```sh
   python3 cpcb_main.py
   python3 cpcb_main2.py
   ```

#### KSPCB Lake Data
   ```sh
   python3 kspcb_lake_main.py
   ```

#### KSPCB River Data
   ```sh
   python3 kspcb_river_main.py
   ```

### Additional Notes

- **Chromium Driver**: Ensure the Chromium driver version matches the version of the Chromium browser installed on your machine.
- **Error Handling**: Scripts include basic error handling, but additional logging and exception management can be implemented for robustness.
- **Configuration**: Modify the configuration settings in the respective `main.py` files to match any changes in the website structure or scraping requirements.







