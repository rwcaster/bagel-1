#$ -cwd
#$ -S /bin/bash
#$ -N frelax
#$ -e prepare-logs
#$ -o prepare-logs

f=$( awk 'NR=="'${SGE_TASK_ID}'"' scaffolds.txt )
cd prepare-input/

export PATH=/home/carlin/Rosetta/main/source/bin:$PATH
export ROSETTA3_DB=/home/carlin/Rosetta/main/database

rosetta_scripts.static.linuxgccrelease -out:path:all ../prepare-output -s ${f}.pdb -parser:protocol frelax.xml -nstruct 10 -extra_res_fa NAX-${f}*.params

