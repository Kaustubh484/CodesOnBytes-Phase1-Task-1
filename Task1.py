import pandas as pd
import requests

# Function to fetch data from the JSONPlaceholder API
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to convert data to a DataFrame and save it as a CSV file
def save_as_csv(data, filename="dataset.csv"):
    if data is not None:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Dataset saved as {filename}")
    else:
        print("Unable to save dataset.")

# Main function
def main():
    # Fetch data from the API
    api_data = fetch_data()

    # Save data as a CSV file
    save_as_csv(api_data)

if __name__ == "__main__":
    main()
