
from FollowYourPose.test_followyourpose import *

import copy
import gradio as gr
from transformers import AutoTokenizer, CLIPTextModel


def get_time_string() -> str:
    x = datetime.datetime.now()
    return f"{(x.year - 2000):02d}{x.month:02d}{x.day:02d}-{x.hour:02d}{x.minute:02d}{x.second:02d}"


class merge_config_then_run():
    def __init__(self) -> None:
            # Load the tokenizer
        # pretrained_model_path = 'FateZero/ckpt/stable-diffusion-v1-4'
        self.tokenizer = None
        self.text_encoder = None
        self.vae = None
        self.unet = None
        
        # cache_ckpt = False
        # if cache_ckpt:
        #     self.tokenizer = AutoTokenizer.from_pretrained(
        #         pretrained_model_path,
        #         # 'FateZero/ckpt/stable-diffusion-v1-4',
        #         subfolder="tokenizer",
        #         use_fast=False,
        #     )

        #     # Load models and create wrapper for stable diffusion
        #     self.text_encoder = CLIPTextModel.from_pretrained(
        #         pretrained_model_path,
        #         subfolder="text_encoder",
        #     )

        #     self.vae = AutoencoderKL.from_pretrained(
        #         pretrained_model_path,
        #         subfolder="vae",
        #     )
        #     model_config = {
        #         "lora": 160,
        #         # temporal_downsample_time: 4
        #         "SparseCausalAttention_index": ['mid'],
        #         "least_sc_channel": 640
        #     }
        #     self.unet = UNetPseudo3DConditionModel.from_2d_model(
        #         os.path.join(pretrained_model_path, "unet"), model_config=model_config
        #     )

    def run(
        self,
        data_path,
        target_prompt,
        num_steps,
        guidance_scale,
        user_input_video=None,
        start_sample_frame=0,
        n_sample_frame=8,
        stride=1,
        left_crop=0,
        right_crop=0,
        top_crop=0,
        bottom_crop=0,
    ):
        default_edit_config='FollowYourPose/configs/pose_sample.yaml'
        Omegadict_default_edit_config = OmegaConf.load(default_edit_config)
        
        dataset_time_string = get_time_string()
        config_now = copy.deepcopy(Omegadict_default_edit_config)
        # print(f"config_now['pretrained_model_path'] = model_id {model_id}")

        offset_dict = {
            "left": left_crop,
            "right": right_crop,
            "top": top_crop,
            "bottom": bottom_crop,
        }
        ImageSequenceDataset_dict = {
            "start_sample_frame" : start_sample_frame,
            "n_sample_frame" : n_sample_frame,
            "sampling_rate"       : stride,   
            "offset": offset_dict,
        }
        config_now['validation_data'].update(ImageSequenceDataset_dict)
        if user_input_video and data_path is None:
            raise gr.Error('You need to upload a video or choose a provided video')
        if user_input_video is not None:
            if isinstance(user_input_video, str):
                config_now['validation_data']['path'] = user_input_video
            elif hasattr(user_input_video, 'name') and user_input_video.name is not None:
                config_now['validation_data']['path'] = user_input_video.name
        config_now['validation_data']['prompts'] = [target_prompt]
        # ddim config
        config_now['validation_data']['guidance_scale'] = guidance_scale
        config_now['validation_data']['num_inference_steps'] = num_steps
        config_now['skeleton_path'] = data_path
        
        save_path = test(**config_now)
        mp4_path = save_path.replace('_0.gif', '_0_0_0.mp4')
        return mp4_path

