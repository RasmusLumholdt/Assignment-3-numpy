import numpy as np

def get_data_arr(filename="kkdata.csv"):
    return np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)


def find_native_and_non_native_english_speakers():
    data = get_data_arr()
    year = 2015
    #Some arbitrary native enligh countries were chosen, not all.
    english_mask = ((data[:,0] == year) & ((data[:,3] == 5142) | (data[:,3] == 5397) | (data[:,3] == 5170)))
    native = np.sum(data[english_mask][:,4])


    non_native_mask = ((data[:,0] == year) & (data[:,3] != 5142) & (data[:,3] != 5397) & (data[:,3] != 5170))
    non_native = np.sum(data[non_native_mask][:,4])
    return native, non_native

def mask_certain_data(data, mask):
    return data[mask]

def accum_val_from_filter(data, mask):
    masked_data = data[mask]

    return np.sum(masked_data[:,4])

