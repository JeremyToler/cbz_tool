#TODO Add ability to unzip CBZ, convert to webp, and rezip
import sys
import os
import file_manager
import compress

def main(root_dir):
    folders = file_manager.get_folders(root_dir)
    for folder in folders:
        folder_path = os.path.join(root_dir, folder)
        files = file_manager.get_files(folder_path)
        file_count = len(files)
        if file_count < 1:
            continue
        for i in range(file_count):
            file_path = os.path.join(folder_path, files[i])
            compress.to_webp(file_path)
            file_manager.rename_webp(file_path, file_count, folder_path, i)
            file_manager.delete(file_path)
        compress.to_cbz(folder_path)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = input('Please enter path to folders you want to convert')
    main(root_dir)