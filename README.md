# Joint-Partition Group Attention for Skeleton-Based Action Recognition

This repository holds the Pytorch implementation of [Joint-Partition Group Attention for Skeleton-Based Action Recognition]() by Hu Cui, Tessai Hayama.

## Introduction

We propose Joint-Partition Group Attention (JPGA) to simultaneously capture correlations between joints and body parts of different granularity sizes for skeleton-based action recognition. Specifically, JPGA integrates the joint tokens according to the joint’s human body partition attributes and produces different body parts tokens (partition-tokens) with different granularities. Then the attention map of JPGA is computed from joint-token and partition-token of different granularity sizes to represent the relationship between joints and body parts. Based on  JPGA, we construct our Joint-Partition Former (JPFormer), and conduct  extensive experiments on NTU-RGB+D, NTU-RRB+D 120, and Northwestern UCLA datasets and achieve state-of-the-art results, which highlights the  effectiveness of our design and practice

## Prerequisites

This package has the following requirements:

* `Python 3.8`
* `Pytorch 1.12`

## Data Preparation

### Download four datasets:

1. **SHREC’17 Track** dataset from [http://www-rech.telecom-lille.fr/shrec2017-hand/](http://www-rech.telecom-lille.fr/shrec2017-hand/) 
   - First, extract all files to `/data/shrec/shrec17_dataset`
   
   - Then, run `python gen_traindataset.py` and `python gen_testdataset.py`
2. **DHG-14/28** dataset from [http://www-rech.telecom-lille.fr/DHGdataset/](http://www-rech.telecom-lille.fr/DHGdataset/)
   - First, extract all files to `./data/DHG14-28/DHG14-28_dataset`
   
   - Then, run `python python gen_dhgdataset.py`
3. **NTU RGB+D 60** Skeleton dataset from [https://rose1.ntu.edu.sg/dataset/actionRecognition/](https://rose1.ntu.edu.sg/dataset/actionRecognition/)
   - First, extract all skeleton files to `./data/ntu/nturgbd_raw`
   
   - Then, run `python get_raw_skes_data.py`, `python get_raw_denoised_data.py` and `python seq_transformation.py` in sequence
   
   - put the .npz file to ntu or ntu120 fold.
4. **NW-UCLA** dataset from [Download NW-UCLA dataset](https://www.dropbox.com/s/10pcm4pksjy6mkq/all_sqe.zip?dl=0) 
5. Put downloaded data into the following directory structure:
   
   ```
   - data/
     - shrec/
       - shrec17_dataset/
         - HandGestureDataset_SHREC2017/
           - gesture_1
             ...
     - DHG14-28/
       - DHG14-28_dataset/
         - gesture_1
           ...
     - NW-UCLA/
       - all_sqe
         ...
     - ntu/
       - NTU60_Xsub.npz
       - ...
     - ntu120/
       - NTU120_XSet.npz
       - ...
   
   ```

## Training

You can change the configuration in the yaml file and in the main function. 

### SHREC’17 Track dataset:

Run `python main.py --device 0 --config ./config/shrec/joint14.yaml`

### NTU RGB+D 60 dataset :

On cross-view, run `python main.py --device 0 --config ./config/nturgbd-cross-view/joint.yaml`  

On cross-subject, run `python main.py --device 0 --config ./config/nturgbd-cross-subject/joint.yaml`

### NTU RGB+D 120 dataset :

On cross-view, run `python main.py --device 0 --config ./config/nturgbd120-cross-view/joint.yaml`

On cross-subject, run `python main.py --device 0 --config ./config/nturgbd120-cross-subject/joint.yaml`

### NW-UCLA dataset:

Run `python main.py --device 0 --config ./config/ucla/joint.yaml`

## Testing

Run `python main.py --device 0 --config ./config/ntu_test/bm.yaml`

You need to specify the path value according to your own weights file.



# Citation
```python
@article{cui2024joint,
  title={Joint-Partition Group Attention for skeleton-based action recognition},
  author={Cui, Hu and Hayama, Tessai},
  journal={Signal Processing},
  volume={224},
  pages={109592},
  year={2024},
  publisher={Elsevier}
}
```
## Acknowledgement
This repo is based on

- [2s-AGCN](https://github.com/lshiwjx/2s-AGCN)
- [ST-GCN](https://github.com/yysijie/st-gcn)
