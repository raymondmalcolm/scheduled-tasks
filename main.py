# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import random
import datetime as dt
import smtplib
import pandas as pd
from pathlib import Path

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL:")

my_email = MY_EMAIL
password = MY_PASSWORD
to_email = TO_EMAIL

now = dt.datetime.now()
day_of_week = now.weekday()
#print(day_of_week)

# 2. Check if today matches a birthday in the birthdays.csv

directory_path = Path('letter_templates')
letters = []

try:
    df  = pd.read_csv("birthdays.csv")
    birthday_dict = df.to_dict(orient='records')
except FileNotFoundError:
    print("File not found.")

# iterate over directory items and filter for files
for file_path in directory_path.iterdir():
    if file_path.is_file():
        with file_path.open('r', encoding='utf-8') as f:
            letters.append(f.read())

for birthday in birthday_dict:
    if int(birthday["Month"]) == now.month and int(birthday["Day"]) == now.day:
        letter = random.choice(letters)
        letter = letter.replace("[NAME]", birthday["Name"])

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=birthday["Email"], 
                                msg=f"Subject:Happy Birthday\n\n{letter}"

        )




