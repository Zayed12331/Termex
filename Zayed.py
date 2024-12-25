#!/bin/bash

# Clear the screen
clear

# Ask for phone number
echo "Please enter the phone number (include country code, e.g., +201012345678): "
read number

# Simulate loading
echo "Processing..."
sleep 2

# Ask if the user wants to send the message
echo "Do you want to send the message? (y/n): "
read confirm

if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
    # Simulate sending the message
    echo "Sending message..."
    sleep 2
    
    # Sending the SMS using Globfone's API
    response=$(curl -s -X POST "https://www.globfone.com/send-sms" \
        -d "number=$number" \
        -d "message=مرحبا عزيزي" \
        -d "submit=Send")
    
    # Check if the message was successfully sent
    if [[ $response == *"success"* ]]; then
        echo "Message sent successfully to $number!"
    else
        echo "Failed to send the message. Please try again."
    fi
else
    echo "Message not sent."
fi
