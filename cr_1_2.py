# КР 1. Режимы АТ. НН - нагрузка
# 1. СН -> ВН, НН
# 2. ВН -> СН, НН
from numpy import array, empty

s_n = 400
u = array([330, 150])

p = empty([2, 3])
q = empty([2, 3])
# 1 р-м     ВН    СН
p[0, :2] = [-120, 270]
q[0, :2] = [-50, 100]
# 2 р-м     СН    НН
p[1, 1:] = [-140, 210]
q[1, 1:] = [-40, 80]

s = p + 1j*q
# Изменить знаки по схеме!
s[0, 2] = s[0, 0] + s[0, 1]
s[1, 0] = s[1, 1] - s[1, 2]

k_tp = (u[0] - u[1]) / u[0]
s_tp = k_tp * s_n  # type

s_lv = abs(s[:, 2])
s_c = abs(k_tp*abs(s[:, 0]) + abs(s[:, 2]))  # common
# s_lv > s_tp -> недопустимый р-м
# s_c > s_tp -> недопустимый р-м
if s_lv.any() > s_tp:
    print('Перегрузка обмотки НН')
if s_c.any() > s_tp:
    print('Перегрузка общей обмотки')

print(s_lv)
print(s_c)
print(s_tp)
