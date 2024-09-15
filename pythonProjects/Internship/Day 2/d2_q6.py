# Import necessary libraries
import requests
import pandas as pd
import time

# Define the API endpoint for fetching ISS current location data
url = "http://api.open-notify.org/iss-now.json"

# Define the header to mimic a browser request
headers = {
    "User-Agent": ("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 "
                   "Mobile Safari/537.36")
}

# Initialize an empty list to store the ISS location data
iss_data = []

# Specify the number of records to collect (100 in this case)
num_records = 100

# Loop to collect ISS location data
for attempt in range(num_records):
    try:
        # Send GET request to fetch the current ISS position
        response = requests.get(url, headers=headers)
        
        # Verify the success of the request (status code 200)
        if response.status_code == 200:
            # Extract JSON data from the response
            data = response.json()
            
            # Get latitude, longitude, and timestamp from the response
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            timestamp = data['timestamp']
            
            # Store the data in the list as a dictionary
            iss_data.append({
                'timestamp': timestamp,
                'latitude': latitude,
                'longitude': longitude
            })
            
            # Log the collected data for this iteration
            print(f"Record {attempt + 1}: Latitude {latitude}, Longitude {longitude} at {timestamp}")
        else:
            print(f"Failed to fetch data for attempt {attempt + 1} (Status code: {response.status_code})")
    
    except Exception as err:
        # Handle any exceptions that may occur during the request
        print(f"Error during attempt {attempt + 1}: {err}")
    
    # Introduce a 1-second delay to avoid hitting API rate limits
    time.sleep(1)

# Check if any data was collected
if iss_data:
    # Create a DataFrame from the collected data
    iss_df = pd.DataFrame(iss_data)
    
    # Save the data to a CSV file (adjust the path as needed)
    csv_file_path = 'iss_location_data.csv'
    iss_df.to_csv(csv_file_path, index=False)

    print(f"Data collection complete! {num_records} records saved to {csv_file_path}.")
else:
    print("No data was collected.")
