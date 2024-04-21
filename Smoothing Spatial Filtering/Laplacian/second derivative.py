import numpy as np
import matplotlib.pyplot as plt

# 2차 미분의
# 함수 정의
def f(x):
    return x**3 - 3*x**2 + 2

def f_prime(x):
    return 3*x**2 - 6*x

def f_double_prime(x):
    return 6*x - 6

# x 값 설정
x = np.linspace(-1, 4, 400)

# 함수 계산
y = f(x)
y_prime = f_prime(x)
y_double_prime = f_double_prime(x)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.gca().set_facecolor('black')
plt.gcf().set_facecolor('black')

plt.plot(x, y, label="f(x) = $x^3 - 3x^2 + 2$", color="cyan")
plt.plot(x, y_prime, label="f'(x) = $3x^2 - 6x$", color="yellow")
plt.plot(x, y_double_prime, label="f''(x) = $6x - 6$", color="magenta")

# 특정 점 표시 (1차 미분이 0인 점 및 2차 미분이 0인 점)
critical_points = [1, 2]  # 1차 미분이 0인 x값
inflection_point = [1]    # 2차 미분이 0인 x값

for cp in critical_points:
    plt.scatter(cp, f(cp), color='red')  # 최소/최대점
    plt.annotate(f"({cp}, {f(cp):.2f})", (cp, f(cp)), textcoords="offset points", xytext=(0,10), ha='center', color='white')

for ip in inflection_point:
    plt.scatter(ip, f(ip), color='blue') # 변곡점
    plt.annotate(f"({ip}, {f(ip):.2f})", (ip, f(ip)), textcoords="offset points", xytext=(0,-15), ha='center', color='white')

plt.title("Function and its Derivatives")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='white', linewidth=0.5)
plt.axvline(0, color='white', linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()
