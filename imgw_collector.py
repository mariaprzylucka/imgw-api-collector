# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 11:56:28 2025

@author: msur
"""

import requests
import json
import os
from datetime import datetime

URL = "https://danepubliczne.imgw.pl/api/data/meteo/"

def get_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    response = requests.get(URL, stream=True)
    
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%SZ')
        filename = f"data/imgw_data_{timestamp}.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {filename}")
    else:
        print(f"Failed to fetch data. Status: {response.status_code}")

if __name__ == "__main__":
    get_data()
