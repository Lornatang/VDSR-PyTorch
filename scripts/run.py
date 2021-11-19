import os

os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/train --lmdb_path train_lmdb/VDSR/TB291_HR_lmdb --upscale_factor 1")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/train --lmdb_path train_lmdb/VDSR/TB291_LRbicx2_lmdb --upscale_factor 2")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/train --lmdb_path train_lmdb/VDSR/TB291_LRbicx3_lmdb --upscale_factor 3")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/train --lmdb_path train_lmdb/VDSR/TB291_LRbicx4_lmdb --upscale_factor 4")

os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/valid --lmdb_path valid_lmdb/VDSR/TB291_HR_lmdb --upscale_factor 1")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/valid --lmdb_path valid_lmdb/VDSR/TB291_LRbicx2_lmdb --upscale_factor 2")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/valid --lmdb_path valid_lmdb/VDSR/TB291_LRbicx3_lmdb --upscale_factor 3")
os.system("python3 ./create_lmdb_dataset.py --image_dir TB291/VDSR/valid --lmdb_path valid_lmdb/VDSR/TB291_LRbicx4_lmdb --upscale_factor 4")
