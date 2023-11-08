from tkinter import *
from time import *
from threading import Timer
import os
from sql_scripts import *
try: 
    from datetime import datetime
    from PIL import Image, ImageTk
    import requests
except ImportError:
    print("Installing Libraries")
    print()
    os.system("pip install datetime pillow requests")

from datetime import datetime
from PIL import Image, ImageTk
import requests

weather = ""

root = Tk() 
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
city_value = StringVar()

now = datetime.now()
print("Successfully sycnronized the Features")
print()

def customWeather():
    global weather
    lng = 0
    lat = 0
    co = False
    we = True
    country = "Unknown"

    api_key = "141f5109c5c29634665af4a4a59e95a6"
 
    city_name=city_value.get()

    countryid, lat, lng = execute_query(f"select country_id, latitude, longitude from cities where name = '{city_name}'")[0]
    country = execute_query(f"select name from countries where id = {countryid}")[0][0]
    
    # for i in range(0,len(rows)):
    #     if rows[i].get("City") == city_name:
    #         country = rows[i].get("Country")
    #         lat = rows[i].get("Latitude")
    #         lng = rows[i].get("Longitude")
    #         we = True
    #         co = False
    
           
    time_url = "https://www.timeapi.io/api/Time/current/coordinate?latitude="+str(lat)+"&longitude="+str(lng)
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
    responset = requests.get(time_url)
    weather_info = response.json()
    time_info = responset.json()
 
    inpfield.delete("1.0", "end")   

    # if country == "Unknown":
    #     for i in range(len(rows)):
    #         if rows[i].get("Country") == city_name:
    #             co = True
    
    if co == False and we == True:
        kelvin = 273 
        tempc = int(weather_info['main']['temp'] - kelvin)
        tempk = int(weather_info['main']['temp'])
        tempf = ((9*tempc)/5)+32
        tempf = round(tempf,1)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        time = time_info.get("time")
        wind_speed = weather_info['wind']['speed']

        if lat == 0 and lng == 0:
            time = "Unable to Fetch Time"
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
         
        weather = f"Weather of: {city_name}, {country}\nTime : {time}\nTemperature (Celsius): {tempc}°C\nTemperature (Kelvin): {tempk}K\nTemperature (Farenheit) :{tempf}°F\nPressure: {pressure} hPa\nWind Speed: {wind_speed} m/s\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nWeather Info: {description}"

    else:
        if co == True:
            weather = f"You have given a name of a Country.\nPlease enter a name of a City"
        elif we == False:
            weather = f"Weather for {city_name} not found"
            
    inpfield.insert(INSERT, weather) 
            
def showWeather():
    global weather
    
    city = execute_query("select name from cities order by rand() limit 1")[0][0]
    print(city)
    countryid, lat, lng = execute_query(f"select country_id, latitude, longitude from cities where name = '{city}'")[0]
    country = execute_query(f"select name from countries where id = {countryid}")[0][0]

    autofield.delete("1.0", "end")

    api_key = "141f5109c5c29634665af4a4a59e95a6"
 
    city_name=city
    
    time_url = "https://www.timeapi.io/api/Time/current/coordinate?latitude="+str(lat)+"&longitude="+str(lng)
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
    responset = requests.get(time_url)
    
    weather_info = response.json()
    time_info = responset.json()
   
    if weather_info['cod'] == 200:
        kelvin = 273 
        tempc = int(weather_info['main']['temp'] - kelvin)
        tempk = int(weather_info['main']['temp'])
        tempf = ((9*tempc)/5)+32
        tempf = round(tempf,1)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        time = time_info.get("time")
        wind_speed = weather_info['wind']['speed']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)\
         
        weather = f"Weather of: {city_name}, {country}\nTime : {time}\nTemperature (Celsius): {tempc}°C\nTemperature (Kelvin): {tempk}K\nTemperature (Farenheit) :{tempf}°F\nPressure: {pressure} hPa\nWind Speed: {wind_speed} m/s\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nWeather Info: {description}" 
    autofield.insert(INSERT, weather) 

class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.timer = None
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.timer = Timer(self.interval, self._run)
            self.timer.daemon = True
            self.timer.start()
            self.is_running = True

    def stop(self):
        self.timer.cancel()
        self.is_running = False
        
def date():
    dtfield.delete("1.0", "end")
    url = "https://www.timeapi.io/api/Time/current/coordinate?latitude="+str(22.7206)+"&longitude="+str(75.8472)
    responsed= requests.get(url)
    info = responsed.json()
    day = info.get("dayOfWeek")
    d = info.get("day")
    m = info.get("month")
    y = info.get("year")
    data = f"{day}  {d}/{m}/{y}"

    dtfield.insert(INSERT,data)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
    
# response = requests.get("https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/bg.jpg")
# img = Image.open(BytesIO(response.content))
img = Image.open("bg.jpg")
img = img.resize((width,height), Image.LANCZOS)
test = ImageTk.PhotoImage(img)
bk = Label(image=test)
bk.image = test
bk.place(x=0, y=0)  

#Display
root.attributes('-fullscreen', True)
root.title("Global Weather Bulletin") 

title = Label(root, text= 'Global Weather Bulletin', font= 'Arial 40 bold', bg='yellow').pack(pady=0)
name = Label(root, text= 'Programmed by Anupam Kanoongo', font= 'Arial 30 bold').pack(side = "left", anchor = "sw")
city_head= Label(root, text = 'City of your choice :-', font = 'Arial 20 bold', bg='lightblue').place(x=width-555, y=int(height/3)+25)
cus_city_head= Label(root, text = 'Weather Report of Cities across the World', font = 'Arial 20 bold', bg='lightblue').place(x=50, y=int(height/3)+50)

inp_city = Entry(root, textvariable = city_value,  width = 25, font='Arial 16 bold').place(x=width-555, y=int(height/3)+67)

Button(root, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = "right", anchor = "se")
Button(root, command = customWeather, text = "Check Weather", font="Arial 20", bg='lightblue', fg='black', activebackground="teal").place(x=width-555, y=int(height/3)-35)
Button(root, command = showWeather, text = "Refresh", font="Arial 20", bg='lightblue', fg='black', activebackground="teal").place(x=50, y=int(height/3)-10)

RepeatedTimer(8, showWeather)
RepeatedTimer(60, date)

inpfield = Text(root, width=36, height=11, font="Arial 19",bg="BlanchedAlmond")
inpfield.place(x=width-555, y=int(height/3)+100)
autofield = Text(root, width=36, height=11, font="Arial 19",bg="BlanchedAlmond")
autofield.place(x=50, y=int(height/3)+100)
dtfield = Text(root, width = 20, height = 1, font="Arial 20",bg = "BlanchedAlmond")
dtfield.place(x = int(width/2)-150, y = 2 * int(height/6))
lbl = Label(root, font="Arial 40",bg='BlanchedAlmond')
lbl.place(x = int(width/2)-150, y = 2 * int(height/6)+50)

time()
showWeather()
date()
root.mainloop()
