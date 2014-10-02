#$ -cwd
#$ -S /bin/bash
#$ -N brelax
#$ -e logs
#$ -o logs

export PATH=/home/carlin/Rosetta/main/source/bin:$PATH
export ROSETTA3_DB=/home/carlin/Rosetta/main/database

f=$( awk 'NR=="'${SGE_TASK_ID}'"' list )

rosetta_scripts.static.linuxgccrelease -s ${f}.pdb -parser:protocol frelax.xml -nstruct 10 -extra_res_fa cid92930.params

