# tools.py
import requests
from langchain_core.tools import tool

# 1. We use the @tool decorator to automatically turn this into a LangChain tool
@tool
def weather_tool(city: str) -> str:
    """Get the current weather for a specific city. Example: 'Lagos'"""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url).json()
        current = response["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        return f"Weather in {city}: {temp}°C, {desc}, Humidity: {humidity}%."
    except Exception as e:
        return f"Could not get weather: {e}"

# 2. We define explicit parameters (amount, from_currency, to_currency)
@tool
def currency_tool(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts a specific amount from one currency to another. 
    Currencies MUST be 3-letter ISO codes (e.g., 'USD', 'NGN', 'EUR', 'GBP').
    """
    try:
        # Ensure the codes are uppercase for the API
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url).json()
        
        # Check if the API returned a valid response
        if response.get("result") == "error":
            return f"API Error: {response.get('error-type')}"
            
        rate = response["rates"].get(to_currency)
        if not rate:
            return f"Currency '{to_currency}' not found in exchange rates."
            
        converted_amount = amount * rate
        
        # Format the output beautifully with commas (e.g., 20,000.00)
        return f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}"
        
    except Exception as e:
        return f"Could not convert currency: {e}"

# Note: We completely deleted the old `Tool(name=..., func=...)` wrappers at the bottom! 
# The @tool decorator handles all of that automatically.