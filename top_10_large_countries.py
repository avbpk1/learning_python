import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")

if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit(1)

countries = resp.json()
# Top 10 countries by area

f"Country                                         Population"
print(f"-------                                         ----------" )
for country in sorted(countries, key=lambda c: (c['area'] if c['area'] else 0), reverse=True)[:10]:
    print(f"{country['name']:50}  {country['area']:8.0f}")
# Top 10 countries by population density
print(f"-------                                         ----------" )
print(f"Country                                         Density" )
print(f"-------                                         -------" )
for country in sorted(countries, key=lambda c: ((c['population'])/(c['area']) if c['area'] else 0), reverse=True)[:10]:
    density = country['population']//country['area']
    print(f"{country['name']:50}  {int(density):8.0f}")