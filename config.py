from os import environ

API_ID = int(environ.get("API_ID", "25588319"))
API_HASH = environ.get("API_HASH", "5972c23e4a53fb0f92d8bec8942833c0")
BOT_TOKEN = environ.get("BOT_TOKEN", "7827847503:AAGCDMvqFdtXonXcu4Lh4OZqqI2XGZykXc4")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002418271487"))
ADMINS = int(environ.get("ADMINS", "6016330931"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI","mongodb+srv://akhashalderssss:WdiXao3jkdlVB1Xn@cluster0.sfo2z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
