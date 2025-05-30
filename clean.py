import os
import sys

if len(sys.argv) < 2:
    print('Directory path expected as an argument. Please try again with the path included.')
    sys.exit(1)

directory_name = sys.argv[1]

dir_path = os.path.abspath(directory_name)

file_names = ['setup','stp','install','installer','installation']

def generate_file_dict(directory):
    files_dict = {}
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(('.exe','.msi')):
                filename_lowercase = file.lower()
                if any(file_name in filename_lowercase for file_name in file_names):
                    full_path = os.path.join(root,file)
                    try:
                        size = os.path.getsize(full_path)
                        files_dict[full_path] = round(size/(1024**2),2)
                    except OSError as e:
                        print(f'Failed to load {full_path} file size, {e}')
    return files_dict

if __name__ == "__main__":
    files_dict = generate_file_dict(dir_path)
    for path, size in files_dict.items():
        print(f"{path}: {size} MB")
    print(f'Total setup files size is ≈ {sum(files_dict.values())} MB')
