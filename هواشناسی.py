import requests, json

#result = requests.get("http://google.com")

#print(result.status_code)

api_key ="262da15423dbf58509e16e84b438fa2f"

bace_url ="https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name:")

complete_url = bace_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

print(complete_url)


response = requests.get(complete_url)

x = response.json()

print(x)

#print(x['cod'])