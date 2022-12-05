#!/bin/bash
#
#SBATCH --job-name=idown
#SBATCH --output=logs/download_images.txt

img2dataset --url_list=filtered_dataset/cats.csv --output_folder=img --thread_count=64 --image_size=256 --resize_mode=center_crop --url_col "URL" --caption_col "TEXT" --input_format=csv --save_additional_columns '["similarity","hash","punsafe","pwatermark","aesthetic"]' --encode_format=png --encode_quality=5