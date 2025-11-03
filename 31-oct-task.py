import os
import requests
from dotenv import load_dotenv
from crewai import Crew, Agent, Task
from litellm import completion

# Initialize environment variables
load_dotenv()
OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def litellm_chat(prompt: str) -> str:
    """Wrapper for LiteLLM completion API"""
    response = completion(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_KEY,
        base_url="https://openrouter.ai/api/v1"
    )
    return response["choices"][0]["message"]["content"]

# Create a weather agent using CrewAI
weather_expert = Agent(
    role="Meteorologist",
    goal="Deliver precise and clear weather forecasts for a given location",
    backstory="A meteorology enthusiast skilled in reading atmospheric data and predicting conditions with precision.",
    verbose=False
)

# Function to fetch weather data
def fetch_weather(city: str) -> str:
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
    try:
        res = requests.get(api_url)
        info = res.json()
        if info.get("cod") != 200:
            return f"Could not retrieve weather data for '{city}'. Please try another location."
        temperature = info["main"]["temp"]
        description = info["weather"][0]["description"].capitalize()
        humidity = info["main"]["humidity"]
        wind_speed = info["wind"]["speed"]
        return f"Temperature: {temperature}°C | Condition: {description} | Humidity: {humidity}% | Wind Speed: {wind_speed} m/s"
    except Exception as err:
        return f"Error fetching weather details: {err}"

print("\n=== CrewAI Weather Assistant ===")

while True:
    city_name = input("Enter a city to get the weather (or type 'exit' to quit): ").strip()
    if city_name.lower() == "exit":
        print("Bot: Goodbye! Stay updated on the weather.")
        break
    print("Bot:", fetch_weather(city_name))

# Define a task for the agent
weather_job = Task(
    description=f"Fetch and present the latest weather update for {city_name}.",
    agent=weather_expert,
    expected_output="A clear and concise weather summary for the user."
)

# Build crew and execute
crew_team = Crew(
    agents=[weather_expert],
    tasks=[weather_job]
)

print("\nBot:", fetch_weather(city_name))