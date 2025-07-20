import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "Replace with your OpenWeatherMap API key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            result_label.config(text=f"Weather: {weather}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s", fg="white", bg="#16213E", padx=20, pady=20, relief=tk.SOLID, bd=5, font=("Arial", 14, "bold"))
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection.")

root = tk.Tk()
root.title("Weather App")
root.geometry("480x550")
root.configure(bg="#0F3460")

header_label = tk.Label(root, text="🌦 Weather App 🌤", font=("Arial", 24, "bold"), bg="#E94560", fg="white", padx=20, pady=15, relief=tk.RIDGE, bd=5)
header_label.pack(fill=tk.X)

city_entry = tk.Entry(root, font=("Arial", 16), width=25, justify='center', bd=5, relief=tk.SUNKEN, bg="#F8F9FA", fg="#1E1E2E")
city_entry.insert(0, "Enter city name")
city_entry.pack(pady=20)

search_button = tk.Button(root, text="🔍 Get Weather", font=("Arial", 14, "bold"), command=get_weather, bg="#27AE60", fg="white", width=20, height=2, bd=5, relief=tk.RAISED, activebackground="#218C54", cursor="hand2")
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#0F3460", fg="white", padx=25, pady=25, relief=tk.GROOVE, bd=4)
result_label.pack(pady=20, padx=20)

exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 14, "bold"), command=root.quit, bg="#E94560", fg="white", width=20, height=2, bd=5, relief=tk.RAISED, activebackground="#C13045", cursor="hand2")
exit_button.pack(pady=20)

root.mainloop()
