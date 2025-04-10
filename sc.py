# Расчет ткз
from numpy import array, sqrt
from gen import *
from in_dat import omega, s_sc
from trnsfm import *

s_b = 1000
u_b = array([24, 330, 750])
# Параметры трансформатора блока
i_b = s_b / (sqrt(3) * u_b)
e = 1 + x_d__ * sin_g
x_g = array([x_d__ * s_b / s_g, x2 * s_b / s_g])
r_g = x_g[0] / (omega * t_ar)

x_t = u_sc1 / 100 * s_b / s[0]
r_t = p_sc * s_b / s_t**2
# Параметры атвтотрансформатора
u_sc_at_c = array([0.5*(u_sc_at[1] + u_sc_at[0] - u_sc_at[2]), 0.5*(u_sc_at[1] + u_sc_at[0] - u_sc_at[2]]))
# Параметры линии
e_s = 1
x_s = s_b / s_sc
r_s = 0
x_l = x0 * l * s_b / u_b[2]

