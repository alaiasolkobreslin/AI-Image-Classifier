import pathlib

imgs = pathlib.Path("cat_aesthetic")

with open("captions.txt", "w") as f:
    # f.write("rsync -Pav andrz@nlpgpu-login.seas.upenn.edu:")
    for img in imgs.iterdir():
        img_id = img.stem
        dirname = str(img_id)[:5]
        f.write(f"{dirname}/{img_id}.txt\n")
    # f.write("aesthetic_captions/")

# rsync -Pav --files-from=captions.txt --no-R andrz@nlpgpu-login.seas.upenn.edu:/nlp/data/andrz/cis5200-final-project/filtered_aesthetic/img2/ aesthetic_captions
