import streamlit as st
from utils.prompt_generator import generate_prompt
from utils.cost_links import get_selected_cost_links
from utils.model_loader import load_model
import torch

st.set_page_config(page_title="AI Interior Designer", layout="wide")

# Load model
pipe = load_model()

st.title("🧠 AI–Driven Virtual Interior Designer")
st.write("Select your preferences and generate a high-quality interior design idea with cost insights.")

# Dropdown Options
room_types = ["Living Room", "Bedroom", "Kitchen", "Dining Room", "Bathroom", "Office Room"]
adjectives = ["Large", "Comfortable", "Simple", "Fancy", "Bright", "Stylish"]
architectures = ["Modern", "Classic", "Scandinavian", "Tropical", "Colonial"]
themes = ["Minimalist", "Industrial", "Farmhouse", "Mid-Century", "Art Style"]
colors = ["blue", "green", "beige", "grey", "white", "black", "mustard", "olive"]
woods = ["oak", "walnut", "pine", "cherry", "mahogany"]
walls = ["cream", "off-white", "charcoal", "mustard yellow", "warm beige"]
tiles = ["marble", "ceramic", "wooden-look", "mosaic", "granite"]

# UI Layout
col1, col2 = st.columns(2)
with col1:
    room = st.selectbox("Room Type", room_types)
    adjective = st.selectbox("Adjective", adjectives)
    architecture = st.selectbox("Architecture Style", architectures)
with col2:
    theme = st.selectbox("Interior Theme", themes)
    accent_color = st.selectbox("Accent Color", colors)
    wood = st.selectbox("Wood Finish", woods)
    wall = st.selectbox("Wall Color", walls)
    tile = st.selectbox("Tile Type", tiles)

if st.button("✨ Generate Design & Estimate Costs", use_container_width=True):
    prompt = generate_prompt(room, adjective, architecture, theme, accent_color, wood, wall, tile)
    st.markdown(f"**Generated Prompt:** `{prompt}`")

    with st.spinner("Generating..."):
        image = pipe(prompt, guidance_scale=7, num_inference_steps=20, width=640, height=640).images[0]
        st.image(image, caption="Generated Interior Design", width=500)

        
        st.subheader("💰 Material Cost Estimations")
        st.markdown(get_selected_cost_links(accent_color, wood, wall, tile), unsafe_allow_html=True)
