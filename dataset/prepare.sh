: '
Script for cleaning and resizing your dataset.

Performs the preprocessing steps:
  1. Runs resize function to convert all datasets to 224x224 (if image resolution is larger) and jpeg encoding
  2. Fixes channel flip errors in a few datasets

To reduce disk memory usage during conversion, we download the datasets 1-by-1, convert them
and then delete the original.
We specify the number of parallel workers below -- the more parallel workers, the faster data conversion will run.
Adjust workers to fit the available memory of your machine, the more workers + episodes in memory, the faster.
The default values are tested with a server with ~120GB of RAM and 24 cores.
'

# DOWNLOAD_DIR=<your_download_dir>
# CONVERSION_DIR=<temporary_dir_for_conversion>
# arguments
DOWNLOAD_DIR=$1
CONVERSION_DIR=$2
N_WORKERS=20                  # number of workers used for parallel conversion --> adjust based on available RAM
MAX_EPISODES_IN_MEMORY=200    # number of episodes converted in parallel --> adjust based on available RAM

# increase limit on number of files opened in parallel to 20k --> conversion opens up to 1k temporary files
# in /tmp to store dataset during conversion
ulimit -n 20000

# format: [dataset_name, dataset_version, transforms]
DATASET_TRANSFORMS=(
    "your_dataset 1.0.0 resize_and_jpeg_encode"  # replace with your dataset name
)

for tuple in "${DATASET_TRANSFORMS[@]}"; do
  # Extract strings from the tuple
  strings=($tuple)
  DATASET=${strings[0]}
  VERSION=${strings[1]}
  TRANSFORM=${strings[2]}
  
  python3 modify_rlds_dataset.py --dataset=$DATASET --data_dir=$DOWNLOAD_DIR --target_dir=$CONVERSION_DIR --mods=$TRANSFORM --n_workers=$N_WORKERS --max_episodes_in_memory=$MAX_EPISODES_IN_MEMORY
  echo "Modification finished for ${DATASET}."
  echo "=============================="
  echo ""

done
