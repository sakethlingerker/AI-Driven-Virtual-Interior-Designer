# import torch
# from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
# import streamlit as st

# # Cache the model loading to avoid reloading on every interaction
# @st.cache_resource
# def load_model():
#     model_id = "bhoomikagp/sd2-interior-model-version2"
#     scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
#     torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
#     device = "cuda" if torch.cuda.is_available() else "cpu"
 
#     # pipe = StableDiffusionPipeline.from_pretrained(
#     #     model_id,
#     #     scheduler=scheduler,
#     #     torch_dtype=torch_dtype
#     # ).to(device)
#     pipe = StableDiffusionPipeline.from_pretrained(
#     "CompVis/stable-diffusion-v1-4").to("cpu")

 
#     return pipe
from diffusers import StableDiffusionPipeline
import torch

@st.cache_resource
def load_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32  # safer for CPU
    ).to("cpu")
    pipe.enable_attention_slicing()
    return pipe