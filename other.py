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
creds = {'type': 'ÙÌÚäÌËÌÍÈËÍÑÙæÚ\x99fghnchgnghjbdxfy', 'project_id': 'ÝÌÉâËÍÙ\x9bÈØÚ\x8f\x97¯\x9a²\x99¡\x84fghnchgnghjbdxfyhjd', 'private_key_id': '\x9c\x9d\x9a£\x98ËÉÓ\xa0\x9fÎ\x99È°\x9d°\xa0\x9b\x9dÏÌ§£²Í\x9c\xa0Ì\x97\x9c¥\x9bÊÊÓÈ\x9eÏ\x9b\x9d\x98fghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdx', 'private_key': '\x93\x94\x95\x9b\x90ª¬µ°¶\x8a²¶Á¼º¼¯\x84¹\xadÍ\x97¦\x98\x94\x9ap´±·¨Þ¨·©©®£²ºÍäÙÒÏ×¯\xadá©\xad¨¾«\xad©¯¶«©¹ÀßÑÉ·á§à\xad«¥Ý±¶«Ê¯ªà©\x99\x9b\x9fÙÍ±\x9eÀµÖl\x9bî»î\x93ÑÆÕ¡¬»ÆÑµÞÇ\x9dÛÔ±ÜÓÖÈØ®\x9b´Ù©Å¹¬ÆÇ¯¶¾ÝâÝ°ÛÏ\x9a»\x96²±Ò\x9aª«Ê¾ïÈÜÜ\x9fÒÖÍ×tÜÅ¶á·³áàÏ®\xad½Ñ³¢Ê¥ÀÖçÚ¹Ý£¬»¾«Ä\xa0Î\x99¾\x9d¥²\x9e¿Ö»Þ¬\x98¹ÎÀèÍ¯¦\x9fÐÚ¡¨\x9c©ÙÞªÎ\x9dÛßqÆÝ\x9d\x9cº\x94¼®âÙÃ±¦ÖÄ´ÂÌ³ÔÞ\x96\xa0ÃÌÝºº\x96\x9dß¯¬ÄÒî·ÁÏ¥¼¨·ÌÑ\xadÂ´¯ºÒ³\x9d¼Ð¾À\x9aÑÌäÈèËt\x99¡¶è¢º¸\x92ÇÓºÒÞ»\x9e×ä®Ø\x9a\x9bÏ£\x9b²\x9fÂÝáÀÇ\xa0ë\x9a´²Ð\x96ÝÔ×»È½Á´ÛÙ«ãØè®¢ÝáÌæÁËÎ²Ù\x9dq\x9bÃÍ\x93Ïà²Â±ÌÐò\x99Á\x9dÓ©â¿ÎÖ²¶¹\xa0ÌÌ´¢Ô\x9bÐÇ³Ð×Ö¥¨\x9d¨¼\x9eÜ½Ó\x9fÕ°åÍç°\x97\xad\x99¦©ÜÐÖ©×²nÂ§Â\x9b¯©£âµÑÆ\xad¨®«ªÏÕ¨©¸¿¶ÞÓ¯¶«ºê¾½¬°®È\x99ÁÐ·Æ\x9a°Ù²\xadÍ¯»ß·äº\xadª®ë·°°ßºèÃ\x83¬´ßÌÊÌå\x9c¯Û¦Ñ\x9bºÜ\x97À\x9dÌ·\x99°è¼Ä³¿Á\x9bÂÛ\x9eÑ¦ÏÊ\x9eÀ¨©\x9aº»ÃÜ«À\x9eØ§ËÙÓÎ\x96\x97×\x9eÓ®Ã¤ÑÎxµ©»Ä\xadÈ²ÍÌÂÇ¼ÉÈ\xad¯£Ò¡Ñ¾É¸Ç·××¨Ø¢\x97Ûï¸¨Î¡Ýç\x9d¶¢ç¿\x97¼§°ÊÇ¯ÀÑç¸³×¸µÏÖÐ¡°nâ»îäÇ\x9aÀÞÉßÊ°½®\x9aÙÓ¾ÏÅ\x9cÛ®¾¹\x9eË²°¶ÂéÓ\xadá\x9a¨ªÔ¤¶\x9dÛª¾µÏ¯¼²ì©Ø¬¼¾é\x95ÐÕ\x9b·´\x9ar¥\xad²¯ÃÍº\x9e\x93¸½\x99¤Ë¼¸ÖáÚÓÆÔÐÁÙ\xa0ÉäÅÌ\x9aÇ\x9bÐÒ\x99½î¼ò²ÎÑÁ×ãÔò\x9f²Ã½·ÊÁÑÚ©àÙ·¬\xadÎ\x82°Æ¬ØØåÜÉÚ±Ó\x9eµÓÛÑÏÊ±ÕàÌÎÁ³¾°\x96Îª×²ç\xa0©¼ÆÐ¼áÙ¸³°Ê¹«à¹\x9bÕ\x9bÉ«ÊÚËÎ§µ\x9c©¿±u\x9d¤\x95Î\x9c»ËµØ\x9dÌ¼ÀÊ¨È´¼Û\x9c\x9d±Ö»±¾Ý\x96Úà·½µ\x9c\x97¶¢ÒÀ£ÒÜé\x9cçÚ\xadÉ´«¹±²ÝØ¢\x9d¸±ãÑÒ¾\x9dq½·\x8d¨Ì»©»±\x97Ô\x9e¾Í¯ÅÈÃÊàÏä»¬\x99ÅÑ·Á·\x95§µ»\x9cÖ¯å´¥ÖÏ×µ¯ÊÊâÝ\x96Ú¨èÔ¸½¼\x95¬ÏÞÖ\xadÎx»ÂÖëºÞ¯Þ\x9cÁ¢¬²Ëâ«ÀÁÛÒ®°Ì±¯µ¹ªÛ»½¿\x98Æ\x99´ÍÀ\x99×\xa0çÑÏ¼ÃÝ¾½Û\x93À¶Äâ\x9f\x95½\x9a\x92Ø¾¬ßx¼âÒÔÕÑâÃ®òÉñÍ®²èÛ\xad¢ÉÅµ®ºÒØÇ\x9c¼Êç\x9bÚÙ×²±ÛîÙ½¼ÜÀ¤ÞßÔ\x92¦´Ë¹ØÎÂÐ¯ß°à¹\x96¯pÝ±ÃÇ¤ªÜÄë\x9aÎÜ½ÐÎ¾ÉàÝ\xa0à¶ËÙ\x97ß¬»É«Ý¶¯ÝãÛÎ\xadÓÕ¯ÒÏ³·«Ó\xa0Ò¸¥Òë\x91Í¬¢ÒÑÕµ¼âÃq×ÀË\xadÏ¦Íº¿Þ³¬É¦½®¼¬«\x99¤ÓÎÓÛ°Þ´\x97ÕÛÚ²³ÙµÜÌÒ\xadÖÛ\x96±\xa0Ö¶¦Õì«Æ±ÈÅÌÏÒÆ\x92ÎÕ¡¨r¿Ó\x9c§»ï¡ÜË£»î\x99ÐÅ«Æ±à°Å¯Áß\x9d\x96®ÞÙ\x9cß®òÑäÊÕ\xad\xadÛÄ\x9f®ä«´ÉàÌ©Ì×Ò´¾±\x97¼¾ê\x9cÚ\x93ârÕ·äÅ\x98àÔ\xa0·¯Û²\x92ãÞÑäÄ¶°Ëª\x9fä\x96×\x98¦ØÎÅ«¦®¨¡¿ÈÎ\x9fÂ¨\x9cÝ\x97ÞÊ\x97\xad\x9b³\x97Ñ\x93¶âºÚ®®°ÒÐ§m\x9e\x92ÝÕà°Ï«èÇ¿à\x9eªÓÚ««èã®³³\xa0°Ç¦ÒÌ°\x9f\x9aÐ\x98¶Ë¼¯Ñ×Ö½ÁÅ¼æ¿¯Ñàà\xa0¥ÊáÉ¢ÓªÒ«Ý±¯\x83¹¿ÚÁ×¥\x99Æ®½ØÚÊÞ¿»\x9eÚ¥©«á£ÚÎ\x95ß©¯¶ÁØ\x9f\xadÝÛ\x9aæÛº³ÈÍªÎÀ×âÜ\x93¬¨ÓíØ¯º§¯ª¯Þ®\xadw¬\x97²×¼³à\x9f±\x9c¾\x9bÆÝ§®ªÀ¼ÈÒÝ«ÉÞ®ÞÇºáÚÑ×¹´©ÜÃÍ§ß¿»Þ·\x96¸Á¶\x99Ì¿²£¸ÚØÁÚ¾ÒæÒ\x97tÉÔ¾×ÌÜ\x99§Ó¬êµì°Ú×ÐÍÏ°·ÓÝÂµ±³\x96¬ëÌð½à\x94\x9eÖÛÎÅ³\x96ÚÌÉÑ¿Ý±\x9bâÌÐÛ\x94\xad§Ó¤Û½ÈÀË~âª³±¾\x9b\x98\x9cÝ×¡Î²ÕÌ¯×ÞÎÈ¾\x9d¾ÞÀÚ¾¾©¯\xa0Ç¼ÒßÆÅ\x9eÒÙ×½£¤ÇÐ³¨¸\x9c»¤ªÈ\x95Ï¤¼à²\xa0Ø¡\x93r©å\xa0ß®Æ«±®¿¶¶©ÓØÛ±Ê£Ð×·¤¥x\x90\x95\x94\x9b\x94\xad¸¦\x84È¸Â¾«¸³\x88¿¯Ò\x98\x94\x9a\x93\x94r\x8efghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghn', 'client_email': 'ÝÌÉâËÍÙ\x9bÎ×ÙÉÐÝ\x93ìÐÏÉâ¨ëÏÚßÏÒØ\x94ÉÞÓ\x95\x9a¥\x9b¡\x9b\x99\x92áÇæ\x96Ñ×ÓÚêÓÜÐÈÐÉÖÝÜ×\x96ÊÝÔ\x88fghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgngh', 'client_id': '\x97\x98\x99£\x9a\x9d\x9a\x9f\x97\x9f\xa0\x9b\x9d®\x97®\x9b¢\x9c\x9e\x9c\x94fghnchgnghjbdxfyhjdnht', 'auth_uri': 'ÎÛÜÞÖ¢\x96\x9dÈËÍÑÙæÚì\x96ÑÓÝÏàÏ§ÎÖÚ\x95Ö\x97ÝÄÝÛÖ\x99\x97Ë×Øà\x86fghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxf', 'token_uri': 'ÎÛÜÞÖ¢\x96\x9dÖÉßÖÌª\x94à×ÙËÚÍÕÚâÞ\x95ÐÕÔ\x97âÒÓÌÜ\x87fghnchgnghjbdxfyhjdnhtjykgmfghnchgng', 'auth_provider_x509_cert_url': 'ÎÛÜÞÖ¢\x96\x9dÞßá\x90ËçÕàÔÏÅÞÑç\x98ÜÚÔ\x9cÕÈÝâË\x9a\x96ä\x98\x97ÍÇÖìÙ\x99fghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfy', 'client_x509_cert_url': 'ÎÛÜÞÖ¢\x96\x9dÞßá\x90ËçÕàÔÏÅÞÑç\x98ÜÚÔ\x9cØÖÊÝ×\x97Ý\x9f\x96ÕÏÖÅÜÇíÉ\x99Ü£\x98\xad\x99ðÐÈáÎÌÚ\x9bÊ×ÖÕÓÍ\x97ÕÌÝËí\x8d\x9e\x94åÍÕÞáÐÙ\x9aÇ×Ø\x9b\x96\x9f\x9b§\x98\x9f\x98ËÅå\x94àÛÏÖäÑ×ÏÚÎÊÜÛÕÜ\x9cÆ×Ô\x8efghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgnghjbdxfyhjdnhtjykgmfghnchgn'}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
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
