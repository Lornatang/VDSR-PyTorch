import os

# Prepare dataset
os.system("python3 ./prepare_dataset.py --inputs_dir ../data/TB291/original --output_dir ../data/TB291/VDSR/")

# Split train and valid
os.system("python3 ./split_train_valid_dataset.py --inputs_dir ../data/TB291/VDSR")

# Create LMDB database file
os.system("python3 ./create_lmdb_dataset.py --image_dir ../data/TB291/VDSR/train/inputs --lmdb_path ../data/train_lmdb/VDSR/TB291_LR_lmdb")
os.system("python3 ./create_lmdb_dataset.py --image_dir ../data/TB291/VDSR/train/target --lmdb_path ../data/train_lmdb/VDSR/TB291_HR_lmdb")

os.system("python3 ./create_lmdb_dataset.py --image_dir ../data/TB291/VDSR/valid/inputs --lmdb_path ../data/valid_lmdb/VDSR/TB291_LR_lmdb")
os.system("python3 ./create_lmdb_dataset.py --image_dir ../data/TB291/VDSR/valid/target --lmdb_path ../data/valid_lmdb/VDSR/TB291_HR_lmdb")
