import requests
import time
from datetime import datetime,timedelta
import json
import smtplib


print("Starting search for covid vaccine slots!")

age = 
pincodes= [" "]
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
                                    s = smtplib.SMTP('smtp.gmail.com',587)
                                    sender= " "
                                    s_password = " "
                                    
                                    receivers = [""]
    
                                    msg= "Vaccination slot available"

                                    for receiver in receivers:
                                        s.ehlo()
                                        s.starttls()
                                        s.login(sender,s_password)
                                        s.sendmail(sender,receiver,msg)
                                        s.quit()
                                        
                                    counter += 1
                                    
                                else:
                                    pass
                else:
                    pass
            else:       
                pass
            
    if (counter == 0):
        print("No Vaccination slot avaliable!")
    else:
        
        pass


    dt = datetime.now()+ timedelta(minutes= 3)

    while datetime.now() <dt:
        time.sleep(1)
