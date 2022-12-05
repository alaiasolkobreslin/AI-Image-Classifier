#!/bin/bash
#
#SBATCH --partition=p_nlp
#SBATCH --job-name=cats_full
#SBATCH --output=../logs/%x.%j.txt
#SBATCH --gpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --nodelist=nlpgpu02

srun python cats.py
srun img2dataset --url_list=filtered_dataset/cats.csv --output_folder=filtered_dataset/img --thread_count=64 --processes_count=8 --image_size=256 --resize_mode=center_crop --url_col "URL" --caption_col "TEXT" --input_format=csv --save_additional_columns '["similarity","hash","punsafe","pwatermark","aesthetic","TEXT"]' --encode_format=png --encode_quality=5 --enable_wandb=True
cd filtered_dataset
srun clip-retrieval inference --input_dataset img --output_folder embeddings --enable_wandb=True --enable_text=False
srun clip-retrieval index --embeddings_folder embeddings --index_folder indices
srun clip-retrieval filter --query "picture of a cat" --output_folder "cat/" --indice_folder indices
