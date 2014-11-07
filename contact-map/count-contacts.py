# pdb parser 

from re import match
from numpy import array 

class Atom:
  def __init__(self, l):
    self.record = l[0:6]
    self.atom_serial = int(l[6:11]) 
    self.atom_n = int(l[12:16])
    self.alt_loc = l[16]
    self.aa = l[17:20]
    self.chain = l[21] 
    self.aa_n = int(l[22:26])
    self.achar = l[26]
    self.xyz = (float(inp[31:38]), float(inp[40:46]), float(inp[48:54]))
    self.record = l[0:6]

    self.attr = { 
      'record': l[0:6].strip(),
      'atom_serial': int(l[6:11]), 
      'atom_n': int(l[12:16]),
      'alt_loc': l[16],
      'aa': l[17:20],
      'chain': l[21],
      'aa_n': int(l[22:26]),
      'achar': l[26],
      'xyz': (float(inp[31:38]), float(inp[40:46]), float(inp[48:54]))
      'occupancy': float(l[54:60]),
      'temp_factor': float(l[60:66]),
      'seg_id': l[72:76].strip(),
      'element': l[76:78].strip(),
      'charge': l[78:80].strip(),
    }

  def dist(self, other):
    x1, y1, z1 = self.xyz
    x2, y2, z2 = other.xyz
    return ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5

class PDB:
  'Represents a single PDB, use like 1sny = PDB("1sny.pdb")'
  def __init__(self, fn):
    with open(fn) as fn:
      self.atoms = [ Atom(l) for l in fn if match(r'^ATOM', l) ]
      self.hetatms = [ Atom(l) for l in fn if match(r'^HETATOM', l) ] 

#contact_map = [ [ (1, ca.aa) if ca.dist(i) < 10 else 0 for ca in cas ] for i in seq ]
#_matrix = array(_map)
