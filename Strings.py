season = "peak"
price = 9000
print(f"Season: {season}, Base ₹{price}")
print(f"Report:".upper(), season.lower())

file = "Per_Night_GMV_2025_05_28.csv"

parts = file.split("_")
price = price + 500 
print(f"{parts}, Max price is {price}")

