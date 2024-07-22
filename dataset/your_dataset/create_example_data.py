import numpy as np
import tqdm
import os

N_TRAIN_EPISODES = 100
N_VAL_EPISODES = 100

EPISODE_LENGTH = 10


def create_fake_episode(path):
    episode = []
    for step in range(EPISODE_LENGTH):
        episode.append({
            'image': np.asarray(np.random.rand(64, 64, 3) * 255, dtype=np.uint8),
            'wrist_image': np.asarray(np.random.rand(64, 64, 3) * 255, dtype=np.uint8),
            'state': np.asarray(np.random.rand(10), dtype=np.float32),
            'action': np.asarray(np.random.rand(10), dtype=np.float32),
            'language_instruction': 'dummy instruction',
        })
    np.save(path, episode)


# create fake episodes for train and validation
print("Generating train examples...")
folder_path = '../../../dataset/dummy_data/'

os.makedirs(folder_path + 'train', exist_ok=True)
for i in tqdm.tqdm(range(N_TRAIN_EPISODES)):
    create_fake_episode(folder_path + f'train/episode_{i}.npy')

print("Generating val examples...")
os.makedirs(folder_path + 'val', exist_ok=True)
for i in tqdm.tqdm(range(N_VAL_EPISODES)):
    create_fake_episode(folder_path + f'val/episode_{i}.npy')

print('Successfully created example data!')
