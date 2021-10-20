import tequila as tq
import multiprocessing as mp
import numpy
import sys
import os

def compute_molecule(points,n_pno=8):
    geometry="Be 0.0 0.0 0.0\nH 0.0 0.0 {R1:2.2f}\nH 0.0 0.0 -{R2:2.2f}"
    name="beh2_{R1:2.2f}_{R2:2.2f}_180"
    os.mkdir(name.format(**points))
    os.chdir(name.format(**points))
    R1 = points["R1"]
    R2 = points["R2"]
    mol=tq.Molecule(name=name.format(**points), geometry=geometry.format(**points), n_pno=n_pno, pno={"maxrank":n_pno//2})
    os.chdir("..")

os.environ['MAD_NUM_THREADS'] = '12'
os.environ['OMP_NUM_THREADS'] = '12'
pool = mp.Pool(4)

start=1.0
stop=3.0
num=21
datapoints=[]
for R1 in numpy.linspace(start,stop,num):
    for R2 in numpy.linspace(start,stop,num):
        if R2 < R1:
            continue
        datapoints.append({"R1":R1, "R2":R2})

print("{} datapoints: estimated compute time < {} min".format(len(datapoints), len(datapoints)/4))
pool.map(compute_molecule, datapoints)
