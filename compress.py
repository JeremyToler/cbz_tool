from PIL import Image
import file_manager
from archivefile import ArchiveFile

def to_webp(file_path):
    image = Image.open(file_path)
    image.convert('RGB')
    image.save(f'{file_path}.webp',
               'webp',
               lossless=False,
               method = 6,
               quality = 80)
    file_manager.delete(file_path)


def to_cbz(folder_path):
    with ArchiveFile(f'{folder_path}.cbz', 'w') as archive:
        archive.writeall(folder_path)
    file_manager.delete(folder_path)


def unzip(archive_path, folder_path):
    with ArchiveFile (archive_path) as archive:
        files = archive.get_members()
        for file in files:
            if file.is_file:
                path = archive.extract(file, destination=folder_path)
                file_manager.flatten_dir(path, folder_path)
    file_manager.delete(archive_path)

