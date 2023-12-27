import requests 
import geopy
import tkinter as tk
geolocator = geopy.Nominatim(user_agent="weather")
api_key = '45db40e61c13b4a4c6609debf481e505'
root = tk.Tk()
root.geometry('600x400')
root.resizable(False , False)
#search 


search_entry = tk.Entry(root , width=40 )
search_entry.place(x= 100 , y = 10)

def search():
    user_input = search_entry.get()
    location = geolocator.geocode(user_input)
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}')
    output = tk.Label(root ,text=str(int(weather.json()['main']['temp'])-273)+"°C" , font=('Helvetica bold',40))
    output.place(x=250 , y= 100)
    

search_button = tk.Button(root , text="SEARCH" , command= search)
search_button.place(x=440 , y= 10)
root.mainloop()