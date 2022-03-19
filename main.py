from PIL import Image, ImageDraw, ImageFont
import random

def random_phrase():
    nouns = open("nouns.txt", "r").readlines()
    actions = open("actions.txt", "r").readlines()

    ret = f"When the {random.choice(nouns)[:-1]} {random.choice(actions)[:-1]} you"

    return ret

def generate_meme(meme):
    texts = {
        "peace": random_phrase()
    }

    return texts[meme]

def main():
    caption = generate_meme("peace")

    img = Image.open("formats/peace.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('impact.ttf', size=18)
    draw.text((0, 0), caption, 'white', font)
    img.save('out.png')

main()
