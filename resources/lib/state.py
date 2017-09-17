# -*- coding: utf-8 -*-
# THREAD SAFE

# Quit PKC
STOP_PKC = False


# Usually triggered by another Python instance - will have to be set (by
# polling window) through e.g. librarysync thread
SUSPEND_LIBRARY_THREAD = False
# Set if user decided to cancel sync
STOP_SYNC = False
# Could we access the paths?
PATH_VERIFIED = False
# Set if a Plex-Kodi DB sync is being done - along with
# window('plex_dbScan') set to 'true'
DB_SCAN = False
# Plex Media Server Status - along with window('plex_serverStatus')
PMS_STATUS = False
# When the userclient needs to wait
SUSPEND_USER_CLIENT = False
# Plex home user? Then "False". Along with window('plex_restricteduser')
RESTRICTED_USER = False
# Direct Paths (True) or Addon Paths (False)? Along with
# window('useDirectPaths')
DIRECT_PATHS = False
# Shall we replace custom user ratings with the number of versions available?
INDICATE_MEDIA_VERSIONS = False
# Do we need to run a special library scan?
RUN_LIB_SCAN = None

# Stemming from the PKC settings.xml
# Shall we show Kodi dialogs when synching?
SYNC_DIALOG = True
# Have we already checked the Kodi DB on consistency?
KODI_DB_CHECKED = False
# Is synching of Plex music enabled?
ENABLE_MUSIC = True
# How often shall we sync?
FULL_SYNC_INTERVALL = 0
# Background Sync enabled at all?
BACKGROUND_SYNC = True
# How long shall we wait with synching a new item to make sure Plex got all
# metadata?
BACKGROUNDSYNC_SAFTYMARGIN = 0
# How many threads to download Plex metadata on sync?
SYNC_THREAD_NUMBER = 0
# What's the time offset between the PMS and Kodi?
KODI_PLEX_TIME_OFFSET = 0.0

# Path remapping mechanism (e.g. smb paths)
# Do we replace \\myserver\path to smb://myserver/path?
REPLACE_SMB_PATH = False
# Do we generally remap?
REMAP_PATH = False
# Mappings for REMAP_PATH:
remapSMBmovieOrg = None
remapSMBmovieNew = None
remapSMBtvOrg = None
remapSMBtvNew = None
remapSMBmusicOrg = None
remapSMBmusicNew = None
remapSMBphotoOrg = None
remapSMBphotoNew = None

# Along with window('plex_authenticated')
AUTHENTICATED = False
# plex.tv username
PLEX_USERNAME = None
# Token for that user for plex.tv
PLEX_TOKEN = None
# Plex ID of that user (e.g. for plex.tv) as a STRING
PLEX_USER_ID = None
# Token passed along, e.g. if playback initiated by Plex Companion. Might be
# another user playing something! Token identifies user
PLEX_TRANSIENT_TOKEN = None
