# :scissors: AClip2 

Image Resize, Background Removal, Conversion to PNG(300DPI,SVG) and ZIP Archiving. 

Useful for automating the batch process of creating ClipArt packs from a folder of Images, for upload to marketplaces such as Etsy to be sold as digital products.

This repository contains two Python scripts to automate the process of resizing images, removing backgrounds from them, creating 300DPI PNG files and SVG files, and creating zip archives for the processed images (one for PNG, one for SVG).

## aclip2.py

The `aclip2.py` script is used to remove backgrounds from images in a specified folder, resize the images, and save them as PNG and SVG files. The processed images are saved in a subfolder named `aclip-output` within the input folder.

### Usage

```bash
python aclip2.py <input_folder> <project_name>
```

- `<input_folder>`: The folder containing the images you want to process.
- `<project_name>`: The name that will be used as a prefix when saving the processed images.

The script requires the following dependencies:

- `Pillow`
- `svgwrite`
- `rembg` command line tool

Make sure to install the dependencies before running the script.

## zipem.py

The `zipem.py` script is used to create zip archives for the processed images. It creates separate zip files for PNG and SVG images.

### Usage

```bash
python zipem.py <input_folder> <project_name>
```

- `<input_folder>`: The folder containing the processed images (same as the input folder used with `aclip2.py`).
- `<project_name>`: The name that will be used as a prefix for the zip files.

## Workflow

1. Run the `aclip2.py` script to process the images:

   ```bash
   python aclip2.py <input_folder> <project_name>
   ```

2. Run the `zipem.py` script to create zip archives for the processed images:

   ```bash
   python zipem.py <input_folder> <project_name>
   ```

After running both scripts, you will have two zip files (`<project_name>-png.zip` and `<project_name>-svg.zip`) containing the processed PNG and SVG images in the input folder.

