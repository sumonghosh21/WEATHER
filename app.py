import streamlit as st
import requests

# OpenWeatherMap API Key
api_key = "7cbf5bf13f481e8ebfe15d8cde06b36b"

# Function to get weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit app
st.title("Weather App")

# Input for city name
city = st.text_input("Enter City Name")

# Button to get weather
if st.button("Get Weather"):
    weather_data = get_weather(city)
    if weather_data["cod"] == 200:
        st.write(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        st.write("City not found. Please enter a valid city name.")
