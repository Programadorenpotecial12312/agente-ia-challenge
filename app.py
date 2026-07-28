import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader

st.set_page_config(page_title="Agente Inteligente - Q&A", page_icon="🤖")
st.title("🤖 Agente Inteligente de Preguntas y Respuestas")
st.write(
    "Este agente responde preguntas basándose en un documento (PDF o CSV) "
    "usando búsqueda por similitud semántica (RAG simplificado con TF-IDF)."
)

DEFAULT_CSV = "data/conocimiento.csv"


def cargar_csv(fuente):
    return pd.read_csv(fuente)


def cargar_pdf(fuente):
    reader = PdfReader(fuente)
    texto_completo = ""
    for pagina in reader.pages:
        contenido = pagina.extract_text()
        if contenido:
            texto_completo += contenido + "\n"
    fragmentos = [f.strip() for f in texto_completo.split("\n") if len(f.strip()) > 30]
    return pd.DataFrame({"pregunta": fragmentos, "respuesta": fragmentos})


st.sidebar.header("Documento fuente")
archivo = st.sidebar.file_uploader("Sube tu propio PDF o CSV (opcional)", type=["pdf", "csv"])

if archivo is not None:
    if archivo.name.endswith(".csv"):
        df = cargar_csv(archivo)
    else:
        df = cargar_pdf(archivo)
    st.sidebar.success(f"Documento cargado: {archivo.name}")
else:
    df = cargar_csv(DEFAULT_CSV)
    st.sidebar.info("Usando base de conocimiento por defecto (demo SaaS).")

vectorizer = TfidfVectorizer()
matriz_preguntas = vectorizer.fit_transform(df["pregunta"].astype(str))

pregunta_usuario = st.text_input("Escribe tu pregunta:")

if pregunta_usuario:
    vector_usuario = vectorizer.transform([pregunta_usuario])
    similitudes = cosine_similarity(vector_usuario, matriz_preguntas)[0]
    indice_mejor = similitudes.argmax()
    score = similitudes[indice_mejor]

    if score < 0.05:
        st.warning("No encontré información relacionada en el documento.")
    else:
        st.markdown(f"**Respuesta:** {df.iloc[indice_mejor]['respuesta']}")
        st.caption(f"Nivel de coincidencia: {score:.2f}")

st.divider()
st.caption("Ejemplos de preguntas: '¿Qué planes de precios ofrece TaskFlow?', '¿Cómo cancelo mi suscripción?'")
