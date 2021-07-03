# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from datetime import datetime

base_cowin_url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
now=datetime.now();
today_date=now.strftime("%d-%m-%Y")
api_url_telegram="https://api.telegram.org/bot1864942825:AAG55MNmAsxanEEDLeyl8owwoAVMsvMUGtw/sendMessage?chat_id=@__groupid__&text="
group_id="demo_telegram_cowin_up"
up_district_ids=[622, 623, 625, 626, 627, 628, 629, 646, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 687, 640,
                 641, 642, 643, 644, 645, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664,
                 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 682, 624, 681, 683, 684, 685, 686,
                 688, 689, 690, 691, 692, 693, 694, 695, 696]

def fetch_data_from_cowin(district_id):
    query_params="?district_id={}&date={}".format(district_id, today_date)
   

    final_url=base_cowin_url+query_params
    response=requests.get(final_url)
    extract_availability_data(response)
    #print(response.text)
    
def fetch_data_for_state(district_ids):
    for district_id in district_ids:
        fetch_data_from_cowin(district_id)
        
def extract_availability_data(response):
    response_json=response.json()
  
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose2"] > 0 and session["min_age_limit"]==18:
                message="Pincode: {}, Name: {}, Slots: {}, Minimum Age: {}".format(
                    center["pincode"], center["name"], session["available_capacity_dose2"],
                    session["min_age_limit"])
                send_message_telegram(message)
            
def send_message_telegram(message):
    final_telegram_url=api_url_telegram.replace("__groupid__", group_id)
    final_telegram_url=final_telegram_url+message
    response=requests.get(final_telegram_url)
    print(response)       
      
    
if __name__=="__main__":
    fetch_data_for_state(up_district_ids)
