from PIL import Image
import shutil
import file_manager

def to_webp(file_path):
    image = Image.open(file_path)
    image.convert('RGB')
    image.save(f'{file_path}.webp',
               'webp',
               lossless=False,
               method = 6,
               quality = 80)


def to_cbz(folder_path):
    shutil.make_archive(folder_path, 'zip', folder_path)
    file_manager.rename_cbz(folder_path)
    file_manager.delete(folder_path)