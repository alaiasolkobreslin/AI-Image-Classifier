import os
import re

from datasets import load_dataset

dataset = load_dataset("laion/laion2B-en-aesthetic")["train"]
print(f"total: {dataset.num_rows}")

# filter for captions with the word "cat"
CAT_REGEX = re.compile(r"\bcat\b", re.IGNORECASE)


def is_a_cat_picture(example):
    if (pwatermark := example.get("pwatermark", 1)) is None:
        pwatermark = 1
    if (punsafe := example.get("punsafe", 1)) is None:
        punsafe = 1
    if (punsafe := example.get("punsafe", 1)) is None:
        punsafe = 1
    if (width := example.get("WIDTH", 0)) is None:
        width = 1
    if (height := example.get("HEIGHT", 0)) is None:
        height = 1

    return (
        example["TEXT"]
        and pwatermark < 0.5
        and punsafe < 0.5
        and width >= 256
        and height >= 256
        and (CAT_REGEX.search(example["TEXT"]) is not None)
    )


filtered_dataset = dataset.filter(is_a_cat_picture)
print(f"filtered: {filtered_dataset.num_rows}")

# 100k is a lot, trim it down to about 10k
# cats_10k = filtered_dataset.train_test_split(test_size=0.1)["test"]
# print(f"split: {cats_10k.num_rows}")

# save filtered dataset
os.makedirs("filtered_dataset", exist_ok=True)
filtered_dataset.to_csv("filtered_dataset/cats.csv")
# cats_10k.to_csv("filtered_dataset/cats_10k.csv")

# img2dataset --url_list=filtered_dataset/cats.csv --output_folder=filtered_dataset/img --thread_count=64 --image_size=256 --resize_mode=center_crop --url_col "URL" --caption_col "TEXT" --input_format=csv --save_additional_columns '["similarity","hash","punsafe","pwatermark","aesthetic","TEXT"]' --encode_format=png --encode_quality=5 --enable_wandb=True
# clip-retrieval inference --input_dataset img2 --output_folder embeddings --enable_wandb=True --enable_text=False
# clip-retrieval index --embeddings_folder embeddings --index_folder indices
# clip-retrieval filter --query "picture of a cat" --output_folder "cat/" --indice_folder indices
# rsync -av andrz@$NLPGPU:/nlp/data/andrz/cis5200-final-project/filtered_dataset/cat ~/Downloads/
