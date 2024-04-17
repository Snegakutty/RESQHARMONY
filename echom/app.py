from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Define the phone numbers you want to send alerts to
friend_numbers = ['']

# Define your alert message
alert_message = "Accident happened to the person at Latitude: 13.0449408 Longitude: 80.19968"

# Send alert messages to each friend
for number in friend_numbers:
    message = client.messages.create(
        body=alert_message,
        from_='',  # Twilio phone number
        to=number
    )
    print(f"Alert message sent to {number}: {message.sid}")
