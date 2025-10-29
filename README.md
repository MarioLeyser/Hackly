# Hackly 🚀

Un proyecto de hackathon desarrollado para crear una plataforma de gestión y colaboración en eventos de hackathons. Esta aplicación proporciona herramientas esenciales para organizadores y participantes de hackathons.

## ✨ Características Principales

- **🎯 Gestión de Proyectos** - Crea y administra proyectos de hackathon
- **👥 Equipos Colaborativos** - Forma equipos y colabora en tiempo real
- **📊 Dashboard Interactivo** - Visualiza el progreso de los proyectos
- **⚡ Tiempo Real** - Actualizaciones en tiempo real durante el evento
- **📱 Interface Responsive** - Funciona en desktop y móvil

## 🛠️ Stack Tecnológico

### Frontend
- **React** - Biblioteca principal de UI
- **TypeScript** - Tipado estático
- **Tailwind CSS** - Framework de estilos
- **Vite** - Tooling de desarrollo
- **Framer Motion** - Animaciones

### Backend
- **Node.js** - Runtime de JavaScript
- **Express** - Framework web
- **Socket.io** - Comunicación en tiempo real
- **MongoDB** - Base de datos NoSQL
- **JWT** - Autenticación

### Herramientas de Desarrollo
- **Git** - Control de versiones
- **npm** - Gestión de paquetes
- **ESLint** - Linting de código
- **Prettier** - Formateo de código

## 📦 Instalación y Configuración

### Prerrequisitos
- Node.js (versión 16 o superior)
- MongoDB
- npm o yarn

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/MarioLeyser/Hackly.git
cd Hackly
```

2. **Instalar dependencias del backend**
```bash
cd backend
npm install
```

3. **Instalar dependencias del frontend**
```bash
cd ../frontend
npm install
```

4. **Configurar variables de entorno**

Crea un archivo `.env` en la carpeta backend:
```env
PORT=5000
NODE_ENV=development
```

Crea un archivo `.env` en la carpeta frontend:
```env
VITE_API_URL=http://localhost:5000
VITE_APP_TITLE=Hackly
```

5. **Inicializar la base de datos**
```bash
# Asegúrate de que MongoDB esté ejecutándose
mongod
```

6. **Ejecutar la aplicación**

**Terminal 1 - Backend:**
```bash
cd backend
npm run dev
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

7. **Abrir la aplicación**
Navega a `http://localhost:5173` en tu navegador.

## 🎯 Uso de la Plataforma

### Para Organizadores
- Crear y configurar eventos de hackathon
- Gestionar participantes y equipos
- Monitorear el progreso en tiempo real
- Evaluar proyectos participantes

### Para Participantes
- Unirse a hackathons
- Formar equipos colaborativos
- Gestionar proyectos durante el evento
- Colaborar en tiempo real con el equipo

### Ejemplo de API
```javascript
// Crear un nuevo proyecto
fetch('/api/projects', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  },
  body: JSON.stringify({
    name: 'Mi Proyecto Innovador',
    description: 'Descripción del proyecto',
    technologies: ['React', 'Node.js']
  })
});
```

## 🏗️ Estructura del Proyecto

```
Hackly/
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── middleware/
│   │   └── utils/
│   ├── package.json
│   └── server.js
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── styles/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir al proyecto:

1. **Haz un Fork del proyecto**
2. **Crea una rama para tu feature**
```bash
git checkout -b feature/AmazingFeature
```
3. **Commit tus cambios**
```bash
git commit -m 'Add some AmazingFeature'
```
4. **Push a la rama**
```bash
git push origin feature/AmazingFeature
```
5. **Abre un Pull Request**

### Guía de Contribución
- Sigue las convenciones de código existentes
- Añade tests para nuevas funcionalidades
- Actualiza la documentación cuando sea necesario
- Asegúrate de que todos los tests pasen

## 🧪 Scripts Disponibles

### Backend
```bash
npm run dev      # Modo desarrollo con hot reload
npm start        # Producción
npm test         # Ejecutar tests
npm run lint     # Linting del código
```

### Frontend
```bash
npm run dev      # Servidor de desarrollo
npm run build    # Build para producción
npm run preview  # Preview del build
npm run lint     # Linting del código
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autor

- **Mario Leyser** - [GitHub](https://github.com/MarioLeyser) 
- **Laura Rodriguez** - [GitHub](https://github.com/) 
- **Martin Huamani** - [GitHub](https://github.com/) 
- **William Chambi** 
