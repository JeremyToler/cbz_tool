
# CBZ Tool

Converts all sub-directories to CBZ's after deleting all non-images and converting all images into WEBP.  




## Usage/Examples

Cool David has a folder containing only folders of images that they want to compress to CBZ

```javascript
python cbz.py /home/cooldavid/downloads/comics
```

Jeremy is about to ruin his day by deleting a bunch of files that are not images. 
```javascript
python cbz.py /home/jeremy
```

This could be used with crontab to automate CBZ creation and file destruction, but it would probably be better and safer to obtain CBZ files from the beginning.
## Features

- Compresses JPEG, JPG and PNG files to WEBP
- Compresses subfolders that contain JPEG, JPG, PNG, or WEBP files to CBZ
- Deletes all files that are not JPEG, JPG, PNG, or WEBP
- Also deletes JPEG, JPG and PNG after converting them to WEBP
- Also deletes subdirectories



## FAQ

#### Is this safe to use?

No. You should probably back up any files before running this. 

#### Why delete everything instead of just moving the files to a new directory?

It is more convinient for my use case to delete the items.  I might change the code in the near future so that its more universaly useable. 

#### Has anyone actualy asked these questions?

No, I have no users. 



## Roadmap

- Stop deleting everything

- Unzip existing cbz's then convert images to WEBP and re-zip them

