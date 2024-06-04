import sys
import os
import file_manager
import compress

def main(source, dest):
    exts = ['.zip', '.7z', '.rar', '.tar.bz2', '.tar.gz', '.tar.xz',
            '.cbz', '.cb7', '.cbr', '.cbt']
    file_manager.copy_everything(source, dest)
    folders = file_manager.get_folders(dest)
    for folder in folders:
        folder_path = os.path.join(dest, folder)
        if any(folder.lower().endswith(ext) for ext in exts):
            archive_path = folder_path
            folder_path = os.path.join(dest, file_manager.no_ext(folder))
            compress.unzip(archive_path, folder_path)
        files = file_manager.get_files(folder_path)
        file_count = len(files)
        if file_count < 1:
            file_manager.delete(folder_path)
            continue
        for i in range(file_count):
            if files[i].lower().endswith('.webp'):
                continue
            file_path = os.path.join(folder_path, files[i])
            compress.to_webp(file_path)
            file_manager.rename_webp(file_path, file_count, folder_path, i)
        compress.to_cbz(folder_path)
    

if __name__ == '__main__':
    if len(sys.argv) == 3:
        source, dest = sys.argv[1], sys.argv[2]
    else:
        print('This script requires 2 arguments')
        print('python cbz.py /source/path /destination/path')
    main(source, dest)