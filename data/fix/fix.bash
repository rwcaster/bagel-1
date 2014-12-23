for line in $( cat plates.csv ); do
  OLD=$( echo $line | cut -d, -f2 )
  if grep -q $( echo $line | cut -d, -f2 ) fix.txt; then
    NEW=$( grep $OLD key.txt | awk '{ print $2 }' ) 
    echo $line | sed -E s/$OLD/$NEW/g 
  else
    echo $line
  fi
done
