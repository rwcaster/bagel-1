from core.db.amino_acid import one_to_THREE

with open( 'bagel.pdb' ) as wt:
  wt = wt.readlines()

with open( 'list.txt' ) as l:
  l = l.readlines()

for line in l:
  with open( 'in/' + line.strip() + '.pdb' , 'w') as target:
    orig, i, new = line[0], line[1:-2], line[-2] #-2 since there's a newline char
    for atom in wt:
      atom = atom.strip()
      atm = atom.split()
      if atm[0] == 'ATOM' or atm[0] == 'HETATM':
        if atm[5] != i:
          print( atom, file = target ) 
        else:
          if atm[2] in [ 'N', 'C', 'CA', 'O' ]:
            print( atom[:17] + one_to_THREE(new) + atom[20:], file=target )
          else:
            pass #don't print anything

      elif atm[0] == 'REMARK':
        if re.match( i , atom ):
          pass # don't print remarks lines mentioning this position
        else:
          print( atom, file=target) 
        print( atom , file=target)
      else:
        pass 



