import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url: str) -> pd.DataFrame:
    """Downloads data from an API and returns it as a pandas DataFrame."""
    print("Downloading data from the World Bank API...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # This will crash if the website returns an error (like 404)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame() # Return an empty DataFrame if it fails

    # The World Bank API returns a list with two elements. 
    # The first element [0] contains metadata, the second [1] contains our actual data.
    data = response.json()
    actual_records = data[1]
    
    # Load the records into a pandas DataFrame
    df = pd.DataFrame(actual_records)
    return df

if __name__ == "__main__":
    # This URL fetches the population of all countries for the year 2022
    api_url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2022&format=json&per_page=300"
    
    df = fetch_data(api_url)
    
    print("\n--- DATA PREVIEW ---")
    print(df.head())

print("\n--- CLEANING THE DATA ---")
    
# 1. Extract the text from the dictionary columns
# We use .apply() to go through every single row and pull out the "value" key
df["country_name"] = df["country"].apply(lambda x: x["value"] if isinstance(x, dict) else x)
df["indicator_name"] = df["indicator"].apply(lambda x: x["value"] if isinstance(x, dict) else x)

# 2. Select only the columns we care about
columns_to_keep = ["countryiso3code", "country_name", "indicator_name", "date", "value"]
df_clean = df[columns_to_keep]

# 3. Show the clean data
print(df_clean.head())

print("\n--- POPULATION OF PAKISTAN AND INDIA ---")
# Filter for just Pakistan and India
target_countries = ["Pakistan", "India"]
filtered_df = df_clean[df_clean["country_name"].isin(target_countries)]
    
# Sort by population (highest first)
filtered_df = filtered_df.sort_values(by="value", ascending=False)
    
print(filtered_df[["country_name", "value"]])

print("\n--- CLEANING FOR ANALYSIS ---")
# 1. Drop rows where 'value' (population) is missing
# 2. Filter for a specific list of real countries
real_countries = [
        "India", "China", "United States", "Indonesia", "Pakistan", 
        "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"
    ]
df_countries = df_clean[df_clean["country_name"].isin(real_countries)]
    
# 3. Sort by highest population and get the top 10
top_10 = df_countries.sort_values(by="value", ascending=False).head(10)
    
print(top_10[["country_name", "value"]])


print("\n--- GENERATING CHART ---")
    
# 1. Create the figure
plt.figure(figsize=(10, 6))
    
# 2. Draw the bar chart (we reverse the order so the biggest is at the top)
plt.barh(top_10["country_name"][::-1], top_10["value"][::-1], color="teal")
    
# 3. Add labels and title
plt.title("Top 10 Most Populated Countries (2022)", fontsize=16)
plt.xlabel("Population", fontsize=12)
plt.ylabel("Country", fontsize=12)
    
# 4. Save the chart to the day11 folder
plt.savefig("day11/top_10_population.png")
print("Chart saved as day11/top_10_population.png!")