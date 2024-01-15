import numpy as np

def normalize(arr, min_nor, max_nor):
    normalized_array = np.zeros(arr.size, dtype=np.float32)
    diff_nor = max_nor - min_nor
    arr_min = min(arr)
    diff_arr = max(arr) - arr_min
    for i in range(arr.size):
        temp = (((arr[i] - arr_min)*diff_nor)/diff_arr) + min_nor
        normalized_array[i] = temp
    return normalized_array

def combine_tracks(tracks: list):
    max_track_length = 0
    for track in tracks:
        max_track_length = max(max_track_length, track.size)
        
    master_track = np.zeros(max_track_length, dtype=np.float32)
    
    for track in tracks:
        if track.size < max_track_length:
            track = np.concatenate((track, np.zeros(max_track_length - track.size, dtype=np.float32)))
        master_track += track
        
    print(1)
    master_track = normalize(master_track, -1, 1)
        
    return master_track
