from PIL import Image
class ImageEditor():
    def __init__(self, filename):
         self.filename = filename
         self.original = None
         self.changed = list()
    def open (self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдено!')
        self.original.show()

    def do_left(self):
            rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
            self.changed.append(rotated)
            rotated.save('stichh.jpg')

    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        cropped.save('stichh.jpg')

MyImage = ImageEditor("stichh.jpg")
MyImage.open()
MyImage.do_left()
MyImage.do_cropped()
for im in MyImage.changed:
    im.show()