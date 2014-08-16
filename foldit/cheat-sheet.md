Foldit Model of Beta-glucosidase B
==================================

Important basics
----------------

+ Load Your Protein:
Start ---> Intro Puzzles --> Level 1-1 -->  Intro Puzzle loaded hit:  Ctrl-Alt-Shift-A

Select all four files: 

+ bagel.pdb+ cid92930.conf.pdb+ cid92930.enzdes.cst+ cid92930.params

Use the advanced design interface
----------------------
Menu --> Selection Interface
Menu --> General Options --> Show Advanced GUI
Menu --> View Options 
  Cartoon Thin
  Score/Hydro+CPK

Save Your Protein:  
------------------
Ctrl-Alt-Shift-S

Residue energy
--------------
Mouse over residue so it is highlighted and hit Tab

Viewing Options
---------------
+ Zoom to Area of Interest: Mouse over residue of interest so it is highlighted;  hit Shift-Q  (no click) I often move around until I see the ligand and then do this

+ BackShading:  Ctrl-Shift-Click (on black backdrop) and drag

+ Front Clipping:  Ctrl-Alt-Click (on black backdrop) and drag

+ Measuring:  Mouse over atom1 of interest, hit Ctrl-Alt-Shift-C (no click), repeat for atom 2 (reports distance), atom 3 (angle), and atom 4 (dihedral)


Selection Options
---------------------
+ See upper left corner of Foldit

+ SphereAround:  Ctrl-Shift-Click on residue and drag. 


Using terminal commands 
-----------------------
+ (Main --> Script Terminal)
+ Select specific residue:  selection.Select(<res#>)
+ Zoom to specific residue:  ui.CenterViewport(<res#>)


Design Options
----------------
+ Click residue and hit mutate (m).  Selecting a subset of residues (lower right boxes) can be used to do directed designs.  This selection will be used in both mutate AND shake (i.e. shake now mutates those residues while everything else stays native).


Rules of Thumb
--------------
+ NEVER WIGGLE (W) without selecting a sub-selection. 
+ Sometimes high energies (mutations/conformations) are need to get to the low energy.
+ Importance of score is in order as it appears in the Tab menu
+ Native or close to native is generally better
+ Manually force the interaction you want and then side-chain wiggle (E) those residues and the ones around it
+ General order of operations:  E --> S --> E
+ If score is not dropping faster than 0.05/s you are likely at an energy minima.  This is true ONLY FOR Wiggling (W/E).  If you are shaking pay attention to the number of cycles on the upper left corner.  Often the low energy is found after 5-10 cycles (cycles is the number in the parenthesis after the timer).


General Energy Rules (on a per amino acid basis)
------------------------------------------------
+ Energies less than 0 are good.
+ Energies 0 - +2 can be ok if clashing (fa_rep) is low (i.e. <1)
+ Energies +2 - +5 are iffy… but can work if you think the "static" picture is missing the enabling feature
+ Energies +5 - +10 are are unlikely… something will likely have to move for this to work
+ Energies >+10 are are really unlikely to work… but go for it if you have a good reason
