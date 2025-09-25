import os

def get_files_info(working_directory, directory="."):
    
    abs_working_dir= os.path.abspath(working_directory)
    abs_directory=""
    if directory is None:
        abs_directory = os.path.abspath(working_directory)
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    # print(f"Working dir: {abs_working_dir}, Target dir: {abs_directory} test:{abs_directory.startswith(abs_working_dir)}")
    
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    final_res = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size= os.path.getsize(content_path)
        final_res += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"
    return final_res