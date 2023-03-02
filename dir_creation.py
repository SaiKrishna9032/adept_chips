import os

def log_directory_creation():
    LOG_DIR = 'dead'
    try:
        print("creating a directory...")
        os.makedirs('sai')
        print("directory is created.")
    except FileExistsError as e:
        print('WARNING: NOT Created.')
        pass
    return LOG_DIR
log_directory_creation()