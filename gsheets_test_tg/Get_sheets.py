import os

from pandas.core.frame import DataFrame
from Google import Create_Service
import pandas as pd
from pprint import  pprint

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# https://docs.google.com/spreadsheets/d/1C8DdA4XTDJvG_tYlxQihxGO1QOZIdYIaDENUmLcHOqs

def get_sheets(student_id:str, subject="Precalculus"):
    precalculus_id = "1LI8mlPVmpbBePB0lUA7imnJo_Kql4JvaD6q4ovXKK_8"
    indexes = "A3:AN99"
    service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


    #    test attendence 
    work_sheet = subject
    response1 = service.spreadsheets().values().get(
        spreadsheetId=precalculus_id,
        majorDimension="ROWS",
        range=f"{work_sheet}!{indexes}"

    ).execute()


    print(student_id)

    # colomns = response1['values'][0]
    # data = response1['values'][1:]
    # df = pd.DataFrame(data, columns=columns
    for item in response1['values'][1:]:
        for n in item:
            if n == student_id:   
                print(item[:8])
                data = item[1:8]


    info=f"ID: {data[0]}\n"
    info+=f"Name: {data[1]}\n"
    info+=f"Surename: {data[2]}\n"
    info+=f"Email: {data[3]}\n"
    info+=f"Group: {data[4]}\n"
    info+=f"Department: {data[5]}\n"
    info +=f"Absences: {data[6]}\n"
    return info
