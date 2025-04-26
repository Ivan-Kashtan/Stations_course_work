# Расчет ткз - исходные данные
from numpy import array, sqrt, where, empty
from gen import *
from in_dat import omega, s_sc, l_ln, n_g
from trnsfm import *
import line as ln
from var2 import n1_c

s_b = 1000
u_b = array([24, 330, 750])
i_b = s_b / (sqrt(3) * u_b)
# Генератор
e_g = 1 + x_d__ * sin_g
x_g = array([x_d__ * s_b / s_g, x2 * s_b / s_g])
r_g = x_g[0] / (omega * t_ar)
# Параметры трансформатора блока
x_t = u_sc_tb / 100 * s_b / s_tb
r_t = p_sc_tb * s_b / s_tb**2
# Параметры атвтотрансформатора
#                  В    С   Н
u_sc_at_c = array([0.5*(u_sc_at[1] + u_sc_at[0] - u_sc_at[2]), 0.5*(u_sc_at[2] + u_sc_at[0] - u_sc_at[1]),
                   0.5*(u_sc_at[1] + u_sc_at[2] - u_sc_at[0])])
u_sc_at_c[where(u_sc_at_c < 0)] = 0

x_at = u_sc_at_c / 100 * s_b / s_at
r_at = p_sc_at * s_b / s_at**2
#              В    С   Н
# x_at_c = s_b / s_at * x_at
# r_at_c = s_b / s_at * r_at

n_at = 2
# Параметры линии
e_n = 1
x_n = s_b / s_sc
r_n = 0
x_ln = empty([2])
x_ln[0] = ln.x * l_ln * s_b / u_b[2]**2
x_ln[1] = 3 * x_ln[0]
r_ln = ln.r * l_ln * s_b / u_b[2]**2

n_b = array([n1_c, 0, n_g-n1_c])

print(r_at)
# print(x_ln[1])
