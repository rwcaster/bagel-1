#!/bin/bash

#$ -cwd 
#$ -S /bin/bash
#$ -e logs
#$ -o logs
#$ -p -4 
#4 -N all_bagels 

export ROSETTA_DB3=/share/tmp-data-1/siegellab/Rosetta/main/database
export PATH=$PATH:/share/tmp-data-1/siegellab/Rosetta/main/source/bin

TARGET=$( awk 'NR=="'${SGE_TASK_ID}'" { print $1 }' short_list.txt )
NEW_RES=$( awk 'NR=="'${SGE_TASK_ID}'" { print $2 }' short_list.txt )

rosetta_scripts.linuxgccrelease @ repack.enzdes.flags -in:file:s bagel.pdb -parser:script_vars target="$TARGET" new_res="$NEW_RES" 
