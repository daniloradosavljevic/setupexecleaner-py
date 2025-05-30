import os
import sys

if len(sys.argv) < 2:
    print('Directory path expected as an argument. Please try again with the path included.')
    sys.exit(1)

directory_name = sys.argv[1]

dir_path = os.path.abspath(directory_name)

file_names = ['setup','stp','install','installer','installation']

def clean(directory):
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(('.exe','.msi')):
                filename_lowercase = file.lower()
                if any(file_name in filename_lowercase for file_name in file_names):
                    print(os.path.join(root,file))

if __name__ == "__main__":
    clean(dir_path)