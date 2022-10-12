import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred():
    BOT_TOKEN = ""
    API_ID = 1390245    
    API_HASH = "a021871c10d820e0bb7a5d0e999d8c7f"
    DB_URL = "https://truecallerbot-fe076-default-rtdb.firebaseio.com/"

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = os.getenv("T_AUTH")      # Truecaller auth id CA
    E_AUTH = os.getenv("E_AUTH")      # Eyecon auth id
    E_AUTH_V=os.getenv("E_AUTH_V")    # Eyecon auth_v
    E_AUTH_C=os.getenv("E_AUTH_C")    # Eyecon auth_c
