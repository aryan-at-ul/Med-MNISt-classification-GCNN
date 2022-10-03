import os
from monai.apps import download_and_extract


dir_path = os.path.dirname(os.path.realpath(__file__))

resource = "https://github.com/Project-MONAI/MONAI-extra-test-data/releases/download/0.8.1/MedNIST.tar.gz"
md5 = "0bc7306e7427e00ad1c5526a6677552d"

root_dir = os.path.join(dir_path, "data")

compressed_file = os.path.join(root_dir, "MedNIST.tar.gz")
data_dir = os.path.join(root_dir, "MedNIST")
if not os.path.exists(data_dir):
    download_and_extract(resource, compressed_file, root_dir, md5)


print("Done., data is saved to", root_dir)
