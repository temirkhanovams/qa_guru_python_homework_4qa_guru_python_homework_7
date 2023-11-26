import zipfile
import pytest
from utils import *


@pytest.fixture(scope="session", autouse=True)
def test_create_zip():
    if not os.path.isdir(path_tmp): os.mkdir(path_tmp)
    if os.path.exists(path_root_zip): os.remove(path_root_zip)

    with zipfile.ZipFile(path_tmp_zip, mode='w') as zf:
        for file in os.listdir(path_resources):
            add_file = os.path.join(path_resources, file)
            zf.write(add_file, arcname=file)
    # yield
    #
    # shutil.rmtree(path_tmp)
