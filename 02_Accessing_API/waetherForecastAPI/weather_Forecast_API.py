import requests

def get_temp(city, api_key = '3b062dc13d761435698c8ad0d8b30001'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

get_temp(city='London')