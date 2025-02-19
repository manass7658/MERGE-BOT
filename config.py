import os


class Config(object):
    API_HASH = os.environ.get("627b314d25c83e2c9a1a99db9ae0a3ef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ.get("27857521")
    OWNER = os.environ.get("7024087501")
    OWNER_USERNAME = os.environ.get("@itsshadowslayer")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("mongodb+srv://manashsuhoo77:4Hptt83gAdyhdtL5@cluster0.umagl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002475020860")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
