import os
import sys
import zipfile

def get_files_with_ext(folder_path, ext):
    ext = ext.lower()
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(ext)]
    print(f"Found {len(files)} files with extension {ext}: {files}")  # Print the number of files found and their paths
    return files



def zip_files(files, output_name, project_name):
    with zipfile.ZipFile(output_name, 'w') as zipf:
        for index, file in enumerate(files, start=1):
            file_ext = os.path.splitext(file)[-1]
            new_file_name = f"{project_name}_{index}{file_ext}"
            print(f"Adding file: {file} as {new_file_name}")  # Print the file path and new_file_name
            zipf.write(file, new_file_name)



def zip_files_in_groups(folder_path, output_folder, file_ext, project_name, group_size=100):
    files = get_files_with_ext(folder_path, file_ext)
    num_groups = (len(files) + group_size - 1) // group_size

    for i in range(num_groups):
        group_files = files[i * group_size: (i + 1) * group_size]
        zip_name = f"{project_name}.zip"
        output_path = os.path.join(output_folder, zip_name)
        zip_files(group_files, output_path, project_name)
        print(f"Created {output_path}")

def main(input_folder, project_name):

    png_files = get_files_with_ext(input_folder, '.png')
    svg_files = get_files_with_ext(input_folder, '.svg')

    png_zip_name = f"{project_name}-png.zip"
    svg_zip_name = f"{project_name}-svg.zip"

    png_zip_path = os.path.join(input_folder, png_zip_name)
    svg_zip_path = os.path.join(input_folder, svg_zip_name)

    zip_files(png_files, png_zip_path, project_name)
    print(f"Created {png_zip_path}")

    zip_files(svg_files, svg_zip_path, project_name)
    print(f"Created {svg_zip_path}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <project_name>")
    else:
        input_folder = sys.argv[1]
        project_name = sys.argv[2]
        main(input_folder, project_name)
