from forex_python.converter import CurrencyRates  # CURRENCYRATES
#from steaminvenscraper import steamscraper
import requests  # REQUEST MODULE TO GET WEBSITE HTML

# converting RMB to USD
def CNYtoUSD(rmbPrice):
    c = CurrencyRates()
    rmbPrice = c.convert('CNY', 'USD', float(rmbPrice))
    return rmbPrice

def skintoURL(skinName):
    skinName = skinName.replace(' ', '+')
    skinName = skinName.replace('|', '%7C')
    return skinName

skin_name = '★ Bowie Knife | Doppler (Factory New)'
skin_name_api = skintoURL('★ Bowie Knife | Doppler (Factory New)')
url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1&search=' + skin_name_api
user_cookies = { 'Cookie' : ''}
buffAPIGrabber = requests.get(url, cookies=user_cookies)
buffJSON = buffAPIGrabber.json() #API to JSON
if (bool('StatTrak' in skin_name) == True):
    buff_price = buffJSON['data']['items'][1]['sell_min_price']
    buff_price_USD = str("%.2f" % float(CNYtoUSD(buff_price)))
else:
    buff_price = buffJSON['data']['items'][0]['sell_min_price']
    buff_price_USD = str("%.2f" % float(CNYtoUSD(buff_price)))

# Printing Results
print(skin_name)
print(buff_price +' ¥ '+ buff_price_USD + ' $')
