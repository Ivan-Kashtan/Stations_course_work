# Расчет ткз - исходные данные
from numpy import array, sqrt, where, empty
from gen import *
from in_dat import omega, s_sc, l_ln
from trnsfm import *
import line as ln

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
# u_sc_at_c = array([0.5*(u_sc_at[1] + u_sc_at[0] - u_sc_at[2]), 0.5*(u_sc_at[2] + u_sc_at[0] - u_sc_at[1]),
#                    0.5*(u_sc_at[1] + u_sc_at[2] - u_sc_at[0])])
# u_sc_at_c[where(u_sc_at_c < 0)] = 0

# x_at = u_sc_at_c / 100 * s_b / s_at
# r_at = p_sc_at * s_b / s_at**2
#              В    С   Н
x_at = array([59.1, 0, 98.5])
r_at = array([0.49, 0.49, 1.36])
n_at = 2
# Параметры линии
e_n = 1
x_n = s_b / s_sc
r_n = 0
x_ln = empty([2])
x_ln[0] = ln.x * l_ln * s_b / u_b[2]**2
x_ln[1] = 3 * x_ln[1]
r_ln = ln.r * l_ln * s_b / u_b[2]**2

# print(x_at)
