with open( 'wrong.txt', 'r' ) as wrong, open( 'right.txt', 'a' ) as right:
  for wrongn in wrong:
    print( wrongn[0] + str( int( wrongn[1:-2] ) - 3 ) + wrongn[-2], file=right) 
