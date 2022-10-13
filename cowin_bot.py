import requests
from datetime import datetime

base_cowin_portal = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
telegram_url="https://api.telegram.org/bot1833473459:AAFDmPxfqCemVq7uytsdYKQ5S1Tel_AxL3w/sendMessage?chat_id=@Cowin_Vaccine_Info&text="  
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")

dist = [269]

def fetch_data_for_state(dist_id):
    for i in dist_id:
        query_params = "?district_id={}&date={}".format(i,today_date)
        final_url = base_cowin_portal+query_params
        response = requests.get(final_url)
        response_json=response.json()
        for centre in response_json["centers"]:
            for session in centre["sessions"]:
                change = session["available_capacity"]
                if(session["available_capacity"]>0):
                    message = "District: {}\nPincode: {}\nCenter: {}\nAvailable-Doses: {}\nAge: {}\nFees: {}\nVaccine: {}\nDate: {}".format(centre["district_name"],centre["pincode"],
                    centre["name"], session["available_capacity"], session["min_age_limit"],centre["fee_type"],session["vaccine"],session["date"])
                    final_api=telegram_url+message
                    response=requests.get(final_api)
    
  

if __name__ == "__main__":
    fetch_data_for_state(dist)
