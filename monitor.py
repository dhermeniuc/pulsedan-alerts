
import json
import time
from datetime import datetime

# Simulare date alertă
alert = {
    "wallet": "4rKPQ8....2vSyKhT",
    "token": "TEST123",
    "price": "0.0032",
    "market_cap": "9500",
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

# Salvăm alerta într-un fișier JSON
with open("alerts.json", "w") as f:
    json.dump([alert], f, indent=2)

print("Alertă salvată cu succes în alerts.json")
