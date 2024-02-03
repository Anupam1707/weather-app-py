import pygame
import requests
from datetime import datetime
from io import BytesIO
from PIL import Image
from fetchify import fetch

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30

# Set up the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Global Weather Bulletin")

# Load background image
try:
    bg_image = Image.open(BytesIO(fetch("bg.jpg", "we", image=True)))
    bg_image = bg_image.resize((WIDTH, HEIGHT))
    bg_surface = pygame.image.fromstring(bg_image.tobytes(), bg_image.size, bg_image.mode)
except:
    print("Failed to load background image")

# Fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# Functions
def get_weather(city_name):
    api_key = "141f5109c5c29634665af4a4a59e95a6"
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(weather_url)
    weather_info = response.json()

    if weather_info['cod'] == 200:
        return weather_info
    else:
        return None

def display_weather(weather_info, country):
    # Extract relevant information
    temperature_kelvin = weather_info['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    pressure = weather_info['main']['pressure']
    humidity = weather_info['main']['humidity']
    wind_speed = weather_info['wind']['speed']
    description = weather_info['weather'][0]['description']
    sunrise_timestamp = weather_info['sys']['sunrise']
    sunset_timestamp = weather_info['sys']['sunset']

    # Convert timestamps to readable times
    sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')
    sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%H:%M:%S')

    # Display information on the screen
    text = f"Weather in {city_name}, {country}\n"
    text += f"Temperature: {temperature_celsius:.2f}°C / {temperature_fahrenheit:.2f}°F\n"
    text += f"Pressure: {pressure} hPa\n"
    text += f"Humidity: {humidity}%\n"
    text += f"Wind Speed: {wind_speed} m/s\n"
    text += f"Description: {description}\n"
    text += f"Sunrise: {sunrise_time}\n"
    text += f"Sunset: {sunset_time}"

    # You need to decide how to display this text on the Pygame screen
    # For simplicity, let's print it to the console
    print(text)


# Main loop
running = True
city_name = ""
input_screen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if input_screen:
                if event.key == pygame.K_RETURN:
                    # Switch to the weather display screen
                    weather_info = get_weather(city_name)
                    if weather_info:
                        display_weather(weather_info, "Unknown Country")  # You can fetch country info similarly
                        input_screen = False
                    else:
                        print("Invalid city name")

                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace to modify the entered city name
                    city_name = city_name[:-1]
                else:
                    # Append other key presses to the city name
                    city_name += event.unicode

    # Draw background
    screen.blit(bg_surface, (0, 0))

    if input_screen:
        # Display the current city name being typed
        text = font.render(city_name, True, WHITE)
        screen.blit(text, (10, 10))
    else:
        # Display weather information on the weather screen
        # Implement this part based on your requirements
        pass

    pygame.display.flip()

# Quit Pygame
pygame.quit()
