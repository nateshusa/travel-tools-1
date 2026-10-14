from fastapi import FastAPI

app = FastAPI(title="Travel Tools Service")

WEATHER = {
    "chennai":      {"temp_c": 33, "sky": "humid and sunny"},
    "kuala lumpur": {"temp_c": 30, "sky": "thunderstorms in the evening"},
    "muscat":       {"temp_c": 38, "sky": "clear and very hot"},
    "bengaluru":    {"temp_c": 26, "sky": "cloudy"},
}
RATES_FROM_INR = {"MYR": 0.05, "OMR": 0.0045, "USD": 0.012, "INR": 1.0}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/weather")
def weather(city: str):
    return WEATHER.get(city.lower().strip(), {"error": "city not in demo data"})

@app.get("/convert")
def convert(amount: float, to_currency: str):
    rate = RATES_FROM_INR.get(to_currency.upper())
    if rate is None:
        return {"error": "currency not in demo data"}
    return {"amount_inr": amount, "to": to_currency.upper(), "result": round(amount * rate, 2)}
