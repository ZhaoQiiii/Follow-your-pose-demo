#!/usr/bin/env python

from __future__ import annotations

import os

import gradio as gr

from inference_followyourpose import merge_config_then_run


# TITLE = '# [FateZero](http://fate-zero-edit.github.io/)'
HF_TOKEN = os.getenv('HF_TOKEN')
# pipe = InferencePipeline(HF_TOKEN)
pipe = merge_config_then_run()
# app = InferenceUtil(HF_TOKEN)

with gr.Blocks(css='style.css') as demo:
    # gr.Markdown(TITLE)
    
    gr.HTML(
    """
    <div style="text-align: center; max-width: 1200px; margin: 20px auto;">
    <h1 style="font-weight: 900; font-size: 2rem; margin: 0rem">
        🕺🕺🕺 Follow Your Pose 💃💃💃 </font></center> <br> <center>Pose-Guided Text-to-Video Generation using Pose-Free Videos
    </h1>
    <h2 style="font-weight: 450; font-size: 1rem; margin: 0rem">
            <a href="https://mayuelala.github.io/">Yue Ma*</a>
            <a href="https://github.com/YingqingHe">Yingqing He*</a> , <a href="http://vinthony.github.io/">Xiaodong Cun</a>, 
            <a href="https://xinntao.github.io/"> Xintao Wang </a>,
            <a href="https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=zh-CN">Ying Shan</a>,
            <a href="https://scholar.google.com/citations?user=Xrh1OIUAAAAJ&hl=zh-CN">Xiu Li</a>,
            <a href="http://cqf.io">Qifeng Chen</a>
    </h2>

    <h2 style="font-weight: 450; font-size: 1rem; margin: 0rem">
                  <span class="link-block">
                    [<a href="https://arxiv.org/abs/2304.01186" target="_blank"
                    class="external-link ">
                    <span class="icon">
                      <i class="ai ai-arxiv"></i>
                    </span>
                    <span>arXiv</span>
                  </a>]
                </span>

                  <!-- Github link -->
                  <span class="link-block">
                    [<a href="https://github.com/mayuelala/FollowYourPose" target="_blank"
                    class="external-link ">
                    <span class="icon">
                      <i class="fab fa-github"></i>
                    </span>
                    <span>Code</span>
                  </a>]
                </span>

                <!-- Github link -->
                  <span class="link-block">
                    [<a href="https://follow-your-pose.github.io/" target="_blank"
                    class="external-link ">
                    <span class="icon">
                      <i class="fab fa-github"></i>
                    </span>
                    <span>Homepage</span>
                  </a>]
                </span>
    </h2>
    <h2 style="font-weight: 450; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0.5rem">
        TL;DR: We tune 2D stable-diffusion to generate the character videos from pose and text description.
    </h2>
    </div>
    """)


    gr.HTML("""
    <p>Alternatively, try our GitHub <a href=https://github.com/mayuelala/FollowYourPose> code  </a> on your GPU.
    </p>""")

    with gr.Row():
        with gr.Column():
            with gr.Accordion('Input Video', open=True):
                # user_input_video = gr.File(label='Input Source Video')
                user_input_video = gr.Video(label='Input Source Video', source='upload', type='numpy', format="mp4", visible=True).style(height="auto")
                with gr.Accordion('Temporal Crop offset and Sampling Stride', open=False):
                    n_sample_frame = gr.Slider(label='Number of Frames',
                                        minimum=0,
                                        maximum=32,
                                        step=1,
                                        value=8)
                    stride = gr.Slider(label='Temporal stride',
                                            minimum=0,
                                            maximum=20,
                                            step=1,
                                            value=1)
                    start_sample_frame = gr.Number(label='Start frame in the video',
                              value=0,
                              precision=0)

                with gr.Accordion('Spatial Crop offset', open=False):
                    left_crop = gr.Number(label='Left crop',
                              value=0,
                              precision=0)
                    right_crop = gr.Number(label='Right crop',
                              value=0,
                              precision=0)
                    top_crop = gr.Number(label='Top crop',
                              value=0,
                              precision=0)
                    bottom_crop = gr.Number(label='Bottom crop',
                              value=0,
                              precision=0)
                    offset_list = [
                         left_crop,
                         right_crop,
                         top_crop,
                         bottom_crop,
                    ]
                
                ImageSequenceDataset_list = [
                   start_sample_frame,
                   n_sample_frame,
                   stride
                ] + offset_list
                
                # model_id = gr.Dropdown(
                #     label='Model ID',
                #     choices=[
                #         'CompVis/stable-diffusion-v1-4',
                #         # add shape editing ckpt here
                #     ],
                #     value='CompVis/stable-diffusion-v1-4')


            with gr.Accordion('Text Prompt', open=True):

                # source_prompt = gr.Textbox(label='Source Prompt',
                #                     info='A good prompt describes each frame and most objects in video. Especially, it has the object or attribute that we want to edit or preserve.',
                #                     max_lines=1,
                #                     placeholder='Example: "a silver jeep driving down a curvy road in the countryside"',
                #                     value='a silver jeep driving down a curvy road in the countryside')
                target_prompt = gr.Textbox(label='Target Prompt',
                                    info='A reasonable composition of video may achieve better results(e.g., "sunflower" video with "Van Gogh" prompt is better than "sunflower" with "Monet")',
                                    max_lines=1,
                                    placeholder='Example: "watercolor painting of a silver jeep driving down a curvy road in the countryside"',
                                    value='watercolor painting of a silver jeep driving down a curvy road in the countryside')





            run_button = gr.Button('Generate')

        with gr.Column():
            result = gr.Video(label='Result')
            # result.style(height=512, width=512)
            # with gr.Accordion('FateZero Parameters for attention fusing', open=True):
                # cross_replace_steps = gr.Slider(label='Cross-att replace steps',
                #                 info='More steps, replace more cross attention to preserve semantic layout.',
                #                 minimum=0.0,
                #                 maximum=1.0,
                #                 step=0.1,
                #                 value=0.7)
                
                # self_replace_steps = gr.Slider(label='Self-att replace steps',
                #                 info='More steps, replace more spatial-temporal self-attention to preserve geometry and motion.',
                #                 minimum=0.0,
                #                 maximum=1.0,
                #                 step=0.1,
                #                 value=0.7)
                
                # enhance_words = gr.Textbox(label='Enhanced words',
                #                     info='Amplify the target-words cross attention',
                #                     max_lines=1,
                #                     placeholder='Example: "watercolor "',
                #                     value='watercolor')

                # enhance_words_value = gr.Slider(label='Target cross-att amplification',
                #                 info='larger value, more elements of target words',
                #                 minimum=0.0,
                #                 maximum=20.0,
                #                 step=1,
                #                 value=10)
            with gr.Accordion('DDIM Parameters', open=True):
                num_steps = gr.Slider(label='Number of Steps',
                                      info='larger value has better editing capacity, but takes more time and memory.',
                                      minimum=0,
                                      maximum=50,
                                      step=1,
                                      value=50)
                guidance_scale = gr.Slider(label='CFG Scale',
                                           minimum=0,
                                           maximum=50,
                                           step=0.1,
                                           value=12.5)
    with gr.Row():
        from example import style_example
        examples = style_example


    inputs = [
            user_input_video,
            target_prompt,
            num_steps,
            guidance_scale,
            *ImageSequenceDataset_list
    ]
    target_prompt.submit(fn=pipe.run, inputs=inputs, outputs=result)
    run_button.click(fn=pipe.run, inputs=inputs, outputs=result)

demo.queue().launch(share=False, server_name='0.0.0.0', server_port=80)
