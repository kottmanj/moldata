# moldata
Some molecular data from [arxiv:2105.03836](https://arxiv.org/abs/2105.03836)   
Molecules are computed in an optimized representation according to [10.1021/acs.jpclett.0c03410](https://doi.org/10.1021/acs.jpclett.0c03410). 
All in a minimal correlated size (as many spatial orbitals as electrons)

## H2 Data
4 qubit JW-Hamiltonian
2 qubit HCB-Hamiltonian
'''bash
H  0.0 0.0 0.0
H  0.0 0.0 {R}
'''
data is stored in `h2_R...` files.
## BeH2 Data:
8 Qubit JW-Hamiltonian
4 Qubit HCB-Hamiltonian
Geometry is:
'''bash
Be 0.0 0.0  0.0
H  0.0 0.0  {R1}
H  0.0 0.0 -{R2}
''' 
data is stored in `beh2_R1_R2_180_...` files.
## N2 Data:
12 Qubit JW-Hamiltonian
6 Qubit HCB-Hamiltonian
Geometry is:
'''bash
N 0.0 0.0 0.0
N 0.0 0.0 {R}
'''
data is stored in `n2_R...` files.

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
It is recommended to use the `local_qubit_map` to have a consistent ordering of the orbitals (otherwise it will change due to the degeneracies in the molecule). This will sort the orbitals (qubits) in the same way as displayed in [arxiv:2105.03836](https://arxiv.org/abs/2105.03836)
```
lqm = mol.local_qubit_map(hcb=True/False)
H = H.map_qubits(lqm)
U = U.map_qubits(lqm)
```

## Export Hamiltonians
Once created as above, export to openfermion like this:  
```python
qubit_operator = H.to_openfermion()
```

## Export Circuits
Get the circuit as above, export to [QASM](https://github.com/aspuru-guzik-group/tequila-tutorials/blob/main/OpenQASMConversions.ipynb) or some of the supported backends of tequila:  
```
backend_circuit = tq.compile(U, backend=...).circuit
```
For Pennylane: Export to `qiskit` and use the `from_qiskit` function in Pennylane (see [here](https://pennylane.readthedocs.io/en/stable/introduction/circuits.html). 

## Optimize Circuits
You can use tequila to optimize the circuits parameters:
'''bash
# if you use an HCB Hamiltonian, make sure to use an HCB circuit as well
# e.g. 'HCB-SPA', 'HCB-UpCCGD'
E = tq.ExpectationValue(H=H,U=U)
result = tq.minimize(E)
opt_energy = result.energy
opt_variables = result.variables

# evaluate E with opt variables
energy = tq.simulate(E, variables=opt_variables)
'''

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
