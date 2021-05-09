from control.matlab import *

S1 = tf([0, 1], [1, 1])
S2 = tf([1, 1], [1, 1, 1])
S = S1 / (1 + S1 * S2)
print('S=', S.minreal())
S = feedback(S1, S2)
print('S=', S.minreal())
