# Режимы АТ 1. НН - генератор
# 1. НН -> ВН, СН
# 2. ВН, НН -> СН

from numpy import array, empty

s_n = 63
u = array([220, 110])

p = empty([2, 3])
q = empty([2, 3])
# 1 р-м     ВН   СН
p[0, :2] = [20, -15]
q[0, :2] = [10, -10]
# 2 р-м     СН   НН
p[1, 1:] = [-40, 25]
q[1, 1:] = [-20, 15]

s = p + 1j*q
# Изменить знаки по схеме!
s[0, 2] = s[0, 0] - s[0, 1]
s[1, 0] = s[1, 1] + s[1, 2]

k_tp = (u[0] - u[1]) / u[0]
s_tp = k_tp * s_n  # type

s_l = abs(s[:, 2])
# s_l > s_tp -> не допустимый р-м
s_c = abs(k_tp*abs(s[:, 0]) + abs(s[:, 2]))  # common
# s_c > s_tp -> недопустимый р-м
print(s_c)
