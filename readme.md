#Breve descripción del sistema Bienvenido/as. Este sistema pretende servir de inventario para el registro y consulta de equipos médicos instalados en un Hospital. 
Aquí se pueden registrar equipos, referentes de cada sector donde se hayan instalados los mismos y proveedores con su información de contacto para recibir soporte.
También, se pueden cargar Artículos para informar a la organización el estado de cada instalación de los equipos.

#Instalar el proyecto Para instalar el proyecto se deben seguir los siguientes pasos:

descargar el repositorio al equipo local y abrirlo con la aplicación vscode.
Una vez abierto, correr en la terminal de VSCODE el comando python manage.py runserver.
A continuación, se mostrará la url generada localmente para acceder al proyecto.
La url de inicio es: http://127.0.0.1:8000/index/
#Navegar dentro del proyecto En el proyecto hay un botón Inicio (en el futuro, en una versión final, será el botón para iniciar sesión y poder cargar y consultar datos
después de autenticar). Para volver siempre a la página inicial, presione ese botón. Luego verá 3 pestañas, cada una hace referencia a una parte del inventario.

#Cómo utilizar el sistema

Para registrarse presione el botón homónimo. En la ventana siguiente rellene los campos mostrados y presione Registrarse

Para iniciar sesión, presione el botón Iniciar sesión e ingrese sus datos.

Una vez dentro del sistema:
Si desea ver la lista de Artículos presione en la pestaña Artículos. Si desea cargar un nuevo Artícuo, previamente deberá iniciar sesión. A continuación, presione el botón CREAR ARTICULO, rellene los campos y presione
CREAR REFERENTE. A continuación, será redirigido a la pestaña anterior, donde verá todos los referentes cargados.
Los mismos pasos deben realizarse para Proveedores y Equipos.
También dispone de un botón en cada ventana que le permite Buscar los elementos cargados previamente.
