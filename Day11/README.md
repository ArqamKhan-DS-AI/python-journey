# Global Population Data Pipeline

An automated data pipeline built in Python that fetches live population data from the World Bank API, cleans the data, and generates a visual chart of the top 10 most populated countries.

## Features
- **Automated Data Ingestion:** Uses the `requests` library to pull live JSON data from the World Bank API.
- **Data Cleaning:** Uses `pandas` to extract nested dictionaries, drop missing values, and filter out non-country regions.
- **Data Visualization:** Uses `matplotlib` to generate a horizontal bar chart.
- **Error Handling:** Safely handles API timeouts and missing values.

## Technologies Used
- Python 3.12
- `pandas` (Data manipulation)
- `requests` (API calls)
- `matplotlib` (Data visualization)

## How to Run
1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt