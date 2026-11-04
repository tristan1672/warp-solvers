import warp as wp

wp.init()
print("Warp", wp.config.version)

@wp.kernel
def add_one(a: wp.array(dtype=float)):
    i = wp.tid()
    a[i] = a[i] + 1.0

a = wp.zeros(8, dtype=float, device= "cuda:0")
wp.launch(add_one, dim=8, inputs=[a])
print(a.numpy())