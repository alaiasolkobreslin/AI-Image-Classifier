#!/bin/bash
#
#SBATCH --job-name=cats
#SBATCH --output=logs/cats.txt

srun python cats.py
