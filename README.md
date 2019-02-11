# **Calendario MatCom** - **Proyecto de Base de Datos II**

## **Facultad de Matemática y Computación** - **Universidad de La Habana**

### **Tutores**

* Hian Cañizares Díaz
* Alejandro Piad Morfis

### **Autores**

* Leynier Gutiérrez González
* Carlos Bermudez Porto
* Roberto Marti Cedeño
* Antonio Otaño Barrero

## **Resumen**

La aplicación Calendario MatCom permitirá crear y editar por los usuarios con los permisos adecuados de forma directa los calendarios de clases, exámenes, eventos, etc. de la Facultad de Matemática y Computación, permitirá consultarlos de forma web así como exportarlos para ser impresos por los usuarios. Permitirá importar los horarios confeccionados por el Vicedecano Docente de la facultad. Contará con filtros predeterminados y consultas avanzadas para una mejor visualización dependiendo del usuario.

## **Descripción Detallada**

### **Crear el Horario**

Brindará un entorno para la creación del horario, tratando de simular la manera actual en que se construye. Además contará con facilidades adicionales en la construcción del mismo, entre estas se podrá contar con una vista maestra del horario que simulará al horario maestro usado actualmente, contará con la facilidad de que al asignarse un turno decidir la frecuencia del mismo facilitando la confección del horario semanal, también la aplicación ofrecerá algunas notificaciones facilitando la detección de problemas como: Aulas asignadas a turnos distintos en un mismo momento, que un mismo grupo este asignado a clases distintas en un mismo momento, etc. Importante destacar que ***en ningún caso se ofrecerá la manera de resolver los conflictos*** anteriores, ni otros que puedan aparecer durante la confección del horario, ***la solución de los mismos siempre estará en manos de las personas asignadas a dicha tarea***.

### **Visualizaciones y Consultas**

Permitirá la consulta al horario de distintas maneras facilitando la obtención de información del mismo, algunas de estas solo a los usuarios interesados. Algunos ejemplos serían: Visualizar los turnos de un grupo, visualizar las aulas utilizadas (o vacías), ver las frecuencias de una asignatura determinada, etc.

### **Exportar e Importar**

Contará con la capacidad de importar los horarios previamente hechos en el formato de Excel permitiendo visualizarlos sin la necesidad de construirlos desde la misma. A su vez también permitirá exportar el horario a documentos para su uso offline, permitiendo además su impresión. La capacidad de exportarlo servirá en caso de no usarse la aplicación, para construir el horario como una manera de facilitar el acceso al mismo. (No se necesitará de enviarlo por correo o copiarlo)

### **Roles y Permisos**

Contará con un sistema de roles y permisos teniéndose desde estudiante, profesores hasta administradores. Con esto se podrá manejar de mejor manera las vistas permitidas para cada usuario, además de funcionalidades agregadas para cada caso.

### **Difundir y Notificar**

Permitirá enviar los horarios por correo electrónico, así como notificar en la aplicación y enviar notificaciones por correo electrónico de los cambios realizados a los horarios. Las notificaciones se enviarán a los usuarios afectados por las modificaciones y se podrán configurar para solo recibir las deseadas.

### **Peticiones y Sugerencias**

Permitirá a los usuarios enviar peticiones para posibles cambios en los horarios, así como también enviar sugerencias planteando donde les vendría mejor las ubicaciones temporales y espaciales nuevas.

### **Tipos de Eventos**

Permitirá manejar diferentes tipos de eventos como turnos de clases (Docencia), eventos extra-clases (Festivales, Exposiciones, etc.), clases de Post-Grado, etc.

### **Distribución de Recursos**

Permitirá la distribución de recursos entre las unidades lógicas o turnos de clase, un ejemplo de ello será el problema de la distribución de los proyectores donde se podrá acceder a consultas sobre en qué turno que proyector se encuentra en que aula o cuando no se encuentra empleado alguno.

### **Log del Sistema**

Tendrá un registro de forma obligatoria sobre todos los cambios, procesos y acciones que se le realicen y los usuarios envueltos en las mismas.

### **Votaciones**

Permitirá a sus usuarios realizar votaciones sobre los horarios en caso de que surja la posibilidad de varias distribuciones del mismo.

### **Interfaz de Administración**

Tendrá una interfaz visual de administración que será la encargada de modificar si es necesario la base de datos sin necesidad de programar.
