from datetime import datetime, date

now = datetime.now()
print(now)

formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted)

today = date(2024, 1, 9)
new_year = date(2025, 1, 1)
diff = new_year - today
print(diff)