from pathlib import Path

def numerical_rename(file_paths, first_number, path_abs, file_type):
    i = first_number
    for image in file_paths:
        image.rename(path_abs + '\\' + str(i) + '.' + file_type)
        i += 1
    return i

print("Укажите полный путь до папки с изображениями")
path_abs = input()
path = Path(path_abs)

if(not(path.exists() and path.is_dir())):
    print("Указанного пути не существует или дан путь к файлу")
    exit()

png = list(path.glob('*.png'))
jpg = list(path.glob('*.jpg'))
jpeg = list(path.glob('*.jpeg'))

last_number = 1

if(len(png) > 0):
    last_number = numerical_rename(png, last_number, path_abs, 'png')
if(len(jpg) > 0):
    last_number = numerical_rename(jpg, last_number, path_abs, 'jpg')
if(len(jpeg) > 0):
    last_number = numerical_rename(jpeg, last_number, path_abs, 'jpeg')

print("Файлы переименованы")



