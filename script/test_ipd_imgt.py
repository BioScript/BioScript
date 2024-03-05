# coding: utf-8
import sys
sys.path.append("..")

from bioscript import IpdImgt
from pprint import pprint

ipd_imgt = IpdImgt()

# res = ipd_imgt.allele(project="HLA", query="startsWith(name,A*02:01)")
# print(res)

hla_a_0201 = ipd_imgt.get_alleles(starts_with="A*02:01")
print(hla_a_0201)
# hla_a_0201_iterator = ipd_imgt.iter(hla_a_0201)
# for item in hla_a_0201_iterator:
#     pprint(ipd_imgt.get_single_allele(accession=item["accession"]))
