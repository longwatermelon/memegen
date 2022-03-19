from PIL import Image, ImageDraw, ImageFont
import random

def random_phrase() -> list:
    nouns = open("nouns.txt", "r").readlines()
    actions = open("actions.txt", "r").readlines()

    ret = f"When the {random.choice(nouns)[:-1]} {random.choice(actions)[:-1]} you"

    return [[(0, 0), ret]]

def random_nouns(count, x, spacing) -> list:
    nouns = open("nouns.txt", "r").readlines()

    return [[(x, spacing * i), random.choice(nouns)] for i in range(count)]

def generate_meme(meme) -> list:
    texts = {
        "peace": random_phrase(),
        "spongebob": random_nouns(5, 350, 230)
    }

    return texts[meme]

def main():
    meme = random.choice(["peace", "spongebob"])
    caption = generate_meme(meme)

    img = Image.open(f"formats/{meme}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('impact.ttf', size=18)
    print(caption)

    for l in caption:
        print(l[0])
        draw.text((l[0][0] - 1, l[0][1] - 1), l[1], 'black', font)
        draw.text((l[0][0] + 1, l[0][1] - 1), l[1], 'black', font)
        draw.text((l[0][0] - 1, l[0][1] + 1), l[1], 'black', font)
        draw.text((l[0][0] + 1, l[0][1] + 1), l[1], 'black', font)

        draw.text(l[0], l[1], 'white', font)
    img.save('out.png')

main()
