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
    response = requests.get(URL, stream=True)
    
    if response.status_code == 200:
        data = response.json()
        now = datetime.utcnow()
        date_str = now.strftime('%Y-%m-%d')  # np. '2025-08-01'
        timestamp_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')

        entry = {
            "timestamp": timestamp_str,
            "data": data
        }

        # Upewnij się, że folder 'data' istnieje
        os.makedirs("data", exist_ok=True)
        filename = f"data/imgw_data_{date_str}.json"

        # Jeśli plik istnieje, wczytaj go i dodaj dane
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                content = json.load(f)
        else:
            content = []

        content.append(entry)

        # Zapisz zaktualizowany plik
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)

        print(f"Appended data to {filename}")
    else:
        print(f"Failed to fetch data. Status: {response.status_code}")

if __name__ == "__main__":
    get_data()
