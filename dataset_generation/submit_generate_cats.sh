#!/bin/bash
#
#SBATCH --partition=p_nlp
#SBATCH --job-name=gencats
#SBATCH --output=../logs/%x.%j.txt
#SBATCH --gpus=1
#SBATCH --nodelist=nlpgpu05

srun python generate_cats.py
