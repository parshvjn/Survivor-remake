import pygame, os

BASE_IMG_PATH = 'assets/images/'

def load_image(path, scaleFactor = 1):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    if scaleFactor != 1: img = pygame.transform.scale(img, (img.get_width()*scaleFactor, img.get_height()*scaleFactor))
    # img.set_colorkey((0,0,0))
    return img

def load_images(path, scaleFactor = 1):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name, scaleFactor))
    return images