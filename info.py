# Bot information
SESSION = 'Media_search'
API_ID = 3937220
API_HASH = 'a4de4c3e683bfdf30b5781142e0d41f2'
BOT_TOKEN = '5096921899:AAHN8eExI_fhmzWY7cD-7tM_kX58u8QoP8o'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = True
PICS = 'https://telegra.ph/file/c774cca7f44d3464ae76b.jpg https://telegra.ph/file/79f50dfea4f89d8604c66.jpg https://telegra.ph/file/86d6169df8c962443eeef.jpg https://telegra.ph/file/729d2a137e53421078b74.jpg https://telegra.ph/file/7f04250a4942fa40b6e68.jpg https://telegra.ph/file/fe22c628729a025703508.jpg https://telegra.ph/file/992034ee054d01d25065b.jpg https://telegra.ph/file/efc96314636379b2e6567.jpg https://telegra.ph/file/30505152d21d586835655.jpg https://telegra.ph/file/0013942adb9ec0c73617a.jpg https://telegra.ph/file/d8dd013ce917cf429a015.jpg https://telegra.ph/file/e02a8c7453d0f375be101.jpg https://telegra.ph/file/d3ada756d0c874aa73e95.jpg https://telegra.ph/file/4f1743c359b75799be337.jpg https://telegra.ph/file/5e243a1a709156e0260d1.jpg https://telegra.ph/file/e6e37eeb762d114c8f5a0.jpg https://telegra.ph/file/489d90e0526b29e47a214.jpg https://telegra.ph/file/bc0c6d6a5733272bc7bd8.jpg https://telegra.ph/file/d65a01adc67ac25ec0cb1.jpg https://telegra.ph/file/0f0284b60638d98eb5d50.jpg'

# Admins, Channels & Users
ADMINS = [658905997]
CHANNELS = [-1001484884182, -1001172622040, -1001280478789]
AUTH_USERS = []
AUTH_CHANNEL = -1001157840306
AUTH_GROUPS = [] 

# MongoDB information
DATABASE_URI = "mongodb+srv://Telegram:Telegram@cluster0.ahnw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Telegram"
COLLECTION_NAME = 'Telegram_files'

# Others
LOG_CHANNEL = -1001501315486
SUPPORT_CHAT = 'FilmClubChannel'
P_TTI_SHOW_OFF = "True"
IMDB = "True"
SINGLE_BUTTON = "True"
CUSTOM_FILE_CAPTION = "<code>{file_name}</code>\n\n<b>Size: <code>{file_size}</code></b>\n\n<b>© Powered by [FilmClubChannel](https://t.me/FilmClubChannel) </b>" 
IMDB_TEMPLATE = "<b>🏷 Title</b>: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)\n☀️ Languages : <code>{languages}</code>\n👥 Cast : <code>{cast}</code>\n📀 RunTime: {runtime} Minutes\n📆 Release Info : {release_date}\n🎛 Countries : <code>{countries}</code>\n👥 Requested By :  {message.from_user.mention}\n🌐 Channel : @FilmClubChannel\n\n© {message.chat.title} </b>"
LONG_IMDB_DESCRIPTION = "False"
SPELL_CHECK_REPLY = "True"
MAX_LIST_ELM = "4"
INDEX_REQ_CHANNEL = -1001501315486

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
