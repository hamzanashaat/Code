
Temperature = input("What's the Temperature Today? ")
Temperature = int(Temperature)
hot_today = "Is it hot today, Stay Hydrated?"
warm_today = "Is it warm today, Enjoy the weather?"
cool_today = "Is it a cool day, Wear a jacket?"
cold_today = "Is it cold today, Stay Warm?"
temperature_today = "What's the Temperature Today?"
if Temperature >= 30:
    print("Hot: " + hot_today)
elif 20 <= Temperature < 30:
    print("Warm: " + warm_today)
elif 10 <= Temperature < 20:
    print("Cool:" + cool_today)
else:
    print("Cold: " + cold_today)
print("Temperature: " + str(Temperature))