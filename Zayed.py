# Importing required modules
import requests

# Input for phone number and message
number = input("Enter the phone number with country code (e.g., +201012345678): ")
message = input("Enter your message: ")

# Confirm sending
confirm = input("Do you want to send the message? (y/n): ").lower()

if confirm == "y":
    # Sending the message using a POST request
    url = "https://www.globfone.com/send-sms"
    data = {
        "number": number,
        "message": message,
        "submit": "Send"
    }

    # Sending the request
    response = requests.post(url, data=data)

    # Checking the response
    if "success" in response.text.lower():
        print(f"Message sent successfully to {number}!")
    else:
        print("Failed to send the message. Please try again.")
else:
    print("Message sending canceled.")
