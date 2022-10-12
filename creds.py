import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred():
    BOT_TOKEN = ""
    API_ID = 1390245    
    API_HASH = "a021871c10d820e0bb7a5d0e999d8c7f"
    DB_URL = "https://truecallerbot-fe076-default-rtdb.firebaseio.com/"

    ####From Truecaller and Eyecon app request headers respectively########

    T_AUTH = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjgyNDE0OTQ4MzMsInRva2VuIjoiYTF3MGctLWI3cU9aZGt5LXl3MmtRRENEdFpIdEZmcmlUeGs4eHN6Rl9iS0Jqbll0ODlCeUt1bkdQNlhndzF6byIsImVuaGFuY2VkU2VhcmNoIjp0cnVlLCJjb3VudHJ5Q29kZSI6ImV0IiwibmFtZSI6Ik5vbWEgTnciLCJlbWFpbCI6Im5vbWFudzUxMEBnbWFpbC5jb20iLCJpbWFnZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FMbTV3dTEwa0pzSFJDNlBENnRjQVQyNFBucnFKRDJtNG1CekloZHVlOExmPXM5Ni1jIiwiaWF0IjoxNjY1NTYzMDk0fQ.C82D2EiUwG5UdC9geAM350mlbzLkrb-c6htf_dWJ5GI"     # Truecaller auth id CA
    E_AUTH = os.getenv("E_AUTH")      # Eyecon auth id
    E_AUTH_V=os.getenv("E_AUTH_V")    # Eyecon auth_v
    E_AUTH_C=os.getenv("E_AUTH_C")    # Eyecon auth_c
