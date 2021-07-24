import requests
import json

def steamscraper(id):
    item_names = []
    steamURL = 'https://steamcommunity.com/inventory/' + id + '/730/2?l=english&count=5000'
    steamAPI = requests.get(steamURL)
    steamAPIParsed = steamAPI.json()
    current_class_id = None
    x = None
    duplicate_dict = {}

    #Checking for duplicates by using class id.
    for z in range(len(steamAPIParsed['assets'])): #30
        x = 0
        current_class_id = steamAPIParsed['assets'][z]['classid']
        for h in range(len(steamAPIParsed['assets'])):
            if current_class_id == steamAPIParsed['assets'][h]['classid']:
                x = x + 1
                duplicate_dict[steamAPIParsed['assets'][h]['classid']] = x


    for i in range(len(steamAPIParsed['descriptions'])):
        item_names.append(steamAPIParsed['descriptions'][i]['market_hash_name'])

    key_list = list(duplicate_dict.keys())
    val_list = list(duplicate_dict.values())
    classid_list = []
    classid_list_counter = []
    # Using classid to find "market_hash_name of such class id's and then adding the name depending on how much times the classid has been repeated.
    for i in range(len(val_list)):
        if val_list[i] > 1:
            classid_list.append(key_list[i])
            classid_list_counter.append(val_list[i])

    for i in range(len(classid_list)):
        for o in range(len(steamAPIParsed['descriptions'])):
            if(steamAPIParsed['descriptions'][o]['classid'] == classid_list[i]):
                    item_names.append(steamAPIParsed['descriptions'][o]['market_hash_name'])

    return item_names
