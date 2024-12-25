#!/bin/bash

# Ask for the phone number
echo "Enter the phone number with country code (e.g., +201012345678):"
read number

# Ask for the message
echo "Enter your message:"
read message

# Confirm sending
echo "Do you want to send the message? (y/n):"
read confirm

if [[ $confirm == "y" || $confirm == "Y" ]]; then
    # Send the message using curl
    response=$(curl -s -X POST "https://www.globfone.com/send-sms" \
        -d "number=$number" \
        -d "message=$message" \
        -d "submit=Send")

    # Check the result
    if [[ $response == *"success"* ]]; then
        echo "Message sent successfully to $number!"
    else
        echo "Failed to send the message. Please try again."
    fi
else
    echo "Message sending canceled."
fi