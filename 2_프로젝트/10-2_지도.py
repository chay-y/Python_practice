import requests

url = 'http://api.vworld.kr/req/address?'
params ='service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'  #도로명주소
road_type2 = 'PARCEL'   #지번주소
address = '&address='
keys = '&key='
primary_key = ' ' #보안키

def request_geo(road):

    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data=page.json()

    # 응답의 상태가 ok인 경우 -> 요청에 대해 응답을 정상적으로 받았으면
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x,y
    else:
        x = 0
        y = 0
        return x,y
    
x,y=request_geo("강원도 원주시 흥업면 남원로 150 (흥업리, 강릉원주대학교원주캠퍼스)")

print(f'x값: {x}')
print(f'y값: {y}')