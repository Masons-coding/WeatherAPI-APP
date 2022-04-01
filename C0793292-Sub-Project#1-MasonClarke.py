"""

Mason Clarke - 0793292

"""

#Imports for the application
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
import time

#Create Object
root = Tk()

#Set title
root.title('Weather App - Mason Clarke - 0793292')

#Set geometry of the window that is displayed on the screen
root.geometry('560x600')
root.configure(bg='#87ceeb')

#Set max and min size of the window that is displayed on the screen so that the size cannot be readjusted by the user
root.maxsize(560,600)
root.minsize(560,600)

#Starting URL before city and api_key are added
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#Reading in the api_key from a file named config.ini
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

#Function for what happens when the "Click for weather" button is clicked - setting all the labels with the corresponding data from the OpenWeatherMap API and also getting the correct weather icon image from image_function()
def search():
    city = city_text.get()
    results = get_weather(city)
    img = PhotoImage(file = 'weather_icons/iconPlaceHolder.png')
    if results :
        location_lbl['text'] = '{}, {}'.format(results[0], results[1])
        temp_lbl['text'] = '{:.0f}°C, {:.0f}°F '.format(results[2], results[3])
        weatherDescription_lbl['text'] = results[4]
        img = image_funtion()
        windSpeeds_lbl['text'] = '{:.2f} KM/H'.format(results[5])
        humidity_lbl['text']= '{}%'.format(results[6])
        countdowntimer()
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

#Function to get the data from the WeatherAPI in the form of a JSON file by using requests
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        weather = json['weather'][0]['main']
        wind = json['wind']['speed']
        wind_speeds = wind * 3.6
        humidity = json['main']['humidity']
        final = (city, country, temp_celsius, temp_fahrenheit, weather, wind_speeds, humidity)
        return final
    else:
        return None

#Declaration of variables to be used in the clock function
hour=StringVar()
minute=StringVar()
second=StringVar()

#Place holder for weather condition icons that will be replaced with the correct weather icon depending on the weather description from the OpenWeatherMap API (it is just a blank image so that img is initialized)
img = PhotoImage(file = 'weather_icons/iconPlaceHolder.png')

#Function that gets the icon that will replace the weather icon place holder depeding on what the weatherDescription_lbl contains (The blank image will be replaced by an image/icon of the weather condition)
def image_funtion():
    if weatherDescription_lbl['text'] == 'Clear':
        img2 = PhotoImage(file='weather_icons/01d.png')
        image.configure(image=img2)
        image.image = img2
    elif weatherDescription_lbl['text'] == 'Clouds':
        img3 =PhotoImage(file='weather_icons/02d.png')
        image.configure(image=img3)
        image.image = img3
    elif weatherDescription_lbl['text'] == 'Snow':
        img4 = PhotoImage(file='weather_icons/13d.png')
        image.configure(image=img4)
        image.image = img4
    elif weatherDescription_lbl['text'] == 'Rain':
        img5 =  PhotoImage(file='weather_icons/10d.png')
        image.configure(image=img5)
        image.image = img5
    elif weatherDescription_lbl['text'] == 'Drizzle':
        img6 = PhotoImage(file='weather_icons/09d.png')
        image.configure(image=img6)
        image.image = img6
    elif weatherDescription_lbl['text']== 'Thunderstorm':
        img7 = PhotoImage(file='weather_icons/11d.png')
        image.configure(image=img7)
        image.image = img7
    elif weatherDescription_lbl['text'] == 'Mist':
        img8 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img8)
        image.image = img8
    elif weatherDescription_lbl['text'] == 'Smoke':
        img9 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img9)
        image.image = img9
    elif weatherDescription_lbl['text'] == 'Haze':
        img10 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img10)
        image.image = img10
    elif weatherDescription_lbl['text'] == 'Dust':
        img11 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img11)
        image.image = img11
    elif weatherDescription_lbl['text'] == 'Fog':
        img12 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img12)
        image.image = img12
    elif weatherDescription_lbl['text'] == 'Sand':
        img13 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img13)
        image.image = img13
    elif weatherDescription_lbl['text'] == 'Ash':
        img14 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img14)
        image.image = img14
    elif weatherDescription_lbl['text'] == 'Squall':
        img15 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img15)
        image.image = img15
    elif weatherDescription_lbl['text'] == 'Tornado':
        img16 = PhotoImage(file='weather_icons/50d.png')
        image.configure(image=img16)
        image.image = img16

#Timer count down function
def countdowntimer():
    # setting the default value as 30 minutes for the timer
    hour.set("00")
    minute.set("30")
    second.set("00")
    #store the clock_input
    clock_input =  int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        
    while clock_input >-1:
         
        mins,secs = divmod(clock_input,60)
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        #Store the value up to two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        #Updating the GUI window
        root.update()
        time.sleep(1)
        #If clock time gets to 0 then run the search funtion to get the values of the weather again so that the weather updates after 30 minutes has passed
        if (clock_input == 0):
            search()
        #After every second decrease the clock by one second
        clock_input -= 1
    
#Weather app HEADER
weather_app = Label(root,text="YOUR WEATHER TODAY",font=("Times", "24", "bold italic"), bg='#87ceeb',pady=5)
weather_app.pack()

#city_text variable to hold the city name the user types in 
city_text = StringVar()

#Input box that the user can type the city name they wish to see the weather for
city_entry = Entry(root, textvariable=city_text, font=("Arial", "20"),width=30,borderwidth=4, justify=CENTER)
city_entry.pack()

#Button the user clicks to trigger the function that gets the weather information of the city they typed in from the OpenWeatherMap API 
search_btn = Button(root, text="Click for weather",font=("Times", "12", "bold"), width=24, borderwidth=6, bg="#A9A9A9", fg="black",command=search)
search_btn.place(x=170,y=100)

#Label for the city name and country to be placed into from the OpenWeatherMap API
location_lbl=Label(root, text="", font=("bold", 20),bg='#87ceeb')
location_lbl.place(x=210,y=150)

#Label for the temperature values in C and F to be placed in from the OpenWeatherMap API
temp_lbl = Label(root, text="",font=("pacifico", "20","italic"),bg='#87ceeb')
temp_lbl.place(x=210,y=200)

#Label for the weather description to be placed in from the OpenWeatherMap API
weatherDescription_lbl = Label(root, text="",font=("pacifico", "20","italic"),bg='#87ceeb')
weatherDescription_lbl.place(x=340,y=300)

#Images of weather conditon (Weather Icons) this will change depending on what value is placed in the weatherDescription_lbl
image = Label(root,image=img, bg='#87ceeb')
image.place(x=230, y=250)

#Label for wind speed to be placed in from the OpenWeatherMap API
windSpeeds_lbl = Label(root, text="",font=("pacifico", "16","italic"),bg='#87ceeb')
windSpeeds_lbl.place(x=100,y=470)

#Label for humidity to be placed in from the OpenWeatherMap API
humidity_lbl = Label(root, text="",font=("pacifico", "16","italic"),bg='#87ceeb')
humidity_lbl.place(x=100,y=560)

#Label above 30 min timer
clock_lbl = Label(root, text="Weather will update in :",font=("pacifico", "14"),bg='#87ceeb')
clock_lbl.place(x=300,y=530)

#Label above wind speeds
wind_lbl = Label(root, text="Wind Speeds :",font=("pacifico", "16"),bg='#87ceeb')
wind_lbl.place(x=20,y=440)

#Label above humidity
hum_lbl = Label(root, text="Humidity :",font=("pacifico", "16"),bg='#87ceeb')
hum_lbl.place(x=20,y=530)

#30 minute count down labels for the hours, minutes and seconds to be placed into to show the countdown taking place from 30 minutes until no time is remaining
hour_box= Label(root, width=3,bg="black",fg="white", font=("Arial",18,""),textvariable=hour)

hour_box.place(x=400,y=560)
  
mins_box = Label(root, width=3,bg="black",fg="white",  font=("Arial",18,""),textvariable=minute)

mins_box.place(x=450,y=560)
  
sec_box = Label(root, width=3,bg="black",fg="white",  font=("Arial",18,""), textvariable=second)

sec_box.place(x=500,y=560)

#Execute Tkinter
root.mainloop()


