# moldata
Some molecular data

## BeH2 Data:
Computed with 2 PNOs for each active orbital.  
Geometry is:
'''bash
Be 0.0 0.0 0.0
H  0.0 0.0  R1
H  0.0 0.0 -R2
'''  
and data is stored in `beh2_R1_R2_180_...` files.

Load into tequila as:
```python
import tequila as tq
mol = tq.Mol(geometry.format(R1,R2), name="beh2/beh2_{R1:2.2f}_{R2:2.2f}/beh2_{R1:2.2f}_{R2:2.2f}".format(R1,R2), n_pno=None)
# get full Hamiltonian and some ansatz (8 qubits)
H = mol.make_hamiltonian()
U = mol.make_upccgsd_ansatz(name="SPA")
# get HCB Hamiltonian and HCB ansatz (4 qubits)
H = mol.make_hardcore_boson_hamiltonian()
U = mol.make_upccgsd_ansatz(name="HCB-SPA")
```

## Install Tequila
Check the [tequila github](https://github.com/aspuru-guzik-group/tequila) page or type:
```bash
pip install git+https://github.com/aspuru-guzik-group/tequila.git@devel
```

## References
Molecules are computed with the approach of  
[arxiv:2008.02819](https://arxiv.org/abs/2008.02819)  
Further improvements (better MRA protcol and SPA ansatz in example above) are descirbed in  
[arxiv:2105.03836](https://arxiv.org/abs/2105.03836)
