import math

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return f"Phương trình có một nghiệm: x = {-c / b}"
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

# Chạy chương trình
if __name__ == "__main__":
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    print(giai_phuong_trinh_bac_hai(a, b, c))

import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu cho hình trái tim
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Vẽ đồ thị
plt.plot(x, y, 'r')
plt.fill(x, y, 'red', alpha=0.6)  # Tô màu đỏ
plt.axis("equal")
plt.axis("off")  # Ẩn trục
plt.title("❤️ Hình Trái Tim ❤️", fontsize=14, color='red')
plt.show()
