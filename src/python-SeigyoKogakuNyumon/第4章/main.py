# ライブラリのインポート
from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import bodeplot_set as bs
import linestyle_generator as lg
import plot_set as ps

Np = [1, 2]
Dp = [1, 5, 3, 4]
P = tf(Np, Dp)
print(P)
