from tkinter import *
from PIL import ImageTk,ImageTk
import requests
import json

root = Tk()
root.title("Weather App By Devansh")
root.geometry("400x50")


#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=50&API_KEY=DC70D33C-EDCD-4559-BBC4-A6BAE23EF99D
def zipLookup():

    try :
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=50&API_KEY=DC70D33C-EDCD-4559-BBC4-A6BAE23EF99D")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good" :
            weather_color = "#0C0"

        elif category == "Moderate" :
            weather_color = "#FFF00"

        elif category == "Unhealthy for Sensitive Groups" :
            weather_color = "#ff9900"

        elif category == "Unhealthy" :
            weather_color = "#FF0000"

        elif category == "Very Unhealthy" :
            weather_color = "#990066"

        elif category == "Hazardous" :
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(root,text= city +" " + "Air Quality" + " " +str(quality)+" " + category , font = ("Helvatica"),background = weather_color)
        myLabel.grid(row =1,column= 0 ,columnspan = 2 )

    except Exception as e:
        api = "Error...."





zip = Entry(root)
zip.pack()
submit = Button(root,text = "Lookup",command = zipLookup).pack()




root.mainloop()
