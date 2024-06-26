import os
import shutil
from pathlib import Path

def copy_everything(source, dest):
    if os.path.isdir(dest):
        response = input(f'Overwrite {dest}? y/N:  ')
        if response.lower() == 'y':
            shutil.rmtree(dest)
    shutil.copytree(source, dest)


def get_folders(file_path):
    dirs = os.listdir(file_path)
    return dirs


def get_files(file_path):
    files = []
    exts = ['.png', '.jpg', '.jpeg', '.webp']
    try:
        raw_files = os.listdir(file_path)
    except:
        return files
    
    for file in raw_files:
        if any(file.lower().endswith(ext) for ext in exts):
            files.append(file)
        else:
            delete(os.path.join(file_path, file))

    files.sort()
    return files


def delete(file_path):
    try:
        os.remove(file_path)
    except:
        try:
            shutil.rmtree(file_path)
        except:
            print(f'Cannot remove {file_path}')


def rename_webp(old_file, new_file):
        shutil.copy(old_file, new_file)
        delete(old_file)


def no_ext(file_path):
    path = Path(file_path)
    return path.resolve().stem


def flatten_dir(old_file, folder_path):
    file = os.path.basename(old_file)
    new_file = os.path.join(folder_path, file)
    if not os.path.isfile(new_file):
        shutil.copy(old_file, new_file)
        delete(old_file)
