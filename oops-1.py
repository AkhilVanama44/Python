






class camera:
    def crop(self):
        print("Photo is cropped")
    def edit(self):
        print("Photo is edited")
    def addcolor(self):
        print("Color is added")
class Filter:
    def greenary(self):
        print("Greenary filter is added")
    def black(self):
        print("Black filter is added")
class collage:
    def collagephoto(self):
        print("Photoes are merged")
class printphto:
    def passportsize(self):
        print("Passport Size photo is printed")
    def postcardsize(self):
        print("Postcard Size photo is printed")
    def largephoto(self):
        print("Largephoto is printed")
obj=camera()
obj.crop()
obj2=Filter()
obj2.greenary()

class camera:
    def crop(self):
        print("Photo is cropped")
    def edit(self):
        print("Photo is edited")
    def addcolour(self):
        print("Color is added")
class Filter:
    def greenary(self):
        print("Greenary filter is added")
    def black(self):
        print("Black filter is added")
class collage:
    def collagephoto(self):
        print("Photoes are merged")
class printphto:
    def passportsize(self):
        print("Passport Size photo is printed")
    def postcardsize(self):
        print("Postcard Size photo is printed")
    def largephoto(self):
        print("Largephoto is printed")

print('1.camera')
print('2.Filter')
print('3.collage')
print('4.printphoto')
x=int(input("choose: "))
match x:
    case 1:
        obj=camera()
        print('1.crop')
        print('2.edit')
        print('3.addcolour')
        x1=int(input("choose: "))
        match x1:
            case 1:
                obj.crop()
            case 2:
                obj.edit()
            case 3:
                obj.addcolour()
    case 2:
        obj1=Filter()
        print('1.greenary')
        print('2.black')
        x2=int(input("choose: "))
        match x2:
            case 1:
                obj1.greenary()
            case 2:
                obj1.black()
    case 3:
        obj2=printphto()
        print('1.passportsize photo')
        print('2.postcardsize photo')
        print('3.large photo')
        x3=int(input('choose: '))
        match x3:
            case 1:
                obj2.passportsize()
            case 2:
                obj2.postcardsize()
            case 3:
                obj2.largephoto()





