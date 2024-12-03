import h5py

with h5py.File("obama.h5", "r") as f:
    print((f["Barack_Obama"][0]).decode())
    f.close()