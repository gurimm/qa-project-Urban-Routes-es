# Proyecto Urban Routes
#### Guri Muñoz Mejía. Cohort 18, Sprint 9
### Descripción del proyecto.
En este proyecto se verificará el proceso completo para pedir un taxi en la aplicación _Urban Routes_.

Para ello se han escrito pruebas automatizadas de acuerdo a las acciones descritas en el ejercicio 1, del Proyecto final del sprint 8.

### Fuente de documentación utilizada
Para la realizción del proyecto se han tomado las siguientes referencias como fuente de documentación:

* [Proyecto para el octavo sprint: Ejercicio 1](https://tripleten.com/trainer/qa-engineer/lesson/0f23a649-8168-41d4-be6a-19fab7206f66/)
* [Web Element Locator Strategies_Course](https://testautomationu.applitools.com/web-element-locator-strategies/)
* [Patrones de Diseño](https://refactoring.guru/es/design-patterns)
* [El tutorial de Python](https://docs.python.org/es/3/tutorial/index.html)

### Descripción de las tecnologías y técnicas utilizadas.

Para las pruebas automatizadas de la aplicación, se realizó la configuración del repositorio Git y clonación del mismo.


Se definieron e instanciaron los localizadores y métodos necesarios en la clase _UrbanRoutesPage_ y las pruebas en la clase _TestUrbanRoutes_, dentro del archivo main.py.

Se generó el script de prueba bajo el Modelo de Objetos de Página (POM), estableciendo los hooks de precondición y postcondición del escenario completo para pedir un taxi de acuerdo con los siguientes pasos:

1. Configurar la dirección
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor en el modal.


 Las tecnologías utilizadas en el proyecto incluyen:

* Python 3.12
* Pytest 8.3.4
* Selenium 4.27.1

### Instrucciones para ejecutar la prueba.

1.  Reemplazar la variable _urban_routes_url_ dentro del archivo data.py, con la URL actualizada del servidor.
2. Ejecutar (_Run_) el archivo main.py
3. Comprobar el resultado de la ejecución en main.py::TestUrbanRoutes::test_set_route 
   * PASSED [100%]
   * Process finished with exit code 0