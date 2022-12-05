import pathlib
import random

import torch
import tqdm
from diffusers import StableDiffusionPipeline

prompt_path = pathlib.Path("aesthetic_captions")
out1_path = pathlib.Path("cat_generated_aesthetic")
out2_path = pathlib.Path("cat_generated_specific_prompts")

prompts = (
    "cat",
    "picture of a cat",
    "realistic cat",
    "cat painting",
    "cat drawing",
    "photo of a cat",
    "cute cat",
    "realistic drawing of a cat",
    "photorealistic cat painting",
    "cat image",
)

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
if torch.cuda.is_available():
    pipe = pipe.to("cuda")


def generate_from_txt_prompt(txt_path):
    img_id = txt_path.stem
    with open(txt_path) as f:
        prompt = f.read().strip()
    print(prompt)
    for _ in range(5):
        result = pipe(prompt)
        image = result.images[0].resize((256, 256))
        nsfw = result.nsfw_content_detected[0]
        if not nsfw:
            break
    else:
        print("Could not generate non-NSFW image after 5 attempts, skipping prompt")
        return
    image.save(out1_path / f"{img_id}_generated.png")
    print(f"Saved as {img_id}_generated.png.\n")


for fp in tqdm.tqdm(list(prompt_path.glob("*.txt"))):
    generate_from_txt_prompt(fp)


def generate_from_random_prompt(idx: int):
    prompt = random.choice(prompts)
    print(prompt)
    for _ in range(5):
        result = pipe(prompt)
        image = result.images[0].resize((256, 256))
        nsfw = result.nsfw_content_detected[0]
        if not nsfw:
            break
    else:
        print("Could not generate non-NSFW image after 5 attempts, skipping prompt")
        return
    image.save(out2_path / f"{idx}.png")
    print(f"Saved as {idx}.png.\n")


for fp in tqdm.tqdm(range(7000)):
    generate_from_random_prompt(fp)
