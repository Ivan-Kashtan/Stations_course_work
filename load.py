from numpy._core._multiarray_umath import ceil

from in_dat import *
from gen import q_g, s_g
# from in_dat import p_r

# Мощности нагрузок потребителей
# Максимальная в зимний период
p_ld_max_w = n_ld * p_ld*k_s
tg_ld = (1 - cos_ld**2)**(1/2)/cos_ld
q_ld_max_w = p_ld_max_w*tg_ld
s_ld_max_w = p_ld_max_w / cos_ld
# Максимальная в летний период
p_ld_max_s = p_ld_max_w * k_max_sm
q_ld_max_s = q_ld_max_w * k_max_sm
s_ld_max_s = s_ld_max_w * k_max_sm

p_ld_min_sm = p_ld_max_w * k_min_sm
q_ld_min_sm = q_ld_max_w * k_min_sm
s_ld_min_sm = s_ld_max_w * k_min_sm
# Мощности собственных нужд
p_s_n = k_s_n * p_g
q_s_n = k_s_n * q_g
s_s_n = k_s_n * s_g

p_g_ = (1-k_s_n) * p_g
q_g_ = (1-k_s_n) * q_g
s_g_ = (1-k_s_n) * s_g  # 875
# ТНЦ-1000000/330, 347/24
n1 = int(ceil(p_ld_max_w / p_g_))  # число генераторов, работающих на сторону СН
n1_c = (p_ld_max_w / p_g_)
# n1 = ceil(85/27)
# n1 = ceil(85/27)

# print(f'{s_g_:.1f}')
# print(f'{s_s_n:.1f}')
# print(f'{n1:.1f}')
