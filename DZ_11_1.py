import glob, os
from PIL import Image



im = Image.open('image.png')
print(f'im: {im.format}, {im.size}, {im.mode}')
im.show()
im = im.convert('RGB')
im.thumbnail((600,600))
im.convert('RGB')
im.save('image_converted.jpg')

# Скрипт ищет файлы с расширением .png в папке Images, изменяет их размер на 800x600 и переводит их в .jpg
# сохраняет файлы в папке converted
size = 800, 600
for infile in glob.glob("Images/*.png"):
    files_list  = infile.split('/')
    file, ext = os.path.splitext(files_list[1])
    im = Image.open(infile).resize(size)
    current_dir = os.getcwd()
    dir_name = current_dir + '/Images/converted'

    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)
    im.convert('RGB').save('./Images/converted/' + file + ".jpg", "JPEG")




