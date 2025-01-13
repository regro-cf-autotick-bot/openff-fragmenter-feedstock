from openff.toolkit import Molecule
from openff.fragmenter.fragment import WBOFragmenter



parent_molecule = Molecule.from_smiles("OC1(CN(C1)C(=O)C1=CC(F)=CC=C1)")

result = WBOFragmenter().fragment(parent_molecule)

assert len(result.fragments) == 2
