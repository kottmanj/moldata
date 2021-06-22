#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=40
#SBATCH --time=02:00:00
#SBATCH --job-name=lasse
#SBATCH --output=log-%j.txt
#SBATCH --mail-type=FAIL
 
cd $SLURM_SUBMIT_DIR

conda activate tequila-3.7 
source ~/bin/load_madness_env 

date
python script.py > script.out

# cleanup
rm */*.00000
rm */*.hdf5
rm */*.bin
rm */restarta*
rm */*nemo*
date 
