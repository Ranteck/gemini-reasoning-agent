# Gemini Reasoning Agent 🤖

Un agente de razonamiento inteligente implementado con Google's Gemini-Pro API que utiliza un enfoque de pensamiento en cadena para proporcionar respuestas más profundas y razonadas.

## 🌟 Características

- Procesamiento de múltiples pasos de razonamiento
- Temperatura dinámica para diferentes etapas de pensamiento
- Salida en streaming para visualizar el proceso de pensamiento
- Sistema de logging para seguimiento y depuración
- Manejo seguro de credenciales mediante variables de entorno

## 🛠️ Requisitos

- Python 3.7+
- Google Cloud Project con API Gemini habilitada
- API Key de Gemini

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Ranteck/gemini-reasoning-agent.git
cd gemini-reasoning-agent
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install google-generativeai python-dotenv
```

4. Configura las variables de entorno:
   - Crea un archivo `.env` en la raíz del proyecto
   - Añade tus credenciales:

```
GEMINI_API_KEY=your_api_key_here
MODEL=gemini-pro
```

## 🚀 Uso

1. Ejecuta el script principal:

```bash
python main.py
```

2. Ingresa un tema o pregunta cuando se te solicite
3. Especifica el número de ciclos de razonamiento deseados
4. El agente procesará la información en múltiples pasos:
   - Formulación inicial de instrucciones
   - Ciclos de razonamiento profundo
   - Síntesis final de insights

## 🤔 Cómo Funciona

El agente utiliza un proceso de tres etapas:

1. **Primer Agente** (Temperatura Baja):
   - Formula instrucciones detalladas y estructuradas
   - Mantiene el enfoque en la consistencia

2. **Segundo Agente** (Temperatura Alta):
   - Realiza razonamiento creativo
   - Explora diferentes ángulos del tema

3. **Tercer Agente** (Temperatura Muy Baja):
   - Sintetiza todos los insights
   - Produce una conclusión coherente y concisa

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor, siente libre de:

- Reportar bugs
- Sugerir nuevas características
- Enviar pull requests

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ⚠️ Nota Importante

Asegúrate de no compartir tu API key y de seguir las mejores prácticas de seguridad al manejar credenciales.
