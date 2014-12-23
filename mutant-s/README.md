mo
==

Takes a FASTA nucleotide sequence and a list of mutations and generates oligos for Kunkel mutagenesis. Usage (from command prompt):

```bash 
python3 makeoligo.py [FASTA file] [list of mutations]
```

Example
-------

### 1sny.fasta

```
cacatgaatagcatcctgattaccggttgtaatcgtggtctgggcctgggtctggttaaagcactgctgaatctgccgcagcctccgcagcacctgtttaccacctgtcgtaatcgcgaacaggcaaaagaactggaagatctggccaaaaaccatagcaacattcatattctggaaatcgatctgcgcaacttcgatgcctatgataaactggttgcagatattgaaggtgtgaccaaagatcagggtctgaatgttctgtttaataacgcaggtattgcaccgaaaagcgcacgtattaccgcagttcgtagccaagaactgctggataccctgcagaccaataccgttgttccgattatgctggcaaaagcatgtctgccgctgctgaaaaaagcagcaaaagccaatgaaagccagccgatgggtgttggtcgtgcagccattattaacatgagcagcattctgggtagtattcagggtaataccgatggtggtatgtatgcatatcgtaccagcaaatcagcactgaatgcagcaaccaaaagcctgagcgttgatctgtatccgcagcgtattatgtgtgttagcctgcatccgggttgggttaaaaccgatatgggtggtagcagcgcaccgctggatgttccgaccagcaccggtcagattgttcagaccattagcaaactgggtgaaaaacagaatggtggctttgtgaattatgatggcactccgctggcatgg
```

### 1sny-list.txt

```
ser154ala+leu156asp+tyr170his
ala94phe+leu156his+met167asn+met207ala
ser154ala+tyr170his
leu156his
ala94lys+ser154ala+leu156asp+tyr170his
```

### Command line

```bash 
python3 makeoligo.py 1sny.fasta 1sny-list.txt
```

### Output

```
s154a+l156d+y170h,tttgctggtacgATGtgcatacataccacc,accctgaatactaccATCaatCGCgctcatgttaataat
a94f+l156h+m167n+m207a,gctgctaccaccCGCatcggttttaaccca,ggtacgatatgcataGTTaccaccatcggtatt,accctgaatactaccATGaatgctgctcatgtt,acgtgcgcttttcggAAAaatacctgcgttatt
s154a+y170h,tttgctggtacgATGtgcatacataccacc,aatactacccagaatCGCgctcatgttaataat
l156h,ctgaatactaccATGaatgctgctcatgtt
a94k+s154a+l156d+y170h,tttgctggtacgATGtgcatacataccacc,accctgaatactaccATCaatCGCgctcatgttaataat,acgtgcgcttttcggTTTaatacctgcgttatt
```
