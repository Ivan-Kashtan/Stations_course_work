# кз в точке К1 - РУСН

from sc import *
from numpy import array, e, sqrt
from var2 import n1_c
from in_dat import n_g

# '''
# 3-й вариант схемы - блоки подключены к АТ
# x[0] - прямая последовательность, x[1] - обратная
x_b = array([[(x_g[0]+x_t[0]) / n1_c, (x_g[0]+x_t[0]) / (1-n1_c)],
            [(x_g[1]+x_t[0]) / n1_c, (x_g[1]+x_t[0]) / (1-n1_c)]])
x_n_e = x_ln / ln.n_ln + x_n
# Зачастую x[1] == x[0] == x
x_at_e = x_at[0] / n_at
x_e = x_n_e * x_b[:, 1] / (x_n_e + x_b[:, 1])
# x_e1 = x_b[:, 0] * x_b[:, 1] / (x_b[:, 0] + x_b[:, 2])
# x_e2 = x_n_e * x_b[:, 2] / (x_n_e + x_b[:, 2])
x_s = x_b[:, 0] * (x_at_e + x_e) / (x_b[:, 0] + x_at_e + x_e)

# '''

'''
# 3-й вариант схемы - блоки подключены к АТ
# прямая последовательность
x_b11 = (x_g[0] + x_t[0]) / n1_c
x_b21 = (x_g[0] + x_t[0]) / (n_g - n1_c)

# x_b31 = (x_g[0] + x_at[2]) / n_at
# x_n_e = x_ln / ln.n_ln + x_n

x_at_e = x_at[0] / n_at
x_e11 = x_b11 * x_b31 / (x_b11 + x_b31)
x_e21 = x_n_e * x_b31 / (x_n_e + x_b31)

x_s1 = x_e11 * (x_at_e + x_e21) / (x_e11 + x_at_e + x_e21)
'''
# '''
# нулевая последовательность
x_b_0 = array([x_t[0] / n1_c, x_t[0], x_at[0] / n_at])
x_n_e_0 = x_ln[0] / ln.n_ln + x_n
x_at_e_0 = x_at[0] / n_at
x_e1_0 = x_at_e_0 + (x_n_e_0 * x_b_0[2]) / (x_n_e_0 + x_b_0[2])
x_e2_0 = x_e1_0 * x_b_0[2] / (x_e1_0 + x_b_0[2])
x_s_0 = x_b_0[0] * x_e2_0 / (x_b_0[0] + x_e2_0)
# '''
'''
# x[0] - нулевая последовательность, x[1] - прямая, x[2] - обратная
x_b = array([[(x_t[0] / 3), x_t[0], x_at[2] / 2],
            [(x_g[0] + x_t[0]) / 3, x_g[0] + x_t[0], (x_g[0] + x_at[2]) / 2],
             [(x_g[1] + x_t[0]) / 3, x_g[1] + x_t[0], (x_g[1] + x_at[2]) / 2]])
# Зачастую x[1] == x[2]
x_n_e = x_ln / ln.n_ln + x_n
x_at_e = x_at[0] / n_at
x_e1 = array([x_at_e + (x_n_e[0] * x_b[0, 2]) / (x_n_e[0] + x_b[0, 2]),
              x_b[1, 0] * x_b[1, 2] / (x_b[1, 0] + x_b[1, 2]),
              x_b[2, 0] * x_b[2, 2] / (x_b[2, 0] + x_b[2, 2])])

x_e2 = array([x_e1[0] * x_b[0, 2] / (x_e1[0] + x_b[0, 2]), x_n_e[0] * x_b[1, 2] / (x_n_e[0] + x_b[1, 2]), x_n_e * x_b[2, 2] / (x_n_e[0] + x_b[2, 2])])
# x_s = array([x_e1[1] * (x_at_e + x_e2) / (x_e1 + x_at_e + x_e2)])
'''

# '''
r_b = array([(r_g + r_t[0])/n1_c, (r_g + r_t[0]), ((r_g + r_at[0])/ n_at)])
r_n_e = r_ln / ln.n_ln + r_n
r_at_e = r_at[0] / n_at
x_e = x_n_e * x_b[:, 1] / x_n_e * x_b[:, 1]
# r_e1 = r_b[0] * r_b[2] / (r_b[0] + r_b[2])
r_e2 = r_n_e * r_b[2] / (r_n_e + r_b[2])
r_s = r_b[0] * (r_at_e + r_e2) / (r_b[0] + r_at_e + r_e2)

e_e = array([e_g, (e_g * x_n_e[1] + e_n * x_b[1, 0]) / (x_n_e[1] + x_b[1, 0])])
e_s = (e_e[0] * (x_at_e + x_e1[0]) + e_e[1] * x_e1[0]) / (x_e1[0] + x_at_e + x_e2[0])
I_sc_3 = array([e_e[0] / x_e1 * i_b[1], e_e[1] / (x_at_e + x_e1) * i_b[1]])
I_sc_3_s = sum(I_sc_3[0])
t_a = x_s[0] / (omega * r_s)
k_s = 1 + e**(-0.01 / t_a)
i_sc_3 = sqrt(2) * k_s * I_sc_3_s
I_sc_1 = 3 * e_s / (sum(x_s) + x_s_0) * i_b[1]

# x = 1

print(I_sc_1)


e_e = array([e_g, (e_g * x_n_e[1] + e_n * x_b21[1, 0]) / (x_n_e[1] + x_b21[1, 0])])
e_s = (e_e[0] * (x_at_e + x_e21[0]) + e_e[1] * x_e11[0]) / (x_e11[0] + x_at_e + x_e2[0])
I_sc_3 = array([e_e[0] / x_e11 * i_b[1], e_e[1] / (x_at_e + x_e11) * i_b[1]])
I_sc_3_s = sum(I_sc_3[0])
t_a = x_s1[0] / (omega * r_s)
k_s = 1 + e**(-0.01 / t_a)
i_sc_3 = sqrt(2) * k_s * I_sc_3_s
I_sc_1 = 3 * e_s / (sum(x_s1) + x_s_0) * i_b[1]

