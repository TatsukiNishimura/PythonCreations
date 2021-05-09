from control.matlab import *

S1 = tf([0, 1], [1, 1])
S2 = tf([1, 1], [1, 1, 1])
S = S2 * S1
print('S=', S)
S = series(S1, S2)
print('S=', S)
