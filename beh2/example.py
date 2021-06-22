import tequila as tq
import numpy 

R1=1.0
R2=2.0
geometry="be 0.0 0.0 0.0\nh 0.0 0.0 {R1}\nh 0.0 0.0 -{R2}"
name="beh2/beh2_{R1:2.2f}_{R2:2.2f}_180/beh2_{R1:2.2f}_{R2:2.2f}_180" # adapt of you move data
mol = tq.Molecule(name=name.format(R1=R1, R2=R2), geometry=geometry.format(R1=R1,R2=R2), n_pno=None)
lqm = mol.local_qubit_map(hcb=False)
hcb_lqm = mol.local_qubit_map(hcb=True)

H = mol.make_hamiltonian().map_qubits(lqm)
HCB_H=mol.make_hardcore_boson_hamiltonian().map_qubits(hcb_lqm)
U = mol.make_upccgsd_ansatz(name="SPA").map_qubits(lqm)
HCB_U = mol.make_upccgsd_ansatz(name="HCB-SPA").map_qubits(hcb_lqm)

# diagonalize Hamiltonians
v, vv = numpy.linalg.eigh(H.to_matrix())
# etc
