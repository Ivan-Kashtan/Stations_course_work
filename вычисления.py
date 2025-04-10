from numpy import array, sqrt, round

# x7 = 295,2
# x5 = 4.9
# x6  =20.1

# e1 = 440
# e2 = 121
# e3 = 97.8

x = array([295.2, 4.9, 20.1])
e = array([440, 121, 97.8])
i = e / (sqrt(3) * x)

print(round(i, 2))

