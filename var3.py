# к стороне СН подключено 3 генератора (n1= 3), к автотрансформаторам связи подключены генераторы.
from math import sqrt, ceil

from gen import cos_g
from load import *
# from var1 import p1_max
import var1
n1_c = 3

p1 = var1.p1 / 2 + p_g
q1 = var1.q1 / 2 + q_g
s1 = sqrt(p1**2 + q1**2) / 2
# p1 = var1.p1

p2 = var1.p1 + 2*p_g - p_r
q2 = var1.q1 + 2*p_g - p_r
k_r = 1.3
s2 = sqrt(p2**2 + q2**2) / k_r

p3 = p_ld_max_w - (n1_c - 1)*p_g_ - 2*p_g + p_s_n
q3 = q_ld_max_w - (n1_c - 1)*q_g_ - 2*q_g + q_s_n
k_p = (u_s - u_ld) / u_s  # profitability
s3 = sqrt((p3/2 + p_g_ / k_p)**2 + (q3/2 + q_g_/k_p)**2)

p4 = p_ld_max_s - (n1_c - 2)*p_g_ - 2*p_g_ + 2*p_s_n
q4 = q_ld_max_s - (n1_c - 2)*q_g_ + 2*q_s_n
s4 = sqrt((p4/2 + p_g_/k_p)**2 + (q4/2 + q_g_/k_p)**2)

s5 = s_g_ / k_p

s6 = s_g_
s_c = max(s1, s2, s3, s4, s5, s6)
# 1733

# print(int(ceil(p1)))
# print(int(ceil(q1)))
#
# print(int(ceil(s2)))
# print(int(ceil(s3)))
# print(int(ceil(s4)))
# print(int(ceil(s5)))
# print(int(ceil(s6)))
# print(int(ceil(s_c)))
