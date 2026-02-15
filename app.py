import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageDraw
import time
from datetime import datetime

st.set_page_config(page_title="SafeGuard AI", layout="wide", page_icon="👷")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

if 'violations' not in st.session_state:
    st.session_state.violations = 0

st.title("👷 SafeGuard AI | Workplace Vision Monitor")
st.write("Computer Vision Compliance System - PPE Detection Node")

col_video, col_stats = st.columns([2, 1])

with col_video:
    st.subheader("Live Safety Feed")
    # Simulate a processed frame
    img = Image.new('RGB', (800, 480), color = (20, 25, 35))
    draw = ImageDraw.Draw(img)
    
    # Simulate Detection Logic
    is_safe = np.random.random() > 0.2
    box_color = "green" if is_safe else "red"
    label = "WORKER: COMPLIANT" if is_safe else "VIOLATION: NO HELMET"
    
    # Draw simulated bounding boxes
    draw.rectangle([250, 100, 550, 400], outline=box_color, width=5)
    draw.text((250, 80), label, fill=box_color)
    
    st.image(img, use_container_width=True)

with col_stats:
    st.subheader("Site Analytics")
    st.metric("Total Personnel On-Site", "12")
    st.metric("Safety Compliance Rate", "92%", delta="-2%")
    
    if not is_safe:
        st.session_state.violations += 1
        st.error(f"🚨 ALERT: Safety Breach detected in Sector 7 at {datetime.now().strftime('%H:%M:%S')}")

    st.subheader("Compliance History")
    log_data = pd.DataFrame({
        "Timestamp": [datetime.now().strftime("%H:%M:%S")],
        "Zone": ["Main Floor"],
        "Issue": ["None" if is_safe else "Missing PPE"]
    })
    st.table(log_data)

time.sleep(1)
st.rerun()
