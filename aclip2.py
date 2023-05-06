import os
import sys
import subprocess
from PIL import Image
import svgwrite
import base64
import io

OUTPUT_FOLDER_SUFFIX = "aclip-output"

def get_images_from_folder(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

import tempfile

def remove_background(image_path):
    try:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_output:
            subprocess.run(["rembg", "i", image_path, temp_output.name], check=True)
            return Image.open(temp_output.name)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while removing background from {image_path}:")
        print(f"Return code: {e.returncode}")
        sys.exit(1)

def resize_image(image, size=(1000, 1000)):
    return image.resize(size, Image.LANCZOS)

def save_image(image, output_path, format='PNG'):
    if format == 'SVG':
        # Convert PIL Image to PNG bytes
        png_bytes = io.BytesIO()
        image.save(png_bytes, format='PNG', dpi=(300, 300))  # Set DPI
        png_bytes.seek(0)
        png_data = base64.b64encode(png_bytes.read()).decode('utf-8')

        # Create an SVG containing the PNG data
        svg = svgwrite.Drawing(output_path, profile='tiny', size=(image.width, image.height))
        svg.add(svg.image(href=f'data:image/png;base64,{png_data}', insert=(0, 0), size=(image.width, image.height)))

        # Save the SVG
        svg.save()
    else:
        image.save(output_path, format, dpi=(300, 300))  # Set DPI


def main(input_folder, project_name):
    output_folder = os.path.join(input_folder, OUTPUT_FOLDER_SUFFIX)
    os.makedirs(output_folder, exist_ok=True)

    image_files = get_images_from_folder(input_folder)

    for idx, image_path in enumerate(image_files):
        print(f"Processing image: {image_path}")
        png_output_path = os.path.join(output_folder, f"{project_name}_{idx + 1}.png")
        svg_output_path = os.path.join(output_folder, f"{project_name}_{idx + 1}.svg")

        image_without_bg = remove_background(image_path)
        resized_image = resize_image(image_without_bg)
        save_image(resized_image, png_output_path)
        save_image(resized_image, svg_output_path, format='SVG')

    print("Calling zipem output_folder:" + output_folder + " project_name:" + project_name)

    # Call script2.py after script1.py completes
    subprocess.call(["python", "zipem.py", output_folder, project_name])



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <project_name>")
    else:
        input_folder = sys.argv[1]
        project_name = sys.argv[2]
        main(input_folder, project_name)
