import re, requests, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

user = input("masukan id : ")
pw = input("masukan sandi : ")

url = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
parsing = parser(url.text,"html.parser")
action = parsing.find("form",{"method":"post"})["action"]
headers = {
	"Host": "m.facebook.com",
	"connection":"keep-alive",
	"cache-control": "max-age=0",
	"save-data": "on",
	"origin": "https://m.facebook.com",
	"content-type": "application/x-www-form-urlencoded",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"dnt": "1",
	"sec-ch-ua": "' Not A;Brand';v='99', 'Chromium';v='99'",
	"sec-ch-ua-mobile":"?1",
	"sec-ch-ua-platform":"'Android'",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"upgrade-insecure-requests":"1",
	"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5",
	"referer": f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
data = {
	"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),
	"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
	"uid":user,
	"flow":"login_no_pin",
	"pass": pw,
	"next": "https://m.facebook.com/login/save-device/"}
post = ses.post("https://m.facebook.com"+action, data=data, headers=headers)
if "c_user" in ses.cookies.get_dict():
	print("akun ok")
elif "checkpoint" in ses.cookies.get_dict():
	print("akun cp")
else:
	print("kata sandi salah")

