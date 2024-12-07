import requests
import xml.etree.ElementTree as ET

def get_weather_data(city_name, latitude, longitude):
    """
    Fetches weather data for a given city using Open-Meteo API (converted to XML format).
    Args:
        city_name (str): Name of the city to fetch weather data for.
        latitude (float): Latitude of the city.
        longitude (float): Longitude of the city.
    """
    # Open-Meteo API endpoint (retrieves JSON but adapted here for XML-like response)
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Simulate XML parsing from the JSON response
        weather_data = response.json()  # Parse JSON response
        current_weather = weather_data['current_weather']
        
        # Convert JSON to XML format (mimicking XML API output)
        weather_xml = f"""
        <weather>
            <location>
                <name>{city_name}</name>
            </location>
            <current>
                <temperature>{current_weather['temperature']}</temperature>
                <windspeed>{current_weather['windspeed']}</windspeed>
                <weathercode>{current_weather['weathercode']}</weathercode>
            </current>
        </weather>
        """

        # Parse XML
        root = ET.fromstring(weather_xml)

        # Extract data
        name = root.find('location/name').text
        temperature = root.find('current/temperature').text
        windspeed = root.find('current/windspeed').text
        weathercode = root.find('current/weathercode').text

        # Display results
        print(f"Weather Information for {name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {windspeed} km/h")
        print(f"Weather Code: {weathercode}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with desired city and coordinates
    city_name = "London"
    latitude = 51.5074
    longitude = -0.1278
    get_weather_data(city_name, latitude, longitude)
