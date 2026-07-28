# 🤖 Agente Inteligente de Preguntas y Respuestas (RAG)

Agente que responde preguntas en lenguaje natural basándose en un documento (PDF o CSV) mediante búsqueda por similitud (RAG simplificado con TF-IDF).

## Descripción general

Este proyecto implementa un chatbot de preguntas y respuestas para una plataforma SaaS ficticia (TaskFlow). El agente lee una base de conocimiento (FAQ, políticas, precios, términos de uso) y responde preguntas del usuario devolviendo el fragmento más relevante del documento.

## Arquitectura

```
Usuario → Interfaz Streamlit → Vectorización TF-IDF → Similitud coseno → Fragmento más relevante → Respuesta
```

1. El documento (CSV o PDF) se carga y se convierte en fragmentos de texto.
2. Cada fragmento se convierte en un vector numérico (TF-IDF).
3. La pregunta del usuario también se convierte en vector.
4. Se calcula la similitud coseno entre la pregunta y todos los fragmentos.
5. Se devuelve el fragmento con mayor similitud como respuesta.

## Herramientas y tecnologías

- **Python 3.11**
- **Streamlit** — interfaz web
- **pandas** — manejo de datos tabulares (CSV)
- **scikit-learn** — vectorización TF-IDF y similitud coseno
- **PyPDF2** — extracción de texto de PDF
- **Oracle Cloud Infrastructure (OCI)** — despliegue en máquina virtual

## Instalación

```bash
git clone https://github.com/TU-USUARIO/agente-ia-challenge.git
cd agente-ia-challenge
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

Abrir en el navegador: `http://localhost:8501`

## Ejemplos de preguntas

- ¿Qué planes de precios ofrece TaskFlow?
- ¿Cómo puedo cancelar mi suscripción?
- ¿TaskFlow ofrece una prueba gratuita?
- ¿Qué política de privacidad tiene TaskFlow?

## Ejemplos de respuestas

**Pregunta:** ¿Cómo puedo cancelar mi suscripción?
**Respuesta:** Puedes cancelar tu suscripción en cualquier momento desde Configuración > Facturación > Cancelar plan. La cancelación se hace efectiva al final del ciclo de facturación en curso.

## Estructura del proyecto

```
agente-ia-challenge/
├── app.py                  # Aplicación Streamlit (agente)
├── requirements.txt        # Dependencias
├── data/
│   └── conocimiento.csv    # Base de conocimiento (FAQ SaaS)
├── README.md
└── .gitignore
```

## Despliegue

Aplicación desplegada en una máquina virtual de Oracle Cloud Infrastructure (OCI), accesible mediante IP pública en el puerto 8501.

**URL de demo:** _agregar aquí el enlace público tras el despliegue_
