# fantasy-points
this script pulls data from Yahoo's Fantasy sports API and stores it in an excel sheet

You need Python 3.7 to run this code. It will not work with Python 2.X

This script uses the python wrapper [Yffpy](https://pypi.org/project/yffpy/) to pull data from Yahoo Fantasy Sports.

> ## Setting up an APP to get a Consumer Key and Secret (from Yffpy's guide)
    Log in to a Yahoo account with access to whatever fantasy football leagues from which you wish to retrieve data.
    Go to https://developer.yahoo.com/apps/create/ and create an app (you must be logged into your Yahoo account as stated above). For the app, select the following options:
        Application Name (Required): yffpy (you can name your app whatever you want, but this is just an example).
        Application Type (Required): select the Installed Application radio button.
        Description (Optional): you may write a short description of what the app does.
        Home Page URL (Optional): if you have a web address related to your app you may add it here.
        Redirect URI(s) (Required): this field must contain a valid redirect address, so you can use localhost:8080
        API Permissions (Required): check the Fantasy Sports checkbox. You can leave the Read option selected (appears in an accordion expansion underneath the Fantasy Sports checkbox once you select it).
        Click the Create App button.
        Once the app is created, it should redirect you to a page for your app, which will show both a Client ID and a Client Secret.
        Make a copy of examples/EXAMPLE-private.json, rename it to just private.json, and copy the Client ID and Client Secret values to their respective fields (make sure the strings are wrapped regular quotes (""), NOT formatted quotes (“”)). The path to this file will be needed to point YFFPY to your credentials.
        Now you should be ready to initialize the OAuth2 connection between YFFPY your Yahoo account.

## Packages
The following packages are used in my code:
```
import yffpy
from yffpy.query import YahooFantasyFootballQuery
import json
import openpyxl
from datetime import date
```
