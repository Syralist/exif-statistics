from exif import Image
import re
from glob import glob
import pathlib

pfad = r"P:/"

excludes = ["unbearbeitet", "Fotobuch", r"\web", "ungefiltert"]


def exclude_path(p):
    for e in excludes:
        if e in p:
            return True
    return False


if __name__ == '__main__':
    files = [f for f in glob(f"{pfad}/**", recursive=True) if re.search(r"\d{4} .*\\.*[.](jpg|JPG)$", f) and not exclude_path(f)]
    # for f in files:
    #     print(f)
    print(pathlib.Path(files[-1]))
    with open(pathlib.Path(files[-1]), 'rb') as image_file:
        my_image = Image(image_file)

    for tag in dir(my_image):
        try:
            print(f'"{tag}" : {my_image.get(tag)}')
        except ZeroDivisionError:
            print(f'"{tag}" : 0/0')
