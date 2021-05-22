import requests
import json
from datetime import datetime, timedelta
import time


age = 22

pinCodes = ["722101"]   ## Here you can make a list of pincodes

print_flag = 'Y'


numdays = 2

base = datetime.today()
date_list = [base + timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

while 1:

    count = 0
    
    print("Searching for centers...")
    time.sleep(3)

    for pinCode in pinCodes:   
        print(pinCode) 
        for INP_DATE in date_str:
            print("\t", INP_DATE)
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode, INP_DATE)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
            response = requests.get( URL, headers=headers )

           
            if response.ok:
                resp_json = response.json()
                
                flag = False
                if resp_json["centers"]:            
                    if(print_flag=='y' or print_flag=='Y'):
                        for center in resp_json["centers"]:
                            
                            #print(center)
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                    print(pinCode)
                                    print("Available on: {}".format(INP_DATE))
                                    print("\t\t", center["name"])
                                    print("\t\t", center["block_name"])
                                    print("\t\t Price: ", center["fee_type"])
                                    print("\t\t Available Capacity: ", session["available_capacity"])
                                    if(session["vaccine"] != ''):
                                        print("\t\t Vaccine Type: ", session["vaccine"])
                                    print("\n")
                                    
                                    count = count + 1
                                else:
                                    b = 25
                                    
                else:
                    a = 25
                   
            else:
                print("Program is not responding")
    if(count == 0):
        print("Currently no slots are available. Check later.")
    else:
        print("Searching Finished!")

        
    

    dt = datetime.now() + timedelta(minutes=3)
    #dt = dt.replace(minute=1)

    while datetime.now() < dt:

        time.sleep(1)
