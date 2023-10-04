
"""
 Prayer Times App with a GUI
 
 Created By *Abdullah EL-Yamany*

 YouTube Channel => Codezilla
 Video Link => https://youtu.be/Ap8benrtnoM?si=abWhXCqDZtZ5TNvi
"""

import requests as rq
import tkinter as tk
from tkinter import ttk, messagebox

 


def fetch_prayer_times(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=5"

    try:
        response = rq.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None

    except Exception as ex:    # massage of Every Error
        messagebox.showerror("Error", f"Unexpected Error Occurred {ex}") # return


def gui_fetch_prayer_times():
    city = city_entry.get()
    country = country_entry.get()


    if city and country:
        prayer_times = fetch_prayer_times(city, country)
        result_show.delete(0, tk.END) # Update1
        for name, time in prayer_times.items():
            result_show.insert(tk.END, f"{name} : {time}")
    
    else:
        messagebox.showerror("Error", "Unable To Fetch Prayer Times, Please Enter Correct City and Country Names")



app = tk.Tk()
app.title("Prayer Times")

frame = ttk.Frame(app, padding = "20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="      City: ")
city_label.grid(row=0, column=0, pady=5)
city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=5)

country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=5)
country_entry = ttk.Entry(frame, width=20)
country_entry.grid(row=1, column=1, pady=5)

fetch_button = ttk.Button(frame, text="Get Prayer Times", command=gui_fetch_prayer_times)
fetch_button.grid(row=2, column=0, columnspan=2, pady=15)

result_show = tk.Listbox(frame, height=13, width=25)
result_show.grid(row=3, column=0, columnspan=2, pady=15)

app.mainloop()

# Update2: show more data [date, hijri]
# Update3: Deal with api using other way