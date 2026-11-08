import numpy as np
import warp as wp

wp.config.mode = "debug"
wp.init()

@wp.kernel
def gradient2D(a: wp.array(dtype=float), b: wp.array(dtype=wp.vec2), inv_2hx: float, inv_2hy: float):
    
    i, j = wp.tid() # 2D grid

    # Initial implementation following exact notation of the central difference method
    # We can further optimise the order of operations and remove division entirely. Multiplcation is generally cheaper
    # We can precompute the factor of (2 * h) into 1/2h and reduce the parenthesis into a single multiplcation
    # The factor would be precomputed along with other simulation domain constant before kernel launch
    """
    ddx = (a[i + 1, j] - a[i - 1, j]) / (2 * hx)
    ddy = (a[i, j + 1] - a[i, j -1]) / (2 * hy)
    """

    ddx = (a[i + 1, j] - a[i - 1, j]) * inv_2hx
    ddy = (a[i, j + 1] - a[i, j - 1]) * inv_2hy

    # i'll implement boundary branching next, where i or j = 0 requires forward difference..

    b[i , j] = wp.vec2(ddx, ddy)

