import tequila as tq

def compute_molecule(points,n_pno=2):
    geometry="Be 0.0 0.0 0.0\nH 0.0 0.0 {R1:2.2f}\nH 0.0 0.0 -{R2:2.2f}"
    name="beh2_{R1:2.2f}_{R2:2.2f}_180"
    R1 = points["R1"]
    R2 = points["R2"]
    mol=tq.Molecule(name=name.format(**points), geometry=geometry.format(**points), n_pno=n_pno)

compute_molecule(points={"R1":1.1,"R2":2.0})
