import requests
import pyttsx3

def get_weather(city):
    api_key = "nnnn"  # my weather API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]
        
        weather_report = (f"The temperature in {city} is {temperature}°C with {weather_desc}. "
                          f"The humidity level is {humidity} percent.")
        
        return weather_report
    else:
        return "City not found. Please try again."


def speak_weather(city):
    weather_info = get_weather(city)
    print(weather_info)
    
    engine = pyttsx3.init()
    engine.say(weather_info)
    engine.runAndWait()
