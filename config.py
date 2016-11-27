from datetime import timedelta

# Lite mode:
# If lite is enabled, all user database related functions are disabled.
# /stalk, /im, /whois /levels are disabled
# /whois, /deaths have limited functionality
# Level up and deaths announcements are disabled
lite_mode = False

# This is the name of the server where the bot will work
# This bot doesn't support multiple servers yet
# mainchannel is where the Bot will do announcements, but he will reply to commands everywhere
# askchannel is a channel where the bot replies with full length messages (like on pms)
#   Messages that are not commands are automatically deleted in askchannel
mainserver = "Redd Alliance/Bald Dwarfs"
mainchannel = "general-chat"
askchannel = "ask-nabbot"

# It's possible to fetch the database contents on a website to show more entries than what the bot can display
# If enabled, certain commands will link to the website
siteEnabled = True
baseUrl = "http://galarzaa.no-ip.org:7005/ReddAlliance/"
charactersPage = "characters.php"
deathsPage = "deaths.php"
levelsPage = "levels.php"

# Discord id for the users that can use admin or mod commands
owner_ids = ["162060569803751424", "162070610556616705", "164253469912334350", "159815675194507265"]
mod_ids = ["164253469912334350", "159815675194507265"]
# Enable of disable specific timezones for /time
displayBrasiliaTime = True
displaySonoraTime = True

# The list of servers to check for with getServerOnline
tibiaservers = ["Fidera"]

# Time since joining until the bot will ignore /im from an user. (See: /im in nabbot.py)
# Note that an user can simply rejoin the server to reset his join date, but that will trigger a log message.
timewindow_im_joining = timedelta(days=3)

# This is the global online list
# don't look at it too closely or you'll go blind!
# characters are added as servername_charactername and the list is updated periodically on think() using getServerOnline()
globalOnlineList = []

# Level threshold for announces (level < announceLevel)
announceTreshold = 30

# Minimum days to show last login in /check command.
last_login_days = 7

# Delay inbreed server checks
serveronline_delay = timedelta(seconds=25)

# Delay in between player death checks
playerdeath_delay = timedelta(seconds=15)

# Databases filenames
USERDB = "users.db"
TIBIADB = "Database.db"

if __name__ == "__main__":
    input("To run NabBot, run nabbot.py")
