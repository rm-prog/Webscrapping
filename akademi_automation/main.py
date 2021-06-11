import time
import datetime
from functions import open_zoom
    

# <----------------- Links for online classes ---------------------------->    
kimi_link = "https://app.akademi.al/course/_student/d316df2a-4bd0-4294-8e43-f94744bacbdb"
biologji_link = "https://app.akademi.al/course/_student/7178b586-5493-4d1f-bfbb-5c4a3806103d"
tik_link = "https://app.akademi.al/course/_student/821a6c1f-e18c-4c5c-80ec-43a81a8b352c"
mat_link = "https://app.akademi.al/course/_student/e9655e11-8457-4003-8b7d-05a4189aba07"
fizik_link = "https://app.akademi.al/course/_student/dbef756f-96dd-45e6-8cfd-955bed271df4"
anglisht_link = "https://app.akademi.al/course/_student/2bf8d3a8-3619-4d38-bee7-f882b633402a"
gjeo2_link = "https://app.akademi.al/course/_student/91edcbf9-82d7-4510-8c69-5b058dfa06c1"
gjeo1_link = "https://app.akademi.al/course/_student/ef9aa300-6fa7-41c4-b3e1-790e3789cbd5"
frengjisht_link = "https://app.akademi.al/course/_student/692e89e7-ca41-4fdb-8e22-dc788a201664"
gjuhe_link = "https://app.akademi.al/course/_student/08c1ea4d-c688-4401-88d7-21439f8cec81"
letersi_link = "https://app.akademi.al/course/_student/b72abc52-833e-461e-a6dc-e4f55cb2995e"
histori_link = "https://app.akademi.al/course/_student/04db553d-6409-42b7-bcc3-1446e0da389f"
filozofi_link = "https://app.akademi.al/course/_student/44fc3be3-4f87-42e8-8e93-22fff11ef2f4"
fiskulture_link = "https://app.akademi.al/course/_student/0f831d9f-d3c0-4475-8c2f-840dc7942672"


day_of_week = datetime.datetime.today().weekday()

# <---------------------- Check day of the week and the hour ------------------------>
# <---------------------- Pass the class links corresponding to the day of the week
def start_lesson():
    if day_of_week == 0:
        if datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
            open_zoom(anglisht_link, gjeo1_link, histori_link)            
    if day_of_week == 1:
        if datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
            open_zoom(mat_link, kimi_link, filozofi_link)            
    if day_of_week == 2:
        if datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
            open_zoom(letersi_link, fizik_link, biologji_link)            
    if day_of_week == 3:
        if datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
            open_zoom(mat_link, fiskulture_link, fizik_link)            
    if day_of_week == 4:
        if datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
            cift_tek = int(input("Tik apo anglisht (1, 2)"))
            if cift_tek == 1: open_zoom(gjuhe_link, tik_link, frengjisht_link)   
            else: open_zoom(gjuhe_link, anglisht_link, frengjisht_link)         


if __name__ == "__main__":
    while datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13: 
        start_lesson()
        time.sleep(60)