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
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        today = datetime.utcnow().strftime('%Y-%m-%d')
        filename = f"data/imgw_data_{today}.json"

        # Dołącz znacznik czasu do danych
        entry = {
            "timestamp": timestamp,
            "data": data
        }

        # Jeśli plik istnieje, wczytaj i dołącz dane
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.append(entry)

        # Zapisz zaktualizowaną listę
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)

        print(f"Appended data to {filename}")
    else:
        print(f"Failed to fetch data. Status: {response.status_code}")

if __name__ == "__main__":
    # Upewnij się, że katalog data/ istnieje
    if not os.path.exists('data'):
        os.makedirs('data')
    get_data()
