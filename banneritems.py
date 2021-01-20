import random


def standard_banner(star):
    characters = {
        "five_stars" : ["Keqing", "Qiqi", "Jean", "Mona", "Diluc"],
        "four_stars" : ["Sucrose", "Fischl", "Xingqiu", "Xiangling", "Razor", "Barbara", "Chongyun", "Bennett", "Ningguang", "Beidou", "Amber", "Kaeya", "Lisa"]

    }

    if int(star) == 5:
        chosen = random.choice(characters["five_stars"])
        print(str(chosen))
        return str(chosen)
    elif int(star) == 4:
        chosen = random.choice(characters["four_stars"])
        print(str(chosen))
        return str(chosen)



def event_char_banner(star):
    characters = {
        "five_stars" : ["Albedo", "Mona", "Diluc", "Keqing", "Qiqi", "Jean"],
        "four_stars" : ["Sucrose", "Fischl", "Xingqiu", "Xiangling", "Razor", "Barbara", "Chongyun", "Bennett", "Ningguang", "Beidou", "Amber", "Kaeya", "Lisa", "Noelle", "Xinyan", "Diona"]

    }

    if int(star) == 5:
        chosen = random.choice(characters["five_stars"])
        print(str(chosen))
        return str(chosen)
    elif int(star) == 4:
        chosen = random.choice(characters["four_stars"])
        print(str(chosen))
        return str(chosen)
