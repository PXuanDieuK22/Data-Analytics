import math
r = float(input("Nhap ban kinh r: "))

cv = 2* math.pi * r
dt = math.pi * r**2

print(f"Ban kinh: {r}")
print(f"Chu vi hinh tron: {cv}")
print(f"Dien tich hinh tron: {dt}")