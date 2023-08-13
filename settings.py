from numba import njit
import numpy as np
import glm
import math

# Resolution
WIN_RES = glm.vec2(1600, 900)

# Color
BG_COLOR = glm.vec3(0.2, 0.3, 0.05)
