import schedule
import os
import shutil
import datetime
import time

source_dir= "/Users/hrrniu"
destination_dir= "/Users/hrrniu/Filmy"

def copy_folder_to_directory(source,dest):
    today= datetime.date.today()
    dest_dir= os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistError:
        print(f"Folder already exsist in: {dest}")
def l():

schedule.every().day.at("06:55").do(Lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)