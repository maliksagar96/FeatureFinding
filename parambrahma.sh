#!/bin/sh

#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=15:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sagar.malik@students.iiserpune.ac.in
#SBATCH --job-name=ff62
#SBATCH --error=job.%J.err
#SBATCH --output=job.%J.out
#SBATCH --partition=standard
#SBATCH --no-requeue

#cd $SLURM_SUBMIT_DIR
cd /home/vijayakumar/Sagar/python/correlation/62

module load python/3.7

python3.7 run2D.py

