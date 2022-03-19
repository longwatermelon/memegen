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
    verb = random.choice(open('verbs.txt', 'r').readlines())[:-1]
    noun = random.choice(open('nouns.txt', 'r').readlines())[:-1]
    noun2 = random.choice(open('nouns.txt', 'r').readlines())[:-1]
    
    texts = {
        "peace": random_phrase(),
        "spongebob": random_nouns(5, 350, 230),
        "uno": [[(100, 150), f"{verb} {noun}s"], [(300, 20), f"{noun2}s"]]
    }

    return texts[meme]

def main():
    meme = random.choice(["peace", "spongebob", "uno"])
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
