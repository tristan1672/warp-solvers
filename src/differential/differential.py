import numpy as np
import warp as wp

wp.config.mode = "debug"
wp.init()

@wp.kernel
def gradient2D(a: wp.array(dtype=float), b: wp.array(dtype=wp.vec2), inv_hx: float, inv_hy: float, r: int, c: int):
    
    i, j = wp.tid() # 2D grid

    # Initial implementation following exact notation of the central difference method
    # We can further optimise the order of operations and remove division entirely. Multiplcation is generally cheaper
    # We can precompute the factor of (2 * h) into 1/2h and reduce the parenthesis into a single multiplcation
    # The factor would be precomputed along with other simulation domain constant before kernel launch
    """
    ddx = (a[i + 1, j] - a[i - 1, j]) / (2 * hx)
    ddy = (a[i, j + 1] - a[i, j -1]) / (2 * hy)
    """
    
    # Negligible branch divergence, only edge threads diverge
    # Warp divergence here is a much better cost than splitting into 3 kernels (forward, backward, central)
    # Warp divergence refers to when a warp has threads executing different paths, and the warp has to execute sequentially
    # per branch, so conceptually in this case we if our array is sized 32 or smaller (a warp is 32 threads, larger and we induce more warps),
    # and the 0 and 31 thread executes forward and backward difference while 1 - 30 executes central difference,
    # we would have 3 sequential warp executions, 1st run being thread 0 running the forward diff and 1-31 being masked off,
    # 2nd run being thread 31 (n-1) running the backward diff and the 3rd run executing thread 1-30 for the central diff.

    # X derivatives
    if i == 0 : # Forward
        ddx = (a[i + 1, j] - a[i, j]) * inv_hx
    elif i == r - 1 : # Backward
        ddx = (a[i, j] - a[i - 1, j]) * inv_hx
    else:   # Central
        ddx = (a[i + 1, j] - a[i - 1, j]) * 0.5 * inv_hx

    # Y derivatives
    if j == 0 :
        ddy = (a[i, j + 1] - a[i, j]) * inv_hy
    elif j == c - 1 :
        ddy = (a[i, j] - a[i, j - 1]) * inv_hy
    else:
        ddy = (a[i, j + 1] - a[i, j - 1]) * 0.5 * inv_hy


    b[i , j] = wp.vec2(ddx, ddy)
