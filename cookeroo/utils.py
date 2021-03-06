import os


def _get_subdirectory_names(directory_path, exclude_hidden=True):
    try:
        subdirectories = next(os.walk(directory_path))[1]
        if exclude_hidden:
            subdirectories = list(filter(lambda folder_name: not str(folder_name).startswith('.'), subdirectories))
    except Exception:
        subdirectories = None
    return subdirectories


def _is_existing_dir(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        return True
    return False


def _clear_dir(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            os.remove(os.path.join(root, file))


def _get_file_paths(directory_path, extension=None):
    file_paths = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if not os.path.isfile(file_path):
            continue
        if extension is None or (extension is not None and file_path.endswith(extension)):
            file_paths.append(file_path)
    return file_paths
