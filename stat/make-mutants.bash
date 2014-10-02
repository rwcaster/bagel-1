#low=$( grep ^SCORE score.sc | sort --reverse -k2 | awk 'NR==1 {print $NF}' )

for mutant in $( cat mutants ); do
  # GLN19ALA
  p=$( echo $mutant | tr -d A-Z )
  o=$( echo $mutant | tr -d 1-9 | cut -c 0-3 )
  n=$( echo $mutant | tr -d 1-9 | cut -c 4-6 )

  gawk 'BEGIN{FIELDWIDTHS="13 2 2 3 2 4 54"}{if($6+0=="'${p}'") \
        {if($2=="N "||$2=="CA"||$2=="C "||$2=="O ") \
        {$4="'${n}'"; print $1 $2 $3 $4 $5 $6 $7} \
        else next} else print $0}' 
done
