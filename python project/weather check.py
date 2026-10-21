import requests
import csv
from datetime import date
from collections import Counter

API_KEY = "6166bd47164f15630fa9cfeadcd129e4"
FILE = "weather_log.csv"
1


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        print("Status code:", response.status_code)
        print("API response:", data)
        if response.status_code == 401:
            print("Invalid API key!")
            return None

        if response.status_code == 404:
            print("City not found!")
            return None

        if response.status_code != 200:
            print("Something went wrong!")
            return None

        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        return temperature, condition

    except requests.RequestException:
        print("Unable to connect to weather service.")
        return None



def add_weather():

    city = input("Enter city name: ")

    result = get_weather(city)

    if result is None:
        return

    temperature, condition = result
    today = str(date.today())

    
    try:
        with open(FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Date"] == today and row["City"].lower() == city.lower():

                    print("Weather for this city is already added today!")
                    return

    except FileNotFoundError:
        pass

    
    with open(FILE, "a", newline="") as file:

        writer = csv.writer(file)

    
        if file.tell() == 0:
            writer.writerow(
                ["Date", "City", "Temperature", "Condition"]
            )

        writer.writerow(
            [today, city, temperature, condition]
        )

    print("Weather log added successfully!")



def view_logs():

    try:
        with open(FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            print("\n--- WEATHER LOGS ---")

            for row in reader:

                print(
                    f"Date: {row['Date']} | "
                    f"City: {row['City']} | "
                    f"Temperature: {row['Temperature']}°C | "
                    f"Condition: {row['Condition']}"
                )

    except FileNotFoundError:

        print("No weather logs found.")



def show_statistics():

    try:
        with open(FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            temperatures = []
            conditions = []

            for row in reader:

                temperatures.append(
                    float(row["Temperature"])
                )

                conditions.append(
                    row["Condition"]
                )

        
        if len(temperatures) == 0:

            print("No data available.")
            return

        
        average = sum(temperatures) / len(temperatures)

    
        highest = max(temperatures)

    
        lowest = min(temperatures)

    
        most_common = Counter(conditions).most_common(1)[0][0]

        print("\n--- WEATHER STATISTICS ---")

        print("Average temperature:", round(average, 2), "°C")
        print("Highest temperature:", highest, "°C")
        print("Lowest temperature:", lowest, "°C")
        print("Most frequent condition:", most_common)

    except FileNotFoundError:

        print("No weather logs found.")



while True:

    print("\n--- WEATHER LOGGER ---")
    print("1. Add weather log")
    print("2. View all logs")
    print("3. Show statistics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_weather()

    elif choice == "2":

        view_logs()

    elif choice == "3":

        show_statistics()

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid choice! Please enter 1, 2, 3, or 4.")