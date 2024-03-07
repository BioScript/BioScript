# BioScript
Open source toolkit for bioinformatics

## IPD
### Package Location 
`bioscript/lib/ipd_imgt`
### Usage
```python
from bioscript import IpdImgt
import pandas
import copy

ipd_imgt = IpdImgt()

hla_group = "A*02:07"

hla_alleles = ipd_imgt.get_alleles(starts_with=hla_group)
hla_iterator = ipd_imgt.iter(hla_alleles)
hla_all = list()
for item in hla_iterator:
    hla_all.append(copy.deepcopy(item))

df = pandas.DataFrame(hla_all)
print(df)
```
### Methods
 - `iter`
 - `get_alleles`
 - `get_single_allele`

Refer to `./notebook/HLA_allele_to_pseudo_seq.ipynb` for detailed usage.

## PseudoSequence
### Location
`bioscript/lib/pseudo_sequence`
### Usage
```python
from bioscript import PseudoSequence

# Example usage:
# fasta_string could be read from a file or received as input
hla_a00005_fasta = """>A*020101
MAVMAPRTLVLLLSGALALTQTWAGSHSMRYFFTSVSRPGRGEPRFIAVGYVDDTQFVRFDSDAASQRMEPRAPWIEQEGPEYWDGETRKVKAHSQTHRVDLGTLRGYYNQSEAGSHTVQRMYGCDVGSDWRFLRGYHQYAYDGKDYIALKEDLRSWTAADMAAQTTKHKWEAAHVAEQLRAYLEGTCVEWLRRYLENGKETLQRTDAPKTHMTHHAVSDHEATLRCWALSFYPAEITLTWQRDGEDQTQDTELVETRPAGDGTFQKWAAVVVPSGQEQRYTCHVQHEGLPKPLTLRWEPSSQPTIPIVGIIAGLVLFGAVITGAVVAAVMWRRKSSDRKGGSYSQAASSDSAQGSDVSLTACKV"""
# Extract the pseudo-sequence
hla_a00005 = PseudoSequence.extract_pseudo_sequence_from_fasta(hla_a00005_fasta, method="netmhcpan_4")
print(hla_a00005)
```

### Detailed Methods Description for PseudoSequence