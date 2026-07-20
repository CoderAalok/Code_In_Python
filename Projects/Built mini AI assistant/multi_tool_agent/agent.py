import datetime
import random
import requests
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from typing import List, Optional

# Static Data
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

PLACES = {
    "nepal": [
        "Pashupatinath Temple",
        "Swayambhunath Stupa",
        "Boudhanath Stupa",
        "Mount Everest",
        "Annapurna Base Camp",
        "Pokhara",
        "Chitwan National Park",
        "Lumbini",
        "Rara Lake",
        "Bhaktapur Durbar Square",
    ],

    "india": [
        "Taj Mahal",
        "Red Fort",
        "Qutub Minar",
        "Gateway of India",
        "Golden Temple",
        "Hawa Mahal",
        "Mysore Palace",
        "Kerala Backwaters",
        "Varanasi Ghats",
        "Statue of Unity",
    ],

    "china": [
        "Great Wall of China",
        "Forbidden City",
        "Terracotta Army",
        "Temple of Heaven",
        "The Bund",
        "Summer Palace",
        "Zhangjiajie National Forest Park",
        "West Lake",
        "Potala Palace",
        "Jiuzhaigou Valley",
    ],

    "japan": [
        "Mount Fuji",
        "Fushimi Inari Shrine",
        "Tokyo Tower",
        "Kinkaku-ji",
        "Arashiyama Bamboo Forest",
        "Osaka Castle",
        "Shibuya Crossing",
        "Himeji Castle",
        "Nara Park",
        "Itsukushima Shrine",
    ],

    "uk": [
        "Big Ben",
        "Tower of London",
        "Buckingham Palace",
        "Stonehenge",
        "London Eye",
        "Edinburgh Castle",
        "Tower Bridge",
        "Windsor Castle",
        "Lake District",
        "British Museum",
    ],

    "france": [
        "Eiffel Tower",
        "Louvre Museum",
        "Notre-Dame Cathedral",
        "Palace of Versailles",
        "Mont Saint-Michel",
        "Arc de Triomphe",
        "French Riviera",
        "Disneyland Paris",
        "Champs-Élysées",
        "Sainte-Chapelle",
    ],

    "germany": [
        "Brandenburg Gate",
        "Neuschwanstein Castle",
        "Cologne Cathedral",
        "Berlin Wall Memorial",
        "Black Forest",
        "Museum Island",
        "Zugspitze",
        "Miniatur Wunderland",
        "Heidelberg Castle",
        "Marienplatz",
    ],

    "usa": [
        "Statue of Liberty",
        "Grand Canyon",
        "Yellowstone National Park",
        "Golden Gate Bridge",
        "Times Square",
        "Hollywood Sign",
        "Niagara Falls",
        "Yosemite National Park",
        "Walt Disney World",
        "White House",
    ],

    "australia": [
        "Sydney Opera House",
        "Great Barrier Reef",
        "Uluru",
        "Bondi Beach",
        "Harbour Bridge",
        "Blue Mountains",
        "Twelve Apostles",
        "Kangaroo Island",
        "Daintree Rainforest",
        "Fraser Island",
    ],

    "canada": [
        "Niagara Falls",
        "Banff National Park",
        "Lake Louise",
        "CN Tower",
        "Jasper National Park",
        "Parliament Hill",
        "Old Quebec",
        "Whistler",
        "Stanley Park",
        "Peggy's Cove",
    ],
}

TOPICS = [
    'Technology',
    'Research',
    'Environment' 
    'Scientific',
    'Entertainment',
    'Climate', 
    'Physics', 
    'Mathematics', 
    'Culture', 
    'Religion',
    'Discipline',
    'Knowledge & Wisdom',  
]

# Model used
MODEL_GEMINI_LATEST = "gemini-flash-latest"

# DEFINE THE TOOLS

# normalize city
def _normalize(city: str):
    return city.strip().title()

# geocoding the country/city to get peck info it
def get_geoCode(city_query: str) -> List:
    get_geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city_query, 
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=5,
    )

    # load data
    get_geo.raise_for_status()
    geo_data = get_geo.json()

    # field out of the geocoding API's JSON reponse
    results = geo_data.get("results")
    return results


# find weather of country/city
def getWeather(city: str) -> dict:
    """Retrieves the real current weather conditions, temperature and wind speed of a country/city"""
    
    # normalize city name
    city_query = _normalize(city)
    
    try:
        # step 1: geocode the city name to get latitude/longitude
        results = get_geoCode(city_query)
        
        # check results 
        if not results:
            return {
                "status": "Error",
                "report": f"Sorry! I couldn't find a location for {city_query.capitalize()}.",
            }
        
        city_details = results[0]
        lat = city_details["latitude"]
        lon = city_details["longitude"]
        city_name = city_details.get("name", city_query)
        country = city_details.get("country", "")
        
        # step 2: fetch current weather for those coordinates
        get_weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,weather_code,wind_speed_10m",
                "timezone": "auto",
            },
            timeout=5,
        )
        
        get_weather.raise_for_status()
        weather_data = get_weather.json()
        
        weather_details = weather_data.get("current", {})
        temperature = weather_details.get("temperature_2m")
        weather_code = weather_details.get("weather_code")
        wind_speed = weather_details.get("wind_speed_10m")
        condition = WEATHER_CODES.get(weather_code, "Unknown conditions")
        
        return {
            "status": "Success",
            "report": (
                f"The weather in {city_name}, {country} is {condition.lower()} " 
                f"with temperature {temperature}°C and wind speed {wind_speed} km/hr."
            )
        }
    
    
    except requests.exceptions.RequestException as e:
        return {
            "status": "Error",
            "error_message": f"Error: {str(e)}\nSorry, I cannot retrieve weather report for {city_query}.",
        }
    
# get date and time
def getDateAndTime(city: str) -> dict:
    """Retrives the real date & time of a city"""
    
    city_query = _normalize(city)
    # step 1: Geocode the city to get timezone info
    try:
        results = get_geoCode(city_query)
        if not results:
            return {
                "status": "Error",
                "report": f"Sorry! I couldn't find a location for {city_query}."
            }
        
        location = results[0]
        city_name = location.get("name", city_query)
        country = location.get("country", "")
        tz_identifier = location.get("timezone")
        
        if not tz_identifier:
            return {
                "status": "Error",
                "report": f"No timezone information available for {city_query}."
            }
        
        # step 2: get current time 
        tz = ZoneInfo(tz_identifier)
        curr_time = datetime.datetime.now(tz)

        return {
            "status": "Success",
            "report": (
                f"The current date & time in {city_name}, {country} is "
                f"{curr_time.ctime()}."
            )
        }
    
    
    except requests.exceptions.RequestException as e:
        return {
        "status": "Error",
        "error_message": f"Error: {str(e)}\nSorry! I cannot retrieve time for {city_query}."
    }
    

# summarize some topics
def summarize(topic: str) -> dict:
    # if topic releates
    if topic in TOPICS:
        return {
            "status": "Success",
            "result": "Interesting topic"
        }
    
    else:
        return {
            'status': 'Error',
            'result': f"I don't have any information about {topic}."
        }


# gives the beautiful place names of a country
def getPlace(country: str) -> dict:
    country = _normalize(country).lower()
    places = PLACES.get(country)
    
    if not places:
        return {
            'status': 'Error',
            'report': f"Sorry, I don't have any information about {country.title()}."
        }
    
    place = random.choice(places)
    return {
        'status': "Success",
        'report': f"The most beautiful place in {country.title()} is {place}."
    }


# greeting user
def greet(name: Optional[str] = None) -> str:
    """Generic greeting if name not provided otherwise using name to greeting"""
    if name:
        name = _normalize(name)
        greeting = f"Hi {name}!"
    else:
        greeting = "Hi there!"
        
    return f"{greeting} what's today in your mind?"
    

# farewell  
def farewell() -> str:
    return "See you later! Have a good day."


# re-defined sub-agent (ensures they exist in this context)
greeting_agent = None
try:
    greeting_agent = Agent(
        name = "greeting_agent",
        model = MODEL_GEMINI_LATEST,
        description = "Your only task is to greet the user.",
        instruction = "You are greeting assistant. " \
        "Always use the 'greet' tool to greet the user."
    )

except Exception as e:
    print(f"Error: {e}")

farewell_agent = None
try:
    greeting_agent = Agent(
        name = "farewell_agent",
        model = MODEL_GEMINI_LATEST,
        description = "Your only task is to say, 'See you later.' to the user.",
        instruction = "You are a farewell assistant. " \
        "Always use the 'farewell' tool and say, 'See you later.'"
    )

except Exception as e:
    print(f"Error: {e}")
    

# Defined main agent job
root_agent = Agent(
    name = "agent",
    model= MODEL_GEMINI_LATEST,
    description = "Your task is to handle all tools except greeting and farewell tools.",
    instruction = "You are a helpful assistant. " \
                "Provide the current date & time, weather conditions, temperature and wind speed. " \
                "Use search tools (e.g. Google) to provide concise and precise answers, or whenever you are unsure of the answer.",

    tools = [getWeather, getDateAndTime, summarize, getPlace],
)

