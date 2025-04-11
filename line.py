from numpy import sqrt, array

from in_dat import n_g, u_s, s_sc
from load import p_g_, p_ld_min_sm, q_ld_min_sm, q_g_

p = n_g * p_g_ - p_ld_min_sm
q = n_g * q_g_ - q_ld_min_sm
s = sqrt(p**2 + q**2)

n_ln = 3
n_w = 4  # число проводов расщепленных
# 240*5 или 400*4 # Файбисович с. 77 табл. 3.7
# с. 86 - токи
# с. 79 - удельные параметры линий
i = s / (sqrt(3) * u_s * (n_ln - 1) * n_w)
# АС 400/64
x = 0.289
r = 0.0187

print(i)
