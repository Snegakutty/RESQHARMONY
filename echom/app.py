from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC5531ef9202bb75912c06228c9d3758db'
auth_token = '007eddf9e7b0efbaa63336fa1aff9c75'
client = Client(account_sid, auth_token)

# Define the phone numbers you want to send alerts to
friend_numbers = ['+916382095224', '+918637677387', '+918778405645', '+919585752915']

# Define your alert message
alert_message = "Accident happened to the person at Latitude: 13.0449408 Longitude: 80.19968"

# Send alert messages to each friend
for number in friend_numbers:
    message = client.messages.create(
        body=alert_message,
        from_='+17792464076',  # Twilio phone number
        to=number
    )
    print(f"Alert message sent to {number}: {message.sid}")