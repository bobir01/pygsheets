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
service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


# A3:AN99  precalculus 
attendence = "1LI8mlPVmpbBePB0lUA7imnJo_Kql4JvaD6q4ovXKK_8"


spreadsheet_id = "1C8DdA4XTDJvG_tYlxQihxGO1QOZIdYIaDENUmLcHOqs"
"""
wrapping singlr cell's data 
"""
# worksheet = "Sheet1"
# response = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     majorDimension="ROWS",
#     range='A1:D10'
indexes = "A3:AN99"
# ).execute()

# # pprint(response)
# # pprint(response['values'])
# # print(response.keys())
# columns = response['values'][0]
# data = response['values'][1:]
# df = pd.DataFrame(data, columns=columns)

# print(df)
# # example of getting full tables 
# response1 = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     majorDimension="ROWS",
#     range=worksheet

# ).execute()

# # pprint(response1['values'])
# df1 =pd.DataFrame(data, columns=columns)
# print(df1)


#    test attendence 
work_sheet = "Precalculus"
response1 = service.spreadsheets().values().get(
    spreadsheetId=attendence,
    majorDimension="ROWS",

    range=f"{work_sheet}!{indexes}"

).execute()

student_id = response1['values'][2][5]
print(student_id)

# colomns = response1['values'][0]
# data = response1['values'][1:]
# df = pd.DataFrame(data, columns=colomns)

bobir = "21SE068"
# print(df)
# range(len(response1['values'][1:]))
for item in response1['values'][1:]:
    for n in item:
        if n == bobir:   
            print(item[:8])
            data = item[1:8]


info=f"ID {data[0]}\n"
info+=f"Name {data[1]}\n"
info+=f"Surename {data[2]}\n"
info+=f"email {data[3]}\n"
info+=f"group {data[4]}\n"
info+=f"department {data[5]}\n"
info +=f"absences {data[6]}\n"

print(info)

