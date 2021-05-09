from control.matlab import *

s1 = tf([1], [1, 1])
s2 = tf([1], [1, 2])
s3 = tf([3, 1], [1, 0])
s4 = tf([2, 0], [1])
s12 = feedback(s1, s2)
s3_12 = series(s12, s3)
S = feedback(s3_12, s4)
print(S)
# 正解
