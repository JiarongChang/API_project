class Location:
    def __init__(self, location_name=None, lat=None,
                 lon=None, station_id=None, time=None, weather_element=None):
        self.location_name = location_name  # 取一樣的物件名稱，但前面的location_name 不等於後面的location_name
        self.lat = lat
        self.lon = lon
        self.station_id = station_id
        self.time = time
        self.weather_element = weather_element


    # 傳入JSON資料，設定屬性的值
    def from_json(self, json_data):
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.location_name = json_data.get('locationName')
        self.station_id = json_data.get('stationId')
        time1 = json_data.get('time')
        self.time = time1.get('obsTime')

        # 新增解析weatherElement
        self.weatherElement = weatherElement()
        self.weatherElement.from_json(json_data['weatherElement'])


class weatherElement:
    def __init__(self, wdir=None, wdsd=None,
                 temp=None, humd=None, h24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h24r = h24r

    # 傳入JSON資料，設定屬性的值
    def from_jason(self, weather_element):
        for element in weather_element:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')

            if element_name == 'WDIR':
                self.wdir = element_value

            if element_name == 'WDSD':
                self.wdsd = element_value

            if element_name == 'TEMP':
                self.temp = element_value

            if element_name == 'HUMD':
                self.humd = element_value

            if element_name == '24R':
                self.h24r = element_value
