#requires mutants in the form ALA 123 PHE with spaces
gawk 'BEGIN{FIELDWIDTHS="13 2 2 3 2 4 54"}{if($6+0=="'$2'") \
      {if($2=="N "||$2=="CA"||$2=="C "||$2=="O ") \
      {$4="'$3'"; print $1 $2 $3 $4 $5 $6 $7} \
      else next}else print $0}' wt.pdb > $1$2$3.pdb
