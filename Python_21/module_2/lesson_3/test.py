from datetime import date

today = date.today()
date = date.fromisoformat("2024-01-23")
print(date >= today)