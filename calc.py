import csv
import os

def load_emission_factors(filename):
    data = {}
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return data

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['category'].strip().lower()
            data[category] = float(row['factor'])
    return data

def calculate_footprint(factors):
    print("===============================================")
    print("          CARBON FOOTPRINT CALCULATOR          ")
    print("===============================================")
    print("Let's calculate your monthly carbon footprint!\n")

    electricity = float(input("1. Electricity usage (kWh per month): "))
    car_km = float(input("2. Car travel (km per month): "))
    bike_km = float(input("3. Bike travel (km per month): "))
    bus_km = float(input("4. Bus travel (km per month): "))
    flights = int(input("5. Short flights per month: "))
    water_liters = float(input("6. Water usage (liters per day): "))
    waste_kg = float(input("7. Waste (kg per week): "))
    diet = input("8. Diet (veg / nonveg): ").strip().lower()

    elec_em = electricity * factors.get("electricity", 0)
    car_em = car_km * factors.get("car", 0)
    bike_em = bike_km * factors.get("bike", 0)
    bus_em = bus_km * factors.get("bus", 0)
    flight_em = flights * factors.get("flight", 0)
    water_em = water_liters * 30 * factors.get("water", 0)
    waste_em = waste_kg * 4 * factors.get("waste", 0)

    diet_em = factors.get("diet_veg", 0) if diet == "veg" else factors.get("diet_nonveg", 0)

    total_emission = (
        elec_em + car_em + bike_em + bus_em +
        flight_em + water_em + waste_em + diet_em
    )

    if total_emission < 300:
        level = "Low"
    elif total_emission < 700:
        level = "Moderate"
    else:
        level = "High"

    print("\n------------------------------------------")
    print("              RESULT SUMMARY              ")
    print("------------------------------------------")
    print(f"Electricity: {elec_em:.2f} kg CO₂")
    print(f"Transport: {(car_em + bike_em + bus_em + flight_em):.2f} kg CO₂")
    print(f"Water: {water_em:.2f} kg CO₂")
    print(f"Waste: {waste_em:.2f} kg CO₂")
    print(f"Diet: {diet_em:.2f} kg CO₂")
    print("------------------------------------------")
    print(f"Total Monthly Carbon Footprint: {total_emission:.2f} kg CO₂")
    print(f"Emission Level: {level}")
    print("------------------------------------------")

    print("\nThanks for using the Carbon Footprint Calculator!")
    print("------------------------------------------")


csv_file = "emission_factors.csv"
factors = load_emission_factors(csv_file)

if factors:
    calculate_footprint(factors)
else:
    print("⚠ Couldn't load emission factors. Check CSV file path.")