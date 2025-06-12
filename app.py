from flights import get_flights

airport_code = input("Enter airport IATA code (e.g. AMS): ").upper()

data = get_flights(airport_code)

if data:
    print("✈️ Arrivals:")
    for f in data.get("arrivals", []):
        print(f"{f['departure']['airport']['name']} → {f['arrival']['scheduledTime']}")

    print("\n🛫 Departures:")
    for f in data.get("departures", []):
        print(f"{f['arrival']['airport']['name']} ← {f['departure']['scheduledTime']}")
