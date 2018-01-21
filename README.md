# PiLapse
Timelapse setup for a RaspberryPi

A collection of scripts used to make timelapse videos using `raspistill`.
Uploads created videos to Google Drive and Youtube using pythong Google API client.

Picture taking is set up as a cron job.

# Authentication:
    1. Create credentials at https://console.developers.google.com/apis/credentials (following https://developers.google.com/drive/v3/web/quickstart/python)

    2. Put the client_secret.json file in `~/.creds` (make the dir if it doesn't exist)

    3. from `~` (`cd ~`) call `python PiLapse/google_api/credentials/create_credentials.py  ~/.creds/client_secret.json APP_NAME  --noauth_local_webserver`

    You will be promted to go to a URL, give the application permissions from your account and copy and paste a code back to the terminal.

    Credentials are generated!


# Seting up the cronjob


