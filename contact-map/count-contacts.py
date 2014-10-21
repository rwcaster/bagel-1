from re import match
from numpy import array 

class CA:
  def __init__(self, inp):
    self.aa = inp[17:20]
    self.xyz = (float(inp[31:38]), float(inp[40:46]), float(inp[48:54]))

  def dist(self, other):
    x1, y1, z1 = self.xyz
    x2, y2, z2 = other.xyz
    return ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5

with open('../foldit/bagel.pdb') as fn:
  seq = [ CA(l) for l in fn if match(r'^AT.+CA', l) ]

_map = [ [ (1, ca.aa) if ca.dist(i) < 10 else 0 for ca in seq ] for i in seq ]
_matrix = array(_map)
print(_map)
