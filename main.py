from PIL import Image, ImageDraw, ImageFont
import random

def plural(action):
    if len(action.split()) > 1:
        return ' '.join([f"{action.split()[0]}s", action.split()[1]])
    else:
        return f"{action}s"

def random_phrase() -> list:
    nouns = open("nouns.txt", "r").readlines()
    actions = open("actions.txt", "r").readlines()

    ret = f"When the {random.choice(nouns)[:-1]} {plural(random.choice(actions)[:-1])} you"

    return [[(0, 0), ret]]

def random_nouns(count, x, spacing) -> list:
    nouns = open("nouns.txt", "r").readlines()

    return [[(x, spacing * i), random.choice(nouns)] for i in range(count)]

def generate_meme(meme) -> list:
    verb = random.choice(open('verbs.txt', 'r').readlines())[:-1]
    noun = random.choice(open('nouns.txt', 'r').readlines())[:-1]
    noun2 = random.choice(open('nouns.txt', 'r').readlines())[:-1]
    action = random.choice(open('actions.txt', 'r').readlines())[:-1]
    noun3 = random.choice(open('nouns.txt', 'r').readlines())[:-1]
    adjective = random.choice(open('adjs.txt', 'r').readlines())[:-1]

    texts = {
        "peace": random_phrase(),
        "uno": [[(100, 150), f"{verb} {noun}s"], [(300, 20), f"{noun2}s"]],
        "bonjour": [[(0, 0), f"{noun3}s when the {noun} {plural(action)} the {noun2}"]],
        "incredible": [[(50, 150), f"Me when I {action} the {noun}"], [(600, 150), f"It's {adjective}"]],
        "death": [[(250, 0), f"The {noun} when I {action} the {noun2}"]],
        "waiting": [[(10, 0), f"{random.choice(['Me', noun])} waiting for the {noun2} to {action} {random.choice(['my', 'the'])} {noun3}"]]
    }

    return texts[meme]

def main():
    meme = random.choice(["peace", "uno", "bonjour", "incredible", "death", "waiting"])
    caption = generate_meme(meme)

    img = Image.open(f"formats/{meme}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('impact.ttf', size=24)
    print(caption)

    for l in caption:
        print(l[0])
        draw.text((l[0][0] - 1, l[0][1] - 1), l[1], 'black', font)
        draw.text((l[0][0] + 1, l[0][1] - 1), l[1], 'black', font)
        draw.text((l[0][0] - 1, l[0][1] + 1), l[1], 'black', font)
        draw.text((l[0][0] + 1, l[0][1] + 1), l[1], 'black', font)

        draw.text(l[0], l[1], 'white', font)

    img.save('out.png')

    with open("caption", "w") as f:
        for i in caption:
            f.write(i[1])
            f.write('.\n')

if __name__ == '__main__':
    main()
