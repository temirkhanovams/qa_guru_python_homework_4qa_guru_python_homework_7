import os

path_project_root = os.path.dirname(os.path.abspath(__file__))
path_resources = os.path.join(path_project_root, 'resources')
path_tmp = os.path.join(path_project_root, 'tmp')

path_root_zip = os.path.join(path_project_root, 'archive.zip')
path_tmp_zip = os.path.join(path_tmp, 'archive.zip')
