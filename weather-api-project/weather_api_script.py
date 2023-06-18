import requests

#grab API key here: https://openweathermap.org/forecast5
#it may take 2 hours for API key activation

def get_weather(city, units='metric', api_key='b5750a9aa46acd894ae7e46bab92fe71'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for item in content['list']:
            # print(item['dt_txt'], item['main']['temp'], item['weather'][0]['description'])
            # the above line just prints the weather forecast on command line, below we write to a data.txt file
            file.write(f"{item['dt_txt']}, {item['main']['temp']}, {item['weather'][0]['description']}\n")

print(get_weather(city='San Francisco'))