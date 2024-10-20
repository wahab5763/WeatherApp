import streamlit as st
import requests

# OpenWeatherMap API details
API_KEY = "SHA256:mDBvmuJWMiaG2BK0T3fJv+WgtPVjdzSt6TfCiSLhOt0"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# List of Sindh cities
sindh_cities = [
    "Karachi", "Hyderabad", "Sukkur", "Larkana", 
    "Mirpur Khas", "Nawabshah", "Khairpur", "Thatta"
]

# Streamlit app title and description
st.title("Sindh Cities Weather App 🌤️")
st.write("Select a city from Sindh to see the current weather conditions.")

# City selection dropdown
selected_city = st.selectbox("Select a City", sindh_cities)

# Button to fetch weather data
if st.button("Get Weather"):
    # API request parameters
    params = {
        "q": selected_city,
        "appid": API_KEY,
        "units": "metric"  # Temperature in Celsius
    }

    # Send API request
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Check if the API request was successful
    if response.status_code == 200:
        # Extract weather details
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display weather information
        st.success(f"Weather in {selected_city}")
        st.write(f"**Temperature**: {temp}°C")
        st.write(f"**Weather**: {weather_desc.capitalize()}")
        st.write(f"**Humidity**: {humidity}%")
        st.write(f"**Wind Speed**: {wind_speed} m/s")
    else:
        # Handle errors
        st.error("Could not retrieve weather data. Please try again.")
