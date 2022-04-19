from PIL import Image, ImageEnhance, ImageFilter


img = Image.open("imposter.gif")

counter = 0
frame = 0

while True:

    img.seek(frame)
    copy = img.convert()
    enhance_factor = (10 * (1 + frame + counter * img.n_frames))

    ecolor = ImageEnhance.Color(copy)
    copy = ecolor.enhance(enhance_factor)

    econtrast = ImageEnhance.Contrast(copy)
    copy = econtrast.enhance(enhance_factor)

    for i in range(int(enhance_factor / 10)):
        copy = copy.filter(ImageFilter.SHARPEN)
    copy.show()

    frame += 1
    if frame == img.n_frames:
        frame = 0
        counter += 1
