# streamlit_app.py
import streamlit as st
import os
import time

st.title("Simulación de Caída Libre")

altura = st.slider("Altura inicial (m)", min_value=1, max_value=100, value=20)

calidad = st.radio(
    "Seleccioná la calidad del video:",
    ("Baja (rápido)", "Media", "Alta (lento)"),
    index=0
)

# Mapear calidad a flags de Manim
calidad_flags = {
    "Baja (rápido)": "480p15",  # low quality
    "Media": "720p30",          # medium
    "Alta (lento)": "1080p60"   # high
}

manim_flags = {
    "Baja (rápido)": "-ql",
    "Media": "-qm",
    "Alta (lento)": "-qh"
}

if st.button("Generar animación"):
    with open("altura.txt", "w") as f:
        f.write(str(altura))

    flag = manim_flags[calidad]
    resolucion = calidad_flags[calidad]

    with st.spinner(f"Generando animación en calidad {calidad}..."):
        os.system(f"manim {flag} main.py Caida")

        # Construir la ruta del video según calidad
        video_path = f"media/videos/main/{resolucion}/CaidaLibre.mp4"

        time.sleep(1)

        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.error("No se encontró el video generado.")
