# Copyright 2021 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import argparse
import os
import shutil

from PIL import Image
from tqdm import tqdm


def main():
    raw_inputs_image_dir = f"{args.output_dir}/temp/inputs"
    raw_target_image_dir = f"{args.output_dir}/temp/target"
    new_inputs_dir = f"{args.output_dir}/train/inputs"
    new_target_dir = f"{args.output_dir}/train/target"

    if os.path.exists(raw_inputs_image_dir):
        shutil.rmtree(raw_inputs_image_dir)
    if os.path.exists(raw_target_image_dir):
        shutil.rmtree(raw_target_image_dir)
    if os.path.exists(new_inputs_dir):
        shutil.rmtree(new_inputs_dir)
    if os.path.exists(new_target_dir):
        shutil.rmtree(new_target_dir)
    os.makedirs(raw_inputs_image_dir)
    os.makedirs(raw_target_image_dir)
    os.makedirs(new_inputs_dir)
    os.makedirs(new_target_dir)

    # Carry out data enhancement processing on the data set in the temp catalog in turn
    file_names = os.listdir(args.inputs_dir)
    for file_name in tqdm(file_names, total=len(file_names)):
        raw_image = Image.open(f"{args.inputs_dir}/{file_name}")

        index = 0
        for scale_ratio in [1.0, 0.9, 0.8, 0.7, 0.6]:
            for scale_factor in [2, 3, 4]:
                # Process HR image
                hr_image = raw_image.resize((int(raw_image.width * scale_ratio), int(raw_image.height * scale_ratio)), Image.BICUBIC)
                # Process LR image
                lr_image = hr_image.resize([hr_image.width // scale_factor, hr_image.height // scale_factor], Image.BICUBIC)
                lr_image = lr_image.resize([hr_image.width, hr_image.height], Image.BICUBIC)
                # Save all images
                lr_image.save(f"{raw_inputs_image_dir}/{file_name.split('.')[-2]}_{index:04d}.{file_name.split('.')[-1]}")
                hr_image.save(f"{raw_target_image_dir}/{file_name.split('.')[-2]}_{index:04d}.{file_name.split('.')[-1]}")
                index += 1
    print("Data augment successful.")

    file_names = os.listdir(raw_inputs_image_dir)
    for file_name in tqdm(file_names, total=len(file_names)):
        lr_image = Image.open(f"{raw_inputs_image_dir}/{file_name}")
        hr_image = Image.open(f"{raw_target_image_dir}/{file_name}")

        for pos_x in range(0, lr_image.size[0] - args.image_size + 1, args.step):
            for pos_y in range(0, lr_image.size[1] - args.image_size + 1, args.step):
                # crop box xywh
                crop_lr_image = lr_image.crop([pos_x, pos_y, pos_x + args.image_size, pos_y + args.image_size])
                crop_hr_image = hr_image.crop([pos_x, pos_y, pos_x + args.image_size, pos_y + args.image_size])
                # Save all images
                crop_lr_image.save(f"{new_inputs_dir}/{file_name.split('.')[-2]}_{pos_x}_{pos_y}.{file_name.split('.')[-1]}")
                crop_hr_image.save(f"{new_target_dir}/{file_name.split('.')[-2]}_{pos_x}_{pos_y}.{file_name.split('.')[-1]}")
    print("Data split successful.")

    shutil.rmtree(raw_inputs_image_dir)
    shutil.rmtree(raw_target_image_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare database scripts.")
    parser.add_argument("--inputs_dir", type=str, default="TB291/original", help="Path to input image directory. (Default: `TB291/original`)")
    parser.add_argument("--output_dir", type=str, default="TB291/VDSR", help="Path to generator image directory. (Default: `TB291/VDSR`)")
    parser.add_argument("--image_size", type=int, default=41, help="Low-resolution image size from raw image. (Default: 41)")
    parser.add_argument("--step", type=int, default=41, help="Crop image similar to sliding window.  (Default: 41)")
    args = parser.parse_args()

    main()
