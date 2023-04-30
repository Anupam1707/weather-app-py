from tkinter import *
import random
from time import *
from threading import Timer
import json
import os

try: 
    from datetime import datetime
    from PIL import Image, ImageTk
    from io import BytesIO
    import requests
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    print("Installing Libraries")
    print()
    os.system("pip install datetime pillow requests gspread oauth2client")

from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

weather = ""

#root.attributes('-fullscreen', True)
root = Tk()    

 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()


scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
cred = "{
  "type": "service_account",
  "project_id": "weather-app-374917",
  "private_key_id": "66255cbe97d7d877819ad399b53f0478bcea6e99",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDCsC231veJ0YMl\n7vUu+gbg98QMfNqa6sfNtlhapD9PaCLQBbYGBTdwvCuh2M3JJd3BAhZwbct5nhec\ncZOtQLyrlFFOjK8hAHpnrOy5DGT2Y9a3W57O6XhTvB6UVZoeEB1hf7/1BlxCf/xw\nXv52X0DHiqYM8nPJIaLgx/8UiuSL/5uMHLluOWk7T4MSfFUNHRdP5UbWX0ohlboc\n53Nt8AM+ZmSjpX6pvGp09k+597XysXS6r/MEj/uftSaOZLqwGkroF8ysdrWRcKl7\n3Uj+hrKZGjlz3H5iEtWZl9KR3feL4q3iYLhmtA07/T4xOk+k7zfzJ0E+CAuboAmP\nJAI3EE5zAgMBAAECggEAQQOviMR3TqVSHBFT/HePY4IqDJeHMxOzXI2HrOFLqRtY\nAMrfcdw9Gt8j3Pz3H7SO/LzTPIFV4Uu7i8lb7RAA0XWKv2X4t9ceiU+0j8lFUAig\nNAQbIPLTdXcNaTC68k4kWaJdOpiAp85wwR/f7yy5B8nT0OAIbYLXjyQKmVQWpW9F\ntSzzN/YqcxbBZF3klVec8cHEQ4gDHBXphFt4ABfAN6mCVKmKDLsAnHNVu+Wj4JN3\n7JJHUfR41TE3+cRThyfiMiiTs9avbd3Y4hh7YvVyJdmSoojy4KVWPbSnrBrrOBKj\nJMDntwtUp8h7HmtiagInrefWQZ80UBmNy85RMeUtsQKBgQDrR3k9e3dacdCG45U8\n67/g4MhMq/eTVhDPNCs29CnGGEr/mzPUG9/O4kX9pxq6nrCeFCEG9rq57QIunjW/\nUM+DTU0SG3f6Jc6ZaVdygvXD2WjOWU1/OB4lKwL1lVlNBdczo3rAzmPSZ14ienCj\nSNlrOwBx5Y4IJdtDXWyn6JSIEQKBgQDT1Y3MeR6o9yjgRayFWb+VRVz++D/+kXEw\nYzkfnixaJzcxeDNzs98PZNATkpY9Tcy4rouN9uuqSXnX0tfi+9NdQjkZiAxHvW27\ndIYc6BhZr/goWifPfxv2yNaw3gFBaAyHGiybcFfoHjaPODe9jNCns+TD8ncmARiX\njZdEaCeSQwKBgBEHCDA56kZibEwG1nslOKrGudhKrc088lR8mxAMFaXfhjX/fn3A\nUq8/Uv9rg5Sz/WZDYKyHWLYx//Ftw8gHyizfgE9qK4GwEMariAeikLTO3DXq4p/t\naMkZ1sn9OAxJ+uwizbR8e17z2i02nUZD9HA9Qef8TA4s5zR143I3c+BxAoGAJkh9\n6+onxFmGpaFx4Fer7AoxGFM9HYCjeB82f6RSV6imrOYQRmTHdzy87gyb4lBhIy9I\nQUvSo1/MCVktcvQX6s7BCwAvV/fAERSp+Cdp3yuSKZjBgRpzr1H0mtpEV9G6EeCF\nF0JiYKy1J4T9beA5BVXZjiAPsGqaSylnoRFBtYkCgYBvM2JYB/STK6RspSwVkxk/\ngpFqSt/CeDvKsEsjjfgBTkvTNII4HsfwUv00ngdLH/mfbiQzI4tehq2I/m+sSdRc\nx1HJQ514ot9gDndEuzVbE5TzRrJT0D9ZVkwXb6kkpU9BcXM/P2W6BT+V9UsL9p30\nBw9wDdG9HFNLEepgGQ8ijQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "weather-google-sheet@weather-app-374917.iam.gserviceaccount.com",
  "client_id": "111575310769961538804",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/weather-google-sheet%40weather-app-374917.iam.gserviceaccount.com"
}"
with open("credentials.json","+w") as f:
          f.write(cred)
          f.close()
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
SHEET_ID = '1iGbUayAGHMfJncrIVTRr_ac6GlJPx0BJDpvZEZPpTOE'
try:
    spreadsheet = gc.open_by_key(SHEET_ID)
    print("Successfully syncronized with the database.")
    print()
except gspread.exceptions.APIError as e:
    print("Error: Could not connect to the database. Reason:", e)

spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet("Sheet1")
rows = worksheet.get_all_records()

os.remove("credentials.json")

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
 
    city_name = city_value.get()

    for i in range(0,len(rows)):
        if rows[i].get("City") == city_name:
            country = rows[i].get("Country")
            lat = rows[i].get("Latitude")
            lng = rows[i].get("Longitude")
            we = True
            co = False
    
           
    time_url = "https://www.timeapi.io/api/Time/current/coordinate?latitude="+str(lat)+"&longitude="+str(lng)
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
    responset = requests.get(time_url)
    weather_info = response.json()
    time_info = responset.json()
 
    inpfield.delete("1.0", "end")   

    if country == "Unknown":
        for i in range(len(rows)):
            if rows[i].get("Country") == city_name:
                co = True
                we = False
    
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
    n = random.randrange(0,44999)
    city = rows[n].get("City")
    country = rows[n].get("Country")
    lat = rows[n].get("Latitude")
    lng = rows[n].get("Longitude")

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
         
        weather = f"Weather of: {city_name}, {country}\nTime : {time}\nTemperature (Celsius): {tempc}°C\nTemperature (Kelvin): {tempk}K\nTemperature (Farenheit) :{tempf}°F\nPressure: {pressure} hPa\nWind Speed: {wind_speed}m/s\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nWeather Info: {description}" 
    autofield.insert(INSERT, weather) 

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
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
    
response = requests.get("https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/bg.jpg")
img = Image.open(BytesIO(response.content))
img = img.resize((1280,720), Image.LANCZOS)
test = ImageTk.PhotoImage(img)
bk = Label(image=test)
bk.image = test
bk.place(x=0, y=0)  

#Display
root.geometry("1280x720")
root.resizable(False, False)
root.title("Global Weather Bulletin")

title = Label(root, text= 'Global Weather Bulletin', font= 'Arial 40 bold', bg='yellow').pack(pady=0)
name = Label(root, text= 'Programmed by Anupam Kanoongo', font= 'Arial 30 bold').place(x=1, y=665)
city_head= Label(root, text = 'City of your choice :-', font = 'Arial 20 bold', bg='lightblue').place(x=885, y=210)
cus_city_head= Label(root, text = 'Weather Report of Cities across the World', font = 'Arial 20 bold', bg='lightblue').place(x=0, y=210)

inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 16 bold').place(x=880, y=250)

Button(root, text = 'Exit', font = 'Arial 20 bold', bg='red', command=root.destroy).place(x=1205, y=665)
Button(root, command = customWeather, text = "Check Weather", font="Arial 20", bg='lightblue', fg='black', activebackground="teal").place(x=920, y=285)
Button(root, command = showWeather, text = "Refresh", font="Arial 20", bg='lightblue', fg='black', activebackground="teal").place(x=220, y=285)

RepeatedTimer(7, showWeather)
RepeatedTimer(60, date)

inpfield = Text(root, width=36, height=11, font="Arial 19",bg="BlanchedAlmond")
inpfield.place(x=770, y=350)
autofield = Text(root, width=36, height=11, font="Arial 19",bg="BlanchedAlmond")
autofield.place(x=0, y=350)
dtfield = Text(root, width = 20, height = 1, font="Arial 20",bg = "BlanchedAlmond")
dtfield.pack(pady=0)
lbl = Label(root, font="Arial 40",bg='BlanchedAlmond')
lbl.pack(pady=0)

time()
showWeather()
date()
root.mainloop()
