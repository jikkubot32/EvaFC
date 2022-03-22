import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 3937220
API_HASH = 'a4de4c3e683bfdf30b5781142e0d41f2'
BOT_TOKEN = '5096921899:AAHN8eExI_fhmzWY7cD-7tM_kX58u8QoP8o'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/c774cca7f44d3464ae76b.jpg https://telegra.ph/file/79f50dfea4f89d8604c66.jpg https://telegra.ph/file/86d6169df8c962443eeef.jpg https://telegra.ph/file/729d2a137e53421078b74.jpg https://telegra.ph/file/7f04250a4942fa40b6e68.jpg https://telegra.ph/file/fe22c628729a025703508.jpg https://telegra.ph/file/992034ee054d01d25065b.jpg https://telegra.ph/file/efc96314636379b2e6567.jpg https://telegra.ph/file/30505152d21d586835655.jpg https://telegra.ph/file/0013942adb9ec0c73617a.jpg https://telegra.ph/file/d8dd013ce917cf429a015.jpg https://telegra.ph/file/e02a8c7453d0f375be101.jpg https://telegra.ph/file/d3ada756d0c874aa73e95.jpg https://telegra.ph/file/4f1743c359b75799be337.jpg https://telegra.ph/file/5e243a1a709156e0260d1.jpg https://telegra.ph/file/e6e37eeb762d114c8f5a0.jpg https://telegra.ph/file/489d90e0526b29e47a214.jpg https://telegra.ph/file/bc0c6d6a5733272bc7bd8.jpg https://telegra.ph/file/d65a01adc67ac25ec0cb1.jpg https://telegra.ph/file/0f0284b60638d98eb5d50.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '658905997').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001484884182 -1001172622040 -1001280478789').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001157840306')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Telegram:Telegram@cluster0.ahnw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001501315486))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'FilmClubChannel')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = "<code>{file_name}</code>

<b>Size: <code>{file_size}</code></b>

<b>© Powered by [FilmClubChannel](https://t.me/FilmClubChannel) </b>"
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🏷 Title</b>: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)\n☀️ Languages : <code>{languages}</code>\n👥 Cast : <code>{cast}</code>\n📀 RunTime: {runtime} Minutes\n📆 Release Info : {release_date}\n🎛 Countries : <code>{countries}</code>\n👥 Requested By :  {message.from_user.mention}\n🌐 Channel : @FilmClubChannel\n\n© {message.chat.title} </b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("4", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
