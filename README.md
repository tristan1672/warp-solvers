# Summary

Warp sandbox where I implement compute kernels. https://github.com/NVIDIA/warp/tree/main

# Setup

```
# Creates the venv if missing, then installs dependencies and checks the GPU.
if (-not (Test-Path .venv)) { py -3.11 -m venv .venv }
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python check_warp.py
```
