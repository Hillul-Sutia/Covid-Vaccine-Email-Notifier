import requests
import time
from datetime import datetime,timedelta
import json
import smtplib

print("Starting search for covid vaccine slots!")

age = 19
pincodes= ["786001","786003","786004"]
print_flag = 'Y'
num_days = 7

actual = datetime.today()

list_format = [actual+ timedelta(days = i) for i in range(num_days)]

actual_dates = [i.strftime("%d%m%y") for i in list_format]

while True:
    counter = 0
    for pincode in pincodes:
        for given_date in actual_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode,given_date)
            header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/547.46 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36' }
            result = requests.get(URL, headers = header)
            #print(result.text)
            if result.ok:
                response_json = result.json()
                flag = False
                if response_json['centers']:
                    if (print_flag.lower() == 'y'):
                        for center in response_json['centers']:
                            #print(center)
                            for session in center['sessions']:
                                if (session['min_age_limit'] <=age and session['available_capacity']> 0):
                                    print("Pincode: " + pincode)
                                    print("Available on: {}".format(givendate))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ",center["fee_type"])
                                    print("\t Availability : ", session["vaccine"])
                                    print("\n")

                                    counter += 1
                                else:
                                    pass
                else:
                    pass
            else:       
                print("No response received!")
            
    if (counter == 0):
        print("No Vaccination slot avaliable!")
    else:
        email_msg = email.message.EmailMessage()
        email_msg["Subject"] = "Vaccination Slot Open"
        username = " yourEmail"
        password = "*****"
        email_msg["From"] = username
        email_msg["To"] = username
        email_msg.set_content(content)
        with smtplib.SMTP(host = 'smtp.gmail.com',port='587') as server:
            server.starttls()
            server.login(username,password)
            server.send_message(email_msg,username,username)
        print("Search Completed!")


    dt = datetime.now()+ timedelta(minutes= 3)

    while datetime.now() <dt:
        time.sleep(1)
