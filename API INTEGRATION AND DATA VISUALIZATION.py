import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = 'dde6d408a53f52af5236f18f2016b207'
CITY = 'London'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

def parse_data(data):
    # Extract datetime, temperature, humidity, and pressure
    times = []
    temps = []
    humidity = []
    pressure = []

    for entry in data['list']:
        dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        times.append(dt)
        temps.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])
        pressure.append(entry['main']['pressure'])
    return times, temps, humidity, pressure

def plot_data(times, temps, humidity, pressure):
    plt.figure(figsize=(14, 8))

    # Temperature plot
    plt.subplot(3, 1, 1)
    plt.plot(times, temps, 'r-', marker='o')
    plt.title(f'5 Day Weather Forecast for {CITY}')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    # Humidity plot
    plt.subplot(3, 1, 2)
    plt.plot(times, humidity, 'b-', marker='x')
    plt.ylabel('Humidity (%)')
    plt.grid(True)

    # Pressure plot
    plt.subplot(3, 1, 3)
    plt.plot(times, pressure, 'g-', marker='s')
    plt.ylabel('Pressure (hPa)')
    plt.xlabel('Date & Time')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    data = fetch_weather_data()
    if data:
        times, temps, humidity, pressure = parse_data(data)
        plot_data(times, temps, humidity, pressure)

if __name__ == '__main__':
    main()
