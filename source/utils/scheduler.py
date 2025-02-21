import os
import schedule
import time
import subprocess
from utils.api.worker import UpdateFuelPrice

def CheckFuelPrices():
    try:
        UpdateFuelPrice()
        print('task 1 ran')

    except Exception as error:
        print(f'[Scheduler Error] {error}.')

def CheckForUpdates():
    try:
        script_path = os.path.join(os.getcwd(), "bash", "update.sh")

        subprocess.run(["bash", script_path], check=True)
        print('task 2 ran')

    except Exception as error:
        print(f'[Scheduler Error] {error}.')

schedule.every().day.at("23:59").do(CheckFuelPrices)
schedule.every().day.at("23:59").do(CheckForUpdates)

while True:
    schedule.run_pending()
    time.sleep(20)
