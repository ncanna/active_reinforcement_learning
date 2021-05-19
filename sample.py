import os, glob
import shutil
import numpy as np

base_dir = ''

ds_dir = ''
dt_dir = ''
dv_dir = ''
set_list = [ds_dir, dt_dir, dv_dir]
move_files = False

#3 ds, 27 dt, 70 dv
def split_three(lst, ratio=[0.03, 0.27, 0.70]):
    train_r, val_r, test_r = ratio
    assert(np.sum(ratio) == 1.0)  # makes sure the splits make sense
    # only need to give 2 indices to split, the last one returns  rest of the list/empty list
    indicies_for_splitting = [int(len(lst) * train_r), int(len(lst) * (train_r+val_r))]
    ds, dt, dv = np.split(lst, indicies_for_splitting)
    return ds, dt, dv

ds, dt, dv = split_three(list)

if move_files:
    for target_dir in set_list:
        for file in os.listdir(base_dir):
            if file in target_dir:
                shutil.copy(os.path.join(base_dir, file), os.path.join(target_dir, file))
            else:
                print(f"File {file} not found in target directory.")

