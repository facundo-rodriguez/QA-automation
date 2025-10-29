# 🧪 Proyecto de Automatización Web – Saucedemo (Pre-Entrega QA Automation)

## 📄 Descripción del Proyecto

Este proyecto corresponde a la **pre-entrega del curso de QA Automation con Python**.  
Su objetivo es **automatizar flujos básicos de navegación web** en el sitio [SauceDemo](https://www.saucedemo.com) utilizando **Selenium WebDriver** y **Pytest**.

El proyecto demuestra:
- Automatizar un login exitoso.
- Validar la navegación y los elementos del catálogo.
- Interactuar con productos y verificar el carrito de compras.

---

## 🧰 Tecnologías Utilizadas

- 🐍 **Python 3.10+**
- 🌐 **Selenium WebDriver**
- 🧪 **Pytest**
- 💻 **Git y GitHub** (control de versiones)
- 📊 **pytest-html** (para generar reportes en HTML)
- 🧩 **Entorno virtual (venv)** para el manejo de dependencias

---

## 📂 Estructura del Proyecto

```
pre-entrega-final/
│
├── tests/
│   └── test_pre_entrega.py        # Casos de prueba con Pytest
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
└── reporte.html                 # Reporte generado por pytest (una vez ejecutado)
```

---

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/facundo-rodriguez/QA-automation.git
   cd QA-automation
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   ```bash
   # En Windows
   venv\Scripts\activate

   # En Linux/Mac
   source venv/bin/activate
   ```

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Verificar WebDriver:**
   Asegúrate de tener el driver compatible con tu navegador (por ejemplo, ChromeDriver) y que esté en el PATH o en la raíz del proyecto.

---

## 🧭 Casos de Prueba Automatizados

### 1️⃣ Login
- Navegar a [https://www.saucedemo.com](https://www.saucedemo.com)
- Ingresar credenciales válidas:
  - Usuario: `standard_user`
  - Contraseña: `secret_sauce`
- Validar redirección a `/inventory.html`
- Confirmar que aparezca el texto “Products” o “Swag Labs”

### 2️⃣ Navegación del Catálogo
- Validar título correcto de la página.
- Comprobar que exista al menos un producto visible.
- Verificar la presencia de elementos como menú, filtros, etc.

### 3️⃣ Interacción con Productos (Carrito)
- Agregar el primer producto al carrito.
- Verificar que el contador del carrito se incremente.
- Acceder al carrito y confirmar que el producto agregado esté presente.

---

## ▶️ Ejecución de las Pruebas

Ejecutar todas las pruebas con Pytest:
```bash
pytest -v
```

Generar un reporte en HTML:
```bash
pytest tests/test_pre_entrega.py -v --html=reporte.html
```

El archivo `reporte.html` contendrá el detalle de los resultados.

---

## 👨‍💻 Autor

**Facundo Rodríguez**  
💼 Curso: QA Automation con Python  


---

## 📜 Licencia

Proyecto educativo desarrollado con fines de práctica y aprendizaje.
