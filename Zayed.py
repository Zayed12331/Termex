#!/bin/bash

# مسح الشاشة عند بدء تشغيل السكربت
clear

# رسم اللوجو باسم "zoz" باستخدام figlet
echo "   "
figlet "zoz"
echo "   "

# طلب الرقم من المستخدم
echo "Please enter the phone number (include country code, e.g., +201012345678): "
read number

# إرسال الرسالة مباشرة باستخدام Globfone API
response=$(curl -s -X POST "https://www.globfone.com/send-sms" \
    -d "number=$number" \
    -d "message=مرحبا عزيزي" \
    -d "submit=Send")

# التحقق من نجاح الإرسال
if [[ $response == *"success"* ]]; then
    echo "Message sent successfully to $number!"
else
    echo "Failed to send the message. Please try again."
fi
