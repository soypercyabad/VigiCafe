# 🖱️ VigiCafe Mouse Keeper

¡Mantente "activo" automáticamente!  
Este pequeño programa evita que aplicaciones como Teams, Zoom o Slack te pongan en estado "ausente" simulando movimiento del mouse cada cierto tiempo.

---

## 🚀 ¿Qué hace?

- Simula un pequeño movimiento del mouse cada X segundos.
- Corre en segundo plano como ícono en la bandeja (junto al reloj).
- Te permite **Iniciar**, **Detener** y **Salir** desde un menú.
- Personalizable y con estructura profesional.

---

## 🧪 Modo desarrollador (recomendado para programadores)

### 1. Clona el proyecto

```bash
git clone https://github.com/soypercyabad/VigiCafe.git
cd VigiCafe
```

### 2. Crea entorno virtual

```bash
python -m venv .env
source .env/Scripts/activate
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Corre la app

```bash
python -m src.main
```

---

## 🪄 Ejecutable 
Puedes descargar el archivo `VigiCafe.exe` desde la [sección de Releases](https://github.com/soypercyabad/VigiCafe/releases) y ejecutarlo directamente. No necesita instalación de Python.

---

## 🧠 Créditos
Proyecto creado por SoyPercyAbad.
Inspirado en la necesidad de mantener actividad constante en apps de trabajo remoto.

---

## 🐍 Requisitos técnicos
- Python 3.10+
- Windows (compatible con pystray)
- Librerías:
  - `pyautogui`
  - `pystray`
  - `Pillow`
  - `python-dotenv`