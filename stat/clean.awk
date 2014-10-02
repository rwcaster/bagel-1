IFS=","
NR == 1 { printf("Plate,Sample,Yield,Dilution,Well,MaxV,kobs,S\n") }
NR > 1 { print $1, $2, $3, $4, $5, $6, $7, $8 }
