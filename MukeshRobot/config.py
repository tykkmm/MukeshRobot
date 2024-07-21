class Config(object):
    LOGGER = True
    API_ID =29426486 
    API_HASH = "d71ad4ec048ab41677a1a439b21ff0c9"
    TOKEN = "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To"  
    OWNER_ID=5976437467
    
    SUPPORT_CHAT = "db" 
    START_IMG = "https://graph.org/file/eaa3a2602e43844a488a5.jpg"
    EVENT_LOGS = ()
    MONGO_DB_URI= "mongodb+srv://Arainanwar009:Ux955XkbkTntynx@cluster0.b1chu9a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "V48U2FLLKRHSVD4X""
    )
    TIME_API_KEY = "1CUBX1HXGNHW""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True