# – к стороне СН подключено 4 генератора (n1 = 4), к автотрансформаторам связи генераторы не подключены.
# from math import sqrt, ceil
from numpy import sqrt, ceil

from gen import cos_g
from load import *

n1_c = 4

p1 = n1_c * p_g_ - p_ld_min_sm
q1 = n1_c * q_g_ - q_ld_min_sm
s1 = sqrt(p1**2 + q1**2) / 2

p2 = p1 - p_r
q2 = q1 - p_r * (1 - cos_g**2)**(1/2)/cos_g
k_r = 1.2
s2 = sqrt(p2**2 + q2**2) / k_r

p3 = p_ld_max_w - (n1_c - 1)*p_g_ + p_s_n
q3 = q_ld_max_w - (n1_c - 1)*q_g_ + q_s_n
s3 = sqrt(p3**2 + q3**2) / 2

p4 = p_ld_max_s - (n1_c - 2)*p_g_ + 2*p_s_n
q4 = q_ld_max_s - (n1_c - 2)*q_g_ + 2*q_s_n
s4 = sqrt(p3**2 + q3**2) / 2

s_c = max(s1, s2, s3, s4)
# 1048

# print(int(ceil(s1)))
# print(int(ceil(s2)))
# print(int(ceil(s3)))
print(int(ceil(s_c)))
