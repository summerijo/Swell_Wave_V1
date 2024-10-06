import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Define the latitude and longitude
latitude = 54.544587
longitude = 10.227487

# Step 1: Fetch data from API
url = f'https://barmmdrr.com/connect/gmarine_api?latitude={latitude}&longitude={longitude}&hourly=swell_wave_height,swell_wave_direction,swell_wave_period,swell_wave_peak_period'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Step 2: Connect to the database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root_123',
            database='swell_wave'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Step 3: Create table if not exists
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS SwellData (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                swell_wave_height FLOAT,
                swell_wave_direction FLOAT,
                swell_wave_period FLOAT,
                swell_wave_peak_period FLOAT,
                latitude FLOAT NOT NULL,
                longitude FLOAT NOT NULL
            );
            '''
            cursor.execute(create_table_query)

            # Step 4: Insert data into the table
            hourly_data = data.get('hourly', {})
            timestamps = hourly_data.get('time', [])
            swell_wave_heights = hourly_data.get('swell_wave_height', [])
            swell_wave_directions = hourly_data.get('swell_wave_direction', [])
            swell_wave_periods = hourly_data.get('swell_wave_period', [])
            swell_wave_peak_periods = hourly_data.get('swell_wave_peak_period', [])

            # Check if all lists have the same length
            if len(timestamps) == len(swell_wave_heights) == len(swell_wave_directions) == len(swell_wave_periods) == len(swell_wave_peak_periods):
                for i in range(len(timestamps)):
                    timestamp_str = timestamps[i]
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M')  # Adjusted format
                    swell_wave_height = swell_wave_heights[i]
                    swell_wave_direction = swell_wave_directions[i]
                    swell_wave_period = swell_wave_periods[i]
                    swell_wave_peak_period = swell_wave_peak_periods[i]

                    # Handle NULL values: set default value or skip insertion
                    if swell_wave_peak_period is None:
                        swell_wave_peak_period = 0.0  # Assign default value, can be adjusted based on your needs
                    
                    # Step 4: Prepare the insert query with latitude and longitude
                    insert_query = '''
                    INSERT INTO SwellData (timestamp, swell_wave_height, swell_wave_direction, swell_wave_period, swell_wave_peak_period, latitude, longitude)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    '''
                    cursor.execute(insert_query, (timestamp, swell_wave_height, swell_wave_direction, swell_wave_period, swell_wave_peak_period, latitude, longitude))

                # Step 5: Commit and close
                connection.commit()
            else:
                print("Error: Data lists have different lengths.")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print(f"Failed to retrieve data: {response.status_code}")
