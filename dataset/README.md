Based on [https://github.com/kpertsch/rlds_dataset_builder](https://github.com/kpertsch/rlds_dataset_builder).


## Converting your Own Dataset to RLDS

Now we can modify the provided example to convert your own data. Follow the steps below:

Rename Dataset: 
Change the name of the dataset folder from example_dataset to the name of your dataset (e.g. robo_net_v2), also change the name of example_dataset_dataset_builder.py by replacing example_dataset with your dataset's name (e.g. robo_net_v2_dataset_builder.py) and change the class name ExampleDataset in the same file to match your dataset's name, using camel case instead of underlines (e.g. RoboNetV2).

Then run in Terminal:

1) cd your_dataset

2) python3 create_example_data.py  # or collect data from real robot '

3) tfds build  # will generate RLDS dataset to /home/user_name/tensorflow_datasets/your_dataset, no idea how to change the generation path


## Transformation keys

```
TFDS_MOD_FUNCTIONS = {
    "resize_and_jpeg_encode": ResizeAndJpegEncode,
    "filter_success": FilterSuccess,
    "flip_image_channels": FlipImgChannels,
    "flip_wrist_image_channels": FlipWristImgChannels,
}
```

You can add your own transformation key here depending on the dataset.
