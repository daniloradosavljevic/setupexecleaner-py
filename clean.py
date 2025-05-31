import os
import sys

if len(sys.argv) < 2:
    print('Directory path expected as an argument. Please try again with the path included.')
    sys.exit(1)

directory_name = sys.argv[1]

dir_path = os.path.abspath(directory_name)

file_names = ['setup','stp','install','installer','installation']

def clean(files_dict):
    deleted_count = 0
    for path in files_dict:
        try:
            os.remove(path)
            deleted_count += 1
            print(f'Deleted: {path}')
        except OSError as e:
          print(f"Failed to delete {path}: {e}")
    if deleted_count == 0:
        print("No files were deleted.")
    else:
        print(f"Successfully deleted {deleted_count} file{'s' if deleted_count != 1 else ''}.")


def generate_files_dict(directory):
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

def print_file_info(files_dict):
    print('Files found:')
    for path, size in files_dict.items():
        print(f"{path}: {size} MB")
    print(f'Total setup files size is ≈ {round(sum(files_dict.values()),2)} MB')
    confirm = input("To delete all the files listed above type 'y', to select which ones to delete type 's', to cancel deletion type 'n': ").strip().lower()
    if confirm == 'y':
        clean(files_dict)
    elif confirm == 's':
        new_dict = select_files_to_delete(files_dict)
        clean(new_dict)
    elif confirm == 'n':
        print('Deletion canceled')
    else:
        print("Invalid input. Please enter 'y' (yes), 's' (select), or 'n' (no).")

def select_files_to_delete(files_dict):
    new_dict = {}
    for path,size in files_dict.items():
        confirm = input(f'Do you really want to delete {path} (y/n): ').strip().lower()
        if confirm == 'y':
            new_dict[path] = files_dict[path]
            print(f'Selected {path}')
        else:
            print(f'Skipped {path}')
    return new_dict

if __name__ == "__main__":
    files_dict = generate_files_dict(dir_path)
    print_file_info(files_dict)
   
