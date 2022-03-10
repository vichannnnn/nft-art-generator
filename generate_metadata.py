import json

f = open('./metadata/all-traits.json', )
data = json.load(f)

# Variables here can be edited


IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmTJgvDuf3hD6eZ2DAus34qLfnM7HqfJwZjdbYAjtXHsxn/"
PROJECT_NAME = "Girl NFT"
COLLECTION_NAME = ''

# ----


def get_attribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URL + COLLECTION_NAME + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }

    # Traits can be added, removed or edited to fit your customization
    # If you're editing generate_nft.py, you'll be editing here as well
    token["attributes"].append(get_attribute("Background", i["Background"]))
    token["attributes"].append(get_attribute("Blush", i["Blush"]))
    token["attributes"].append(get_attribute("Body", i["Body"]))
    token["attributes"].append(get_attribute("Clothes", i["Clothes"]))
    token["attributes"].append(get_attribute("Eyes", i["Eyes"]))
    token["attributes"].append(get_attribute("Hair", i["Hair"]))
    token["attributes"].append(get_attribute("Hat", i["Hat"]))
    token["attributes"].append(get_attribute("Mouth", i["Mouth"]))
    token["attributes"].append(get_attribute("Scarf", i["Scarf"]))

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()
