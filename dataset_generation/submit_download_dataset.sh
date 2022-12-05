#!/bin/bash
#
#SBATCH --job-name=ldown
#SBATCH --output=logs/download_dataset.txt

srun python download_dataset.py
