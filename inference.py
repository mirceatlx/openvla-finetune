# Install minimal dependencies (`torch`, `transformers`, `timm`, `tokenizers`, ...)
# > pip install -r https://raw.githubusercontent.com/openvla/openvla/main/requirements-min.txt
from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image

import torch
import argparse

from prismatic.models.load import load_vla

def get_from_camera(...):
    # TODO: resize the image to the model's input size (224x224)
    pass

def robot_act(action, ...):
    pass

def main(config: dict):
    # Load processor
    processor = AutoProcessor.from_pretrained(config['model_path'], trust_remote_code=True)
    # Load model
    vla = load_vla(
        model_id_or_path=config['model_path'],
        cache_dir=config['cache_dir'],
        load_for_training=False,
    ).config['device']
    image: Image.Image = get_from_camera(...)
    prompt = "In: What action should the robot take to {<INSTRUCTION>}?\nOut:"

    # Predict Action (7-DoF; un-normalize for BridgeData V2)
    inputs = processor(prompt, image).to(config['device'], dtype=torch.bfloat16)
    action = vla.predict_action(**inputs, unnorm_key=config['unnorm_key'], do_sample=False)

    # Execute...
    robot_act(action)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Inference parameters for OpenVLA")
    parser.add_argument("--model_path", type=str, help="Local or HF Hub path to model")
    parser.add_argument("--cache_dir", type=str, help="Local cache directory for model")
    parser.add_argument("--unnorm_key", type=str, help="Key for un-normalizing actions")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu", help="Device to run model on")


    args = parser.parse_args()
    config = vars(args)
    main(config)
	
