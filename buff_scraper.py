#----------------------------------------------------------------------------------------------------------------
# This project is archived. I will no longer be working on this and focus on something else.
# The project does work, one major bug though is the steamscraper, does not grab ALL items sadly. 
# It was too much work to fix that bug and I simply got bored. 
# follow me on twitter : @unemployy
#----------------------------------------------------------------------------------------------------------------


from forex_python.converter import CurrencyRates  # CURRENCYRATES
from steaminvenscraper import steamscraper
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

def pricegrabber(id):
    item_names = steamscraper(id)
    total_price = 0
    for i in range(len(item_names)):
        skin_name = item_names[i]
        skin_name_api = skintoURL(skin_name)
        url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1&search=' + skin_name_api
        user_cookies = { 'Cookie' : 'Device-Id=CtyanlFtuAPHkxQviGID; Locale-Supported=en; game=csgo; client_id=G0GAXVee2VnrxhG503W0UQ; session=1-6irez5Hvx9cOH8rsHZlNo1nfqCy_Qv80D0QYAxRcrHtj2044714143; csrf_token=IjJkOWE2NmY0ZmVhZDEwNDBlOGFhM2M0YzAzZDFkZjJhZTY3MWRmMmUi.E91Y0g.OhE2FH3wcQBVxqeHF9OPcEvQrPI'}
        buffAPIGrabber = requests.get(url, cookies=user_cookies)
        buffJSON = buffAPIGrabber.json() #API to JSON
        if (bool('StatTrak' in skin_name) == True):
            buff_price = buffJSON['data']['items'][1]['sell_min_price']
            buff_price_USD = str("%.2f" % float(CNYtoUSD(buff_price)))
        else:
            buff_price = buffJSON['data']['items'][0]['sell_min_price']
            buff_price_USD = str("%.2f" % float(CNYtoUSD(buff_price)))
        
        total_price = total_price + float(buff_price)
    
    return total_price


print(pricegrabber('76561198286217512'))

