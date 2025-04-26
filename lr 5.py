from numpy import array, pi
# 1
# omega = 2*pi * 50
# x_l = array([])
# x_t = array([])
# l = x / omega
# k = m / l
# x_b =

# k_l = x_d / (2*x_l) - 1  # продольный
# k_t = 1 - 2*x_t / (x_b)  # сквозной
# 2
# u_sc = u_


i = 4
u = array([3.2, 0.46])
x = u / i
k_c = 0.5

x_ = x*(1-k_c)
b = array([-x*k_c, x*(1+k_c), x*(1+k_c)])
print(b)
