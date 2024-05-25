import os

def get_dict(file_path):
    file_dict = {}
    for root_dir, sub_dirs, filenames in os.walk(file_path):
        for dir in sub_dirs:
            sub_path = os.path.join(root_dir, dir)
            file_dict.update({dir: get_files(sub_path)})
    return file_dict


def get_files(file_path):
    files = []
    for root_dir, sub_dirs, filenames in os.walk(file_path):
        files = filenames.copy()
    files.sort()
    return files

def rename(file_path, file_dict):
    didgets = len(str(len(file_dict['test'])))