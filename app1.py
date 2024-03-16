import random
import math
import time
from twilio.rest import Client

# Twilio credentials (replace these with your actual Twilio credentials)
account_sid = "AC40ac42830bcd6ed05dbf92b0ab8bc498"
auth_token = "751edfdc548ac4032c3d80c66c3cf1de"
twilio_phone_number = "+12093184471"
recipient_phone_number = "+918637677387"

# Create Twilio client
client = Client(account_sid, auth_token)

# Simulated GPS module generating random latitude and longitude coordinates
def generate_random_coordinates():
    latitude = random.uniform(30.0, 40.0)  # Simulated latitude range
    longitude = random.uniform(-120.0, -100.0)  # Simulated longitude range
    return latitude, longitude

# Simulated hospital database with randomly generated locations
hospitals = [
    {"name": "Hospital A", "latitude": random.uniform(30.0, 40.0), "longitude": random.uniform(-120.0, -100.0)},
    {"name": "Hospital B", "latitude": random.uniform(30.0, 40.0), "longitude": random.uniform(-120.0, -100.0)},
    {"name": "Hospital C", "latitude": random.uniform(30.0, 40.0), "longitude": random.uniform(-120.0, -100.0)}
]

# Simulated threshold value for proximity detection
threshold_value = 5.0  # Simulated threshold value in kilometers

# Simulated proximity detection and emergency triggering
def simulate_proximity_detection():
    latitude, longitude = generate_random_coordinates()
    print(f"Current location: Latitude {latitude}, Longitude {longitude}")

    # Simulate proximity detection (random value)
    simulated_proximity = random.uniform(0.0, 10.0)  # Simulated proximity value in kilometers
    print(f"Simulated proximity to switch: {simulated_proximity} km")

    # Check if simulated proximity exceeds threshold
    if simulated_proximity > threshold_value:
        print("Emergency detected: Airbag compartment door open")
        send_emergency_message(latitude, longitude)

# Calculate distance between two coordinates (simplified)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Find nearest hospital based on current location
def find_nearest_hospital(latitude, longitude):
    min_distance = float('inf')
    nearest_hospital = None
    for hospital in hospitals:
        distance = calculate_distance(latitude, longitude, hospital["latitude"], hospital["longitude"])
        if distance < min_distance:
            min_distance = distance
            nearest_hospital = hospital
    return nearest_hospital

# Send emergency message to the hospital using Twilio
def send_emergency_message(latitude, longitude):
    nearest_hospital = find_nearest_hospital(latitude, longitude)
    if nearest_hospital:
        message_body = f"Emergency: Airbag compartment door open. Current location: Latitude {latitude}, Longitude {longitude}"
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to=recipient_phone_number
            )
            print(f"Emergency message sent to {nearest_hospital['name']} at Latitude {nearest_hospital['latitude']}, Longitude {nearest_hospital['longitude']}")
        except Exception as e:
            print(f"Error sending message: {str(e)}")

# Main simulation loop
def main():
    while True:
        simulate_proximity_detection()
        print("---------------------------------------")
        time.sleep(5)  # Simulated delay between iterations (5 seconds)

if __name__ == "__main__":
    main()
