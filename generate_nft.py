import os
import random
import traits_handler as traits
from PIL import Image
import json

# This file is used to generate the NFT images, you should run this before running generate_metadata.py

# Variables here can be edited

TOTAL_IMAGES = 100
TRAIT_FOLDER = 'traits'
OUTPUT_FOLDER = 'output'
COLLECTION_NAME = ''
METADATA_FILE_NAME = './metadata/all-traits.json'

# ----

all_images = []
excluded_traits = []


def generate_traits(n: int):
    chosen_traits = {}

    # Traits can be added, removed or edited to fit your customization
    chosen_traits['Background'] = random.choices([i[0] for i in traits.background], [i[1] for i in traits.background])[
        0]
    chosen_traits['Blush'] = random.choices([i[0] for i in traits.blush], [i[1] for i in traits.blush])[0]
    chosen_traits['Body'] = random.choices([i[0] for i in traits.body], [i[1] for i in traits.body])[0]
    chosen_traits['Clothes'] = random.choices([i[0] for i in traits.clothes], [i[1] for i in traits.clothes])[0]
    chosen_traits['Eyes'] = random.choices([i[0] for i in traits.eyes], [i[1] for i in traits.eyes])[0]
    chosen_traits['Hair'] = random.choices([i[0] for i in traits.hair], [i[1] for i in traits.hair])[0]
    chosen_traits['Hat'] = random.choices([i[0] for i in traits.hat], [i[1] for i in traits.hat])[0]
    chosen_traits['Mouth'] = random.choices([i[0] for i in traits.mouth], [i[1] for i in traits.mouth])[0]
    chosen_traits['Scarf'] = random.choices([i[0] for i in traits.scarf], [i[1] for i in traits.scarf])[0]
    chosen_traits['tokenId'] = n

    if chosen_traits in all_images:
        return generate_traits(n)
    return chosen_traits


def generate_image():
    for image in all_images:

        # Traits can be added, removed or edited to fit your customization
        # If you're editing above, you'll be editing here as well
        img1 = Image.open(f'./{TRAIT_FOLDER}/background/{traits.background_file[image["Background"]]}.png').convert(
            'RGBA')
        img2 = Image.open(f'./{TRAIT_FOLDER}/blush/{traits.blush_file[image["Blush"]]}.png').convert('RGBA')
        img3 = Image.open(f'./{TRAIT_FOLDER}/body/{traits.body_file[image["Body"]]}.png').convert('RGBA')
        img4 = Image.open(f'./{TRAIT_FOLDER}/clothes/{traits.clothes_file[image["Clothes"]]}.png').convert('RGBA')
        img5 = Image.open(f'./{TRAIT_FOLDER}/eyes/{traits.eyes_file[image["Eyes"]]}.png').convert('RGBA')
        img6 = Image.open(f'./{TRAIT_FOLDER}/hair/{traits.hair_file[image["Hair"]]}.png').convert('RGBA')
        img7 = Image.open(f'./{TRAIT_FOLDER}/hat/{traits.hat_file[image["Hat"]]}.png').convert('RGBA')
        img8 = Image.open(f'./{TRAIT_FOLDER}/mouth/{traits.mouth_file[image["Mouth"]]}.png').convert('RGBA')
        img9 = Image.open(f'./{TRAIT_FOLDER}/scarf/{traits.scarf_file[image["Scarf"]]}.png').convert('RGBA')

        # You might have to change your composite numbers and the number of lines depending on the number of traits available
        com1 = Image.alpha_composite(img1, img2)
        com2 = Image.alpha_composite(com1, img3)
        com3 = Image.alpha_composite(com2, img4)
        com4 = Image.alpha_composite(com3, img5)
        com5 = Image.alpha_composite(com4, img6)
        com6 = Image.alpha_composite(com5, img7)
        com7 = Image.alpha_composite(com6, img8)
        com8 = Image.alpha_composite(com7, img9)

        rgb_img = com8.convert('RGB')
        file_name = f"{COLLECTION_NAME}_{image['tokenId']}.png"
        rgb_img.save(f'./{OUTPUT_FOLDER}/{file_name}')
        print(f"Generated NFT #{image['tokenId']}")

        os.mkdir(f'./metadata')
        with open(METADATA_FILE_NAME, 'w') as outfile:
            json.dump(all_images, outfile, indent=4)


def main():
    for i in range(TOTAL_IMAGES):
        new_image = generate_traits(i + 1)
        all_images.append(new_image)
        i += 1
    generate_image()


main()
