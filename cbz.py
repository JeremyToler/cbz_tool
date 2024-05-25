#TODO Add ability to unzip CBZ, convert to webp, and rezip
import sys
import files
import compress


def main(file_path):
    comic_dict = files.get_dict(file_path)
    print(comic_dict)
    files.rename(file_path, comic_dict)
    compress.to_webp()
    compress.to_cbz()
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('Please enter path to folders you want to convert')
    main(file_path)