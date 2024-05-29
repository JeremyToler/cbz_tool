import os
import shutil


def get_folders(file_path):
    dirs = os.listdir(file_path)
    return dirs


def get_files(file_path):
    files = []
    try:
        raw_files = os.listdir(file_path)
    except:
        return files
    
    for file in raw_files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            files.append(file)
        else:
            delete(file)

    files.sort()
    return files


def delete(file):
    print(f'DELETE:{file}')


def rename_webp(file, file_count, folder_path, i):
        didgets = len(str(file_count))
        old_file = f'{file}.webp'
        new_file = os.path.join(folder_path, f'{i:0{didgets}d}.webp')
        shutil.copy(old_file, new_file)
        delete(file)
        delete(f'{file}.webp')

def rename_cbz(folder_path):
    new_file = f'{folder_path}.cbz'
    old_file = f'{folder_path}.zip'
    shutil.copy(old_file, new_file)