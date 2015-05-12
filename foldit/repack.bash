# runs the rosetta script repack.xml, which mutates a single residue and then repacks 
# a synonymous mutation is given below 

rosetta_scripts.macosclangrelease @ repack.flags -in:file:s bagel.pdb -parser:script_vars position=164 new_residue=GLU 
