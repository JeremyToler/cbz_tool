
# CBZ Tool

Converts all sub-directories to CBZ's after converting all images into WEBP.  


## Usage/Examples

Cool David has a folder containing only folders of images that they want to compress to CBZ

```javascript
python cbz.py /home/cooldavid/downloads/comics /home/cooldavid/cbzs
```

Mega Jose has a server that automaticly downloads new comics, rad!  They use crontab to automate compressing the comics

```javascript
0 */2 * * * python cbz.py /home/megajose/comics/downloads /home/megajose/comics
```

## Features

- Compresses JPEG, JPG and PNG files to WEBP
- Compresses subfolders that contain JPEG, JPG, PNG, or WEBP files to CBZ
- Unzip existing cbz's then convert images to WEBP and re-zip them

