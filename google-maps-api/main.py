import googlemaps

# Reemplaza 'YOUR_GOOGLE_MAPS_API_KEY' con tu propia clave de API de Google Maps
api_key = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=api_key)

# Lista de cafeterías
cafeterias = [
    "Café Berlin Valencia",
    "Ubik Café Valencia",
    "La Ola Fresca Valencia",
    "Pub Big Ben Valencia",
    "Café de las Horas Valencia",
    "Radio City Valencia",
    "St. Patrick’s Valencia Irish Pub",
    "Upper Club Valencia",
    "Espai Solidaria Valencia",
    "L’Ermità Café Valencia"
]


# Función para obtener detalles de un lugar
def get_place_details(place_name):
    place = gmaps.places(query=place_name + ", Valencia, Spain")
    if place['status'] == 'OK' and place['results']:
        place_id = place['results'][0]['place_id']
        place_details = gmaps.place(place_id=place_id)
        result = place_details['result']
        name = result.get('name', 'N/A')
        address = result.get('formatted_address', 'N/A')
        opening_hours = result.get('opening_hours', {}).get('weekday_text', 'N/A')
        return {'name': name, 'address': address, 'opening_hours': opening_hours}
    else:
        return {'name': place_name, 'address': 'N/A', 'opening_hours': 'N/A'}


# Obtener detalles de todas las cafeterías
cafeteria_details = [get_place_details(cafeteria) for cafeteria in cafeterias]


# Imprimir los detalles
def replaceUnicodeCharacters(message):
    return message.replace('\\u202f', ' ').replace('\\u2009', ' ')


for details in cafeteria_details:
    horarios = f"Horarios: {details['opening_hours']}\n"
    print(f"Nombre: {details['name']}")
    print(f"Dirección: {details['address']}")
    print(f"Horarios: " + replaceUnicodeCharacters(horarios))
