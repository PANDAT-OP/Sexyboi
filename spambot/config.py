import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN1 = "5704604379:AAFflEwCQbcSPu83i8GNIpnufXOCo-igkJY"
    BOT_TOKEN2 = "5784094880:AAFBOu2RFotz4DVPcTIzSpWGKkW-IlLo56E"
    BOT_TOKEN3 = "6103984321:AAFjxzCW7-WLma_KRr3c8OhOtbHr4ijv05U"
    BOT_TOKEN4 = "6091887039:AAHwDxhJm7Ic-tnoq1dQTypGQyADIEdRHwE"
    BOT_TOKEN5 = "6154116526:AAHRbpdqj67msZnOuDoRPGQu0rWA8t_plvA"
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    OWNER_NAME = os.environ.get("OWNER_NAME", None)
    OWNER_USERNAME =os.environ.get("OWNER_USERNAME", None)
    CO_OWNER_ID = set(int(x) for x in os.environ.get("CO_OWNER_ID", None).split())
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", None).split())
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_ID", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    DISPLAY_PIC = os.environ.get("DISPLAY_PIC", None)
    BIO_MSG =  os.environ.get("BIO_MSG", None)
