# takes a bunch of individual assay plates (plate*csv)
# and imports them into a sqlite3 db

echo "Plate,Sample,Yield,Dilution,Well,Max V,kobs,S" > all-plates.csv
for fn in $( ls plate*csv ); do
  cat $fn | tail +2 | cut -d, -f1-8 >> all-plates.csv
done

python csv2sqlite.py all-plates.csv bagel-raw.db

