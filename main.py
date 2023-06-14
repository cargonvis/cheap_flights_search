import http.client
import json
import requests
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import datetime
import os

IATA_AND_ICAO_API_KEY = "YOUR IATA_AND_ICAO_API_KEY"
KIWI_API_KEY = "YOUR KIWI_API_KEY"
SENDER_EMAIL = "YOUR_SENDER_EMAIL"
RECEIVER_EMAIL = "YOUR_RECEIVER_EMAIL"
GMAIL_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"

print('''
  ______   __                                            ________  __  __            __          __              
 /      \ /  |                                          /        |/  |/  |          /  |        /  |             
/$$$$$$  |$$ |____    ______    ______    ______        $$$$$$$$/ $$ |$$/   ______  $$ |____   _$$ |_    _______ 
$$ |  $$/ $$      \  /      \  /      \  /      \       $$ |__    $$ |/  | /      \ $$      \ / $$   |  /       |
$$ |      $$$$$$$  |/$$$$$$  | $$$$$$  |/$$$$$$  |      $$    |   $$ |$$ |/$$$$$$  |$$$$$$$  |$$$$$$/  /$$$$$$$/ 
$$ |   __ $$ |  $$ |$$    $$ | /    $$ |$$ |  $$ |      $$$$$/    $$ |$$ |$$ |  $$ |$$ |  $$ |  $$ | __$$      \ 
$$ \__/  |$$ |  $$ |$$$$$$$$/ /$$$$$$$ |$$ |__$$ |      $$ |      $$ |$$ |$$ \__$$ |$$ |  $$ |  $$ |/  |$$$$$$  |
$$    $$/ $$ |  $$ |$$       |$$    $$ |$$    $$/       $$ |      $$ |$$ |$$    $$ |$$ |  $$ |  $$  $$//     $$/ 
 $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ $$$$$$$/        $$/       $$/ $$/  $$$$$$$ |$$/   $$/    $$$$/ $$$$$$$/  
                                        $$ |                              /  \__$$ |                             
                                        $$ |                              $$    $$/                              
                                        $$/                                $$$$$$/                               
                                        ''')

# Run API for loading all the IATA codes and its correspondient name of airlines
conn = http.client.HTTPSConnection("iata-and-icao-codes.p.rapidapi.com")
headers = {
    'x-rapidapi-key': IATA_AND_ICAO_API_KEY, # IATA AND ICAO API KEY
    'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com"
    }
conn.request("GET", "/airlines", headers=headers)
res = conn.getresponse()
airlines = res.read()
formatted_data = json.loads(airlines)

flight_type = "round" # input("Enter flight type (oneway/round): ")
origin = "HEL" # input("Enter origin airport code: ").upper()
destination = "NONE" # input("Enter destination airport code: ").upper()
adults = 1 # int(input("Enter number of adults: "))
currency = "EUR" # input("Enter the currency (EUR/USD...): ")
min_nights = 2 # int(input("Enter minimum nights in destination: "))
max_nights = 4 # int(input("Enter maximum nights in destination: "))
price_from = 0 # int(input("Enter minimum price: "))
price_to = 60 # int(input("Enter maximum price: "))
amount_offers = 10 # int(input("Enter the amount of offers that you want to receive by email. If less or none are sent is that there were no offers: "))

if destination == "NONE":
    destination = None

while True: # Repeat the code

    date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") # input("Enter start date of search (YYYY-MM-DD): ")
    date_to = (datetime.datetime.now() + datetime.timedelta(days=181)).strftime("%Y-%m-%d") # input("Enter end date of search (YYYY-MM-DD): ")

    # API for searching flights using KIWI
    # Set the API endpoint and parameters
    url = "https://tequila-api.kiwi.com/v2/search" # URL
    headers = {
        "apikey": KIWI_API_KEY, # KIWI API KEY
        "accept": "application/json"
    }

    if flight_type == "oneway":

        params = {
            "flight_type": flight_type, # Switch for oneway/round flights search - will be deprecated in the near future
            "fly_from": origin, # Origin destination airport (if not chosen, it flights from everywhere)
            "fly_to": destination, # Arrival destination airport (if not chosen, it flights to everywhere)
            "date_from": date_from, # Date when range of dates starts
            "date_to": date_to, # Data when range of dates ends
            # "fly_days": [0,1,2,3,4,5,6], # List of week days for the origin flight, where 0 is Sunday, 1 is Monday, etc. BE CAREFUL THAT MAYBE DEPARTURE AND ARRIVAL CANNOT BE IN DIFFERENT DAYS
            "only_working_days": False, # Search flights with departure only on working days
            "only_weekends": False, # Search flights with departure only on weekends
            "adults": adults, # Amount of adults
            "curr": currency, # Currency (EUR, USD...)
            "dtime_from": "00:01", # Minimum departure time in origin flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM)
            "atime_to": "23:59", # Maximum arrival time in origin flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM)
            "max_stopovers": 0, # Maximum amount of stopovers
            # "select_airlines": , #string a list of airlines (IATA codes) separated by ',' (commas) that should / should not be included in the search. The selection or omission of the airline depends on the 'select_airlines_exclude' parameter.
            "selected_cabins": "M", # Preferred cabin class. Cabins can be: M (economy), W (economy premium), C (business), or F (first class).
            "price_from": price_from,  # Minimum price
            "price_to": price_to,  # Maximum price
            "sort": "price", # Sorts the results by quality, price, date or duration. Price is the default value
            "asc": 1, # integer can be set to 1 or 0, default is 1, from cheapest flights to the most expensive
            "limit": 500, # integer limit number of results; the default value is 200; max is up to the partner (500 or 1000)
        }
    
    else:

        params = {
            "flight_type": flight_type, # Switch for oneway/round flights search - will be deprecated in the near future
            "fly_from": origin, # Origin destination airport (if not chosen, it flights from everywhere)
            "fly_to": destination, # Arrival destination airport (if not chosen, it flights to everywhere)
            "ret_from_diff_city": False, # Possibility to return from a different airport # DEACTIVATE IF ONEWAY
            "ret_to_diff_city": False, # Possibility to return to a different airport # DEACTIVATE IF ONEWAY
            "date_from": date_from, # Date when range of dates starts
            "date_to": date_to, # Data when range of dates ends
            # "fly_days": [0,1,2,3,4,5,6], # List of week days for the origin flight, where 0 is Sunday, 1 is Monday, etc. BE CAREFUL THAT MAYBE DEPARTURE AND ARRIVAL CANNOT BE IN DIFFERENT DAYS
            "only_working_days": False, # Search flights with departure only on working days
            "only_weekends": False, # Search flights with departure only on weekends
            "adults": adults, # Amount of adults
            "curr": currency, # Currency (EUR, USD...)
            "dtime_from": "00:01", # Minimum departure time in origin flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM)
            "atime_to": "23:59", # Maximum arrival time in origin flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM)
            "ret_dtime_from": "00:01", # Minimum departure time in returning flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM) # DEACTIVATE IF ONEWAY
            "ret_atime_to": "23:59", # Maximum arrival time in returning flight (use only time in whole hours, not minutes; 11:00 means 11AM, 23:00 means 11PM) # DEACTIVATE IF ONEWAY
            "max_stopovers": 0, # Maximum amount of stopovers
            # "select_airlines": , #string a list of airlines (IATA codes) separated by ',' (commas) that should / should not be included in the search. The selection or omission of the airline depends on the 'select_airlines_exclude' parameter.
            "selected_cabins": "M", # Preferred cabin class. Cabins can be: M (economy), W (economy premium), C (business), or F (first class).
            "nights_in_dst_from": min_nights, # Minimum nights in destination # DEACTIVATE IF ONEWAY
            "nights_in_dst_to": max_nights, # Maximum nights in destination # DEACTIVATE IF ONEWAY
            "price_from": price_from,  # Minimum price
            "price_to": price_to,  # Maximum price
            "sort": "price", # Sorts the results by quality, price, date or duration. Price is the default value
            "asc": 1, # integer can be set to 1 or 0, default is 1, from cheapest flights to the most expensive
            "limit": 500, # integer limit number of results; the default value is 200; max is up to the partner (500 or 1000)
        }

    # Send the API request and get the response
    response = requests.get(url, headers=headers, params=params)

    # Parse the response to get the flight data
    data = response.json()

    if "data" in data:
        quotes = data["data"]

        # Extract the flight data and save it to a DataFrame
        columns = ["Departure Airport", "Destination Airport", "Departure City", "Destination City", "Departure Date", "Return Date", "Airline", "Price",  "Distance", "Duration"]

        rows = []
        for quote in quotes:
            dep_airport = quote["flyFrom"]
            dest_airport = quote["flyTo"]
            dep_city = quote["cityFrom"]
            dest_city = quote["cityTo"]
            dep_date = quote["route"][0]["local_departure"].split("T")[0]
            return_date = quote["route"][-1]["local_arrival"].split("T")[0]
            airline = quote["airlines"]
            for iata_code in airline:
                airline_name = [airline["name"] for airline in formatted_data if airline["iata_code"] == iata_code][0]
            price = quote["price"]
            # currency = quote["currency"]
            distance = quote["distance"]
            # Deal with duration in seconds
            seconds = quote["duration"]["total"]
            # Convert duration to hours, minutes and seconds
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            duration = f'{hours}h, {minutes}m, {seconds}s'

            row = [dep_airport, dest_airport, dep_city, dest_city, dep_date, return_date, airline_name, price, distance, duration]
            rows.append(row)

        df = pd.DataFrame(rows, columns=columns)
        df.to_csv("flights.csv", index=False)

        # Print the first few rows of the DataFrame with meaningful column names
        # display(df) # Only working in Jupyter labs

        # sort the flights by price and select the 10 cheapest flights
        amount_of_results = len(df)

        if amount_of_results >= amount_offers:
            cheapest_flights = df.sort_values('Price').head(amount_offers)
        else:
            cheapest_flights = df.sort_values('Price').head(amount_of_results)

        if amount_of_results != 0:
            # create email message
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECEIVER_EMAIL
            msg['Subject'] = f'{amount_offers} Cheapest Flight Offers'

            # iterate through each cheapest flight and add to email message
            for i, cheapest_flight in cheapest_flights.iterrows():
                flight_info = f"Departure Airport: {cheapest_flight['Departure Airport']}\n" \
                            f"Destination Airport: {cheapest_flight['Destination Airport']}\n" \
                            f"Departure City: {cheapest_flight['Departure City']}\n" \
                            f"Destination City: {cheapest_flight['Destination City']}\n" \
                            f"Departure Date: {cheapest_flight['Departure Date']}\n" \
                            f"Return Date: {cheapest_flight['Return Date']}\n" \
                            f"Airline: {cheapest_flight['Airline']}\n" \
                            f"Price: {cheapest_flight['Price']} Euros \n\n" \
                            f"-----------------------------------------\n\n"

                msg.attach(MIMEText(flight_info))

            # send email message
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
                smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

            print("Email sent successfully!")

        else:
            print(f"No offers found at {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}.")
        
        # Delete csv file with last search (OPTIONAL)
        os.remove('flights.csv')

    time.sleep(1800) # Sleep for 30 min and repeat the code again