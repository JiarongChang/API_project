import requests
from data import Location
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'  # API網址
# 向html提出get請求
html_content = requests.get(url) # html的內容(物件) = 此網址 (呼叫get方法)
# 將內容轉為JSON
json_content = html_content.json() # json的內容(物件) = html的內容(物件)呼叫get方法 (將內容轉為json)
# print(json_content)

records = json_content.get('records')
location = records.get('location')
# print(location)  # location為一個list (網址第45行 https://jsoneditoronline.org/#right=local.juropo&left=local.laripu


# 取得欄位資料
'''for i in range(len(location)): #print出location 第一種方法
    print(location[i]) '''
locations = []  # list
for item in location:  # print(item) => print出location 的第二種方法
    # l = Location()  # Location類別
    # l.from_json(item)  # 呼叫data類別裡的from_jason方法
    # allocations.append(l)
    # print(l.__dict__)
    # print(allocations)

    # lat = item.get('lat')
    # lon = item.get('lon')
    # locationName = item.get('locationName')
    # stationId = item.get('stationId')
    # time = item.get('time')
    # obsTime = time.get('obsTime')
    # print(lat, lon, locationName, locationName, stationId, obsTime)

    location_site = Location()
    location_site.from_json(item)
    locations.append(location_site)

    # 取得觀測資料
    weatherElement = item.get('weatherElement')
    for element in weatherElement:
        elementName = element.get('elementName')
        elementValue = element.get('elementValue')
        print(elementName, elementValue)