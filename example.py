import tequila as tq
import numpy 

R1=1.0
R2=2.0
geometry="be 0.0 0.0 0.0\nh 0.0 0.0 {R1}\nh 0.0 0.0 -{R2}"
name="beh2/beh2_{R1:2.2f}_{R2:2.2f}_180/beh2_{R1:2.2f}_{R2:2.2f}_180" # adapt of you move data
mol = tq.Molecule(name=name.format(R1=R1, R2=R2), geometry=geometry.format(R1=R1,R2=R2), n_pno=None)

print(mol)

lqm = mol.local_qubit_map(hcb=False)
hcb_lqm = mol.local_qubit_map(hcb=True)

H = mol.make_hamiltonian().map_qubits(lqm)
HCB_H=mol.make_hardcore_boson_hamiltonian().map_qubits(hcb_lqm)
U = mol.make_upccgsd_ansatz(name="SPA").map_qubits(lqm)
HCB_U = mol.make_upccgsd_ansatz(name="HCB-SPA").map_qubits(hcb_lqm)

# optimize circuit paramters (with SPA ansatz the result is the same)
result = tq.minimize(tq.ExpectationValue(H=H,U=U), silent=True)
print(result.energy)
result = tq.minimize(tq.ExpectationValue(H=HCB_H,U=HCB_U), silent=True)
print(result.energy)
# diagonalize Hamiltonians
v, vv = numpy.linalg.eigh(H.to_matrix())
print(v[0])
v, vv = numpy.linalg.eigh(HCB_H.to_matrix())
print(v[0])
