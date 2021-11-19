# Usage

## Download datasets

### Download train dataset

#### TB291

- Image format
    - [Google Driver](https://drive.google.com/drive/folders/13wiE6YqIhyix0RFxpFONJ7Zz_00CttdX?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1mhbFj0Nvwthmgx07Gas5BQ) access: `llot`

- LMDB format (train)
    - [Google Driver](https://drive.google.com/drive/folders/1BPqN08QHk_xFnMJWMS8grfh_vesVs8Jf?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1eqeORnKcTmGatx2kAG92-A) access: `llot`

- LMDB format (valid)
    - [Google Driver](https://drive.google.com/drive/folders/1bYqqKk6NJ9wUfxTH2t_LbdMTB04OUicc?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1W34MeEtLY0m-bOrnaveVmw) access: `llot`

### Download valid dataset

#### Set5

- Image format
    - [Google Driver](https://drive.google.com/file/d/1GJZztdiJ6oBmJe9Ntyyos_psMzM8KY4P/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1_B97Ga6thSi5h43Wuqyw0Q) access:`llot`

#### Set14

- Image format
    - [Google Driver](https://drive.google.com/file/d/14bxrGB3Nej8vBqxLoqerGX2dhChQKJoa/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1wy_kf4Kkj2nSkgRUkaLzVA) access:`llot`

#### BSD100

- Image format
    - [Google Driver](https://drive.google.com/file/d/1xkjWJGZgwWjDZZFN6KWlNMvHXmRORvdG/view?usp=sharing)
    - [Baidu Driver](https://pan.baidu.com/s/1EBVulUpsQrDmZfqnm4jOZw) access:`llot`

## Train dataset struct information

### Image format

```text
- TB291
    - VDSR
        - train
            - ...
        - valid
            - ...
```

### LMDB format

```text
- train_lmdb
    - VDSR
        - TB291_LRbicx2_lmdb
            - data.mdb
            - lock.mdb
        - TB291_HR_lmdb
            - data.mdb
            - lock.mdb
- valid_lmdb
    - VDSR
        - TB291_LRbicx2_lmdb
            - data.mdb
            - lock.mdb
        - TB291_HR_lmdb
            - data.mdb
            - lock.mdb
```

## Test dataset struct information

### Image format

```text
- Set5
    - GTmod12
        - baby.png
        - bird.png
        - ...
    - LRbicx4
        - baby.png
        - bird.png
        - ...
- Set14
    - GTmod12
        - baboon.png
        - barbara.png
        - ...
    - LRbicx4
        - baboon.png
        - barbara.png
        - ...
```
