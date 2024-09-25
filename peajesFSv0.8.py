# coding=utf-8
# Autor               : Jota Cordova (jotacordovaj.io@gmail.com)
# Fecha de creación   : 16/08/2024
# Última modificación : 24/09/2024
# Versión             : 0.8.0

#******************************************************************************
#*                                                                            *
#*              ENTREGA FINAL MÓDULO 4 BOOTCAMP FULL STACK PYTHON             *
#*                           MVP Peajes FS                                    *
#*                                                                            *
#******************************************************************************

"""
Historial de versiones:
    0.1.0 (27/08/2024): Versión inicial. Se crea una maqueta inicial con la estructura y secciones, se prueba la interfaz y se genera el módulo 
                        para la inserción de registros y valida instancias. 
    0.1.1 (18/08/2024): Se corrigen problemas en el filtrado de datos para mostrar los datos ingresados, se agregan atributos requeridos para su control.
    0.2.0 (19/08/2024): Se agrega opción de cobros. Los registros ingresados quedan en estado "pendientes de cobro", el proceso siguiente es aplicar 
                        la tarifa y cobrar.
    0.2.1 (20/08/2024): Se modifica la estructura de las tablas para mejorar y robustecer validaciones. Se agrega id único, fechas de operación o actualización.
    0.3.0 (26/08/2024): Se agrega un módulo de consultas a la BBDD, permite hacer búsquedas por algunos criterios y listar los resultados.
    0.4.0 (20/08/2024): Se agrega la capacidad de exportar resultados a CSV, sea para ser usados como comprobantes de cada operación, o como respaldos.
    0.5.1 (20/08/2024): Se agrega un módulo para modificar o actualizar registros de vehículos en la base de datos, permite corregir o agregar información.
    0.6.0 (26/08/2024): Se agrega un módulo para modificar o actualizar las tarifas. Permite crear una nueva tarifa o modificar una existente.
    0.7.0 (20/08/2024): Se modifica la estructura de las tablas para mejorar y robustecer validaciones.
    0.8.1 (20/08/2024): Se mejora la funcionalidad de multifiltro drill-down.
    0.8.2 (26/08/2024): Se mejora la capacidad de exportar resultados a formatos PDF y EXCEL.
    0.8.3 (22/09/2024): Se completan las secciones de ayuda o home, que sólo estaban como maquetas de diagramación.

Próximas mejoras planeadas:    

    1) Agregar un dashboard con los ingresos y otros estadígrafos como vehículos por tipo u hora y día
       de mayor tráfico.
    2) Agregar un buscador de reportes históricos, que permita buscar un comprobante de cobro o una consulta guardada en alguno de los formatos de salida.   

Errores conocidos y workarounds:
    1) Modificar un registro existente, no hace el update en la BBDD, prioridad baja, es un adicional.
    2) Modificar una tarifa existente, no hace el update en la BBDD, prioridad baja, es un adicional.

Licencia: Dominio público

GENERALIDADES DEL SISTEMA:    
    - Guía de estilos y nomenclatura:
        1) Para una mejor identificación, se han agregado prefijos a los objetos:
            f_   : Para funciones
            lst_ : Para listas
            v_   : Para variables
            dict_: Para diccionarios
        2) Notación: Además del prefijo, todos los nombres de objetos, inician con la primera palabra 
        en minúscula y la segunda con la primera letra en mayúscula, ejemplo: "unEjemplo", para las variables se usa "snake_case".        
    
    - Consideraciones especiales:
        1) Cada función incluye docstrings, con indicación de:
            a) Su Propósito o qué hace.
            b) Parámetros que recibe.
            c) Qué retorna.
            
    - Explicación de las columnas del Diccionario de Objetos:
        1) Elemento    : Nombre de la variable o función.
        2) Tipo        : Tipo de dato (str, int, float, list, dict, function, etc.).
        3) Descripción : Qué hace o almacena el objeto.
            
    - Librerías utilizadas:
        1) Streamlit 1.38.0: Librería para crear la interfaz de usuario. Es un framework
                             para desarrollo rápido de aplicaciones web en Python
        2) SQLite3: Librería del core que provee una base de datos integrada a Python.
        3) Pandas 2.2.2: Librería para el manejo de datos
        4) Random: Librería del core para la generación de cadenas aleatorias
        5) String: Librería del core que permite el manejo de cadenas
        6) Datetime: Librería del core que permite el manejo de fechas
        7) IO y BytesIO: Librería del core para generar archivos binarios (exportar PDF)
        8) ExcelWriter: Librería de Pandas para exportar a EXCEL # Esta librería no se carga en la versión WEB
        9) FPDF 1.7.2: Librería para generar PDFs
    
DESCRIPCIÓN POR MÓDULO:

Módulo 1:  pagina_principal(): Home o menú del sistema y definición de las clases.

Descripción
    - Funcionalidades principales:
      1) Definición de clases: Se define una jerarquía de clases para represen-
         tar diferentes tipos de vehículos (automóviles, bicicletas, motocicletas).
      2) Crear la página principal: Renderiza la página principal de la aplicación,
         presenta información sobre el sistema.
      3) Visualiza información: Muestra texto, imágenes y listas para describir las 
         características generales del sistema y lógica de navegación.

    - Dependencias externas:
      1) Streamlit: Biblioteca de Python utilizada para crear aplicaciones web inte-
         ractivas.
      2) Imágenes: Utiliza imágenes externas para ilustrar contenidos. Las imagenes
         se almacenan en la carpeta /assets/img. 
    
        
    - Diccionario de objetos:
        Objeto  	                Tipo        	Descripción
        *************************************************************************************************
        Clases
        ******		
        Vehiculo	                Clase       	Clase base para todos los vehículos.
        Automovil	                Clase	        Hereda de Vehiculo, representa un automóvil.
        Particular	                Clase	        Hereda de Automovil, representa un automóvil particular.
        Carga	                    Clase       	Hereda de Automovil, representa un vehículo de carga.
        Bicicleta               	Clase       	Hereda de Vehiculo, representa una bicicleta.
        Motocicleta             	Clase	        Hereda de Bicicleta, representa una motocicleta.

        Variables
        *********		
        v_nom_sistema	            str	            Nombre del sistema.

        Funciones
        *********		
        f_titulo_lateral	        function    	Establece el título en la barra lateral.

Módulo 2: pagina_ingreso(): Interfaz que permite crear e insertar nuevos vehículos en la base de datos.

Descripción
    - Funcionalidades principales:
        1) Ingreso de vehículos: Permite al usuario ingresar los datos de nuevos
           vehículos en un formulario a través de una interfaz web creada con Streamlit.
        2) Validación de datos: Verifica que los datos ingresados sean válidos y
           tengan el formato correcto.
        3) Persistencia de datos: Almacena los datos de los vehículos en una base
           de datos SQLite.
        4) Presentación de datos: Muestra una tabla con un resumen de los vehículos
           ingresados utilizando un DataFrame (df) de Pandas.

    - Flujo del módulo:
        1) Ingreso de datos: El usuario ingresa los datos de los vehículos a través de los elementos de la interfaz de Streamlit.
        2) Validación: Se valida que los datos ingresados sean del tipo correcto y que cumplan con las restricciones definidas.
        3) Creación de tupla: Se crea una tupla con los datos del vehículo para ser insertada en la base de datos.
        4) Inserción en la base de datos: Se llama a la función insertar_vehiculo para insertar los datos en la tabla vehiculos.
        5) Presentación de resultados: Se muestra un DataFrame (tabla) con los vehículos ingresados.
        6) Los nuevos vehículos quedan en estado de "cobro pendiente" (estado=0), hasta que sean procesados en el módulo de recaudación o cobro

    - Dependencias externas:
        1) Streamlit: Para crear la interfaz de usuario.
        2) SQLite3: Para interactuar con la base de datos.
        3) Pandas: Para manipular y mostrar los datos en un DataFrame.

    - Diccionario de objetos:
        Objeto	                    Tipo/Parámetros     Descripción
        ***********************************************************************
        Funciones
        *********
        pagina_ingreso()		    None                Función principal que define la página de ingreso de vehículos.
        insertar_vehiculo(vehiculo)	tupla               Inserta un nuevo vehículo en la base de datos.
        mostrar_vehiculos()		    None                Muestra los vehículos ingresados.

        Variables
        *********
        lst_alta_vehiculos          list                Lista para almacenar temporalmente los vehículos antes de insertarlos en la base de datos.
        v_num_vehiculos             int                 Variable para almacenar el número de vehículos a ingresar.
        v_fecha_operacion           date                Variable para almacenar la fecha de la operación. Se convierte a fecha para calculo, se guarda como texto.

    - Cosas por hacer (T2D):
        - Validación más robusta: Como el sistema nace de un modelo extraño y sin pretender convertirse en sistema, se fue arreglando en la medida
                                  que se agregaron funcionalidades. Se podrían agregar más validaciones, por ejemplo, para evitar que se dupliquen datos
                                  en el proceso de alta de vehículos, que las marcas y modelos sean consultados a la base, para evitar distintas formas
                                  de escribir un nombre y tener que corregir después o que la cilindrada sea coherente con el tipo de vehículo.
        - Manejo de errores: Se puede mejorar el manejo de errores (mucho), por ejemplo, mostrando mensajes más específicos al usuario en caso de 
                             que ocurra algún problema y proveer una solución administrada, por ahora, y por tratarse sólo de un producto mínimo viable.
        - Optimización de consultas: El MVP procesa pocos vehículos y de forma manual, si se espera procesar una gran cantidad de datos, se deben 
                                     cambiar los métodos de ingreso, de inserción y de consultas a la base de datos.
        - Interfaz de usuario más amigable: Faltan elementos visuales que mejoren la experiencia del usuario, como por ejemplo, un calendario para 
                                            seleccionar fechas.
        - Seguridad: Si en realidad se tratase de una aplicación con acceso público, deberían implementarse medidas de seguridad para proteger los datos, 
                     usuarios por roles, tablas de auditoría, etc.

Módulo 3: pagina_consulta(): Interfaz que permite crear e insertar nuevos vehículos en la base de datos.

Descripción
    - Funcionalidades principales:
        1) Interfaz de consulta: Permite al usuario realizar consultas personalizadas sobre los vehículos registrados en la base de datos.
        2) Consultas frecuentes: Ofrece múltiples opciones de consulta, incluyendo por tipo de vehículo, rango de fechas, vehículos procesados e ingresos recaudados.
        3) Visualización de resultados: Muestra los resultados de la consulta en un DataFrame de Pandas (una tabla).
        4) Exportación de resultados: Permite exportar los resultados en formato CSV, Excel o PDF.

    - Flujo del módulo:
        1) Interfaz de usuario: Se presenta un menú para seleccionar el tipo de consulta.
        2) Selección de criterios: Según el tipo de consulta, se muestran diferentes campos para ingresar los criterios de búsqueda.
        3) Ejecución de la consulta: Al hacer clic en el botón "Ejecutar consulta", se construye la consulta SQL correspondiente y se ejecuta .
        4) Visualización de resultados: Los resultados de la consulta se muestran en un DataFrame de Pandas.
        5) Exportación de resultados: El usuario puede exportar los resultados en diferentes formatos (PDF, CSV, EXCEL).
        
    - Dependencias externas:
        1) Streamlit: Para crear la interfaz de usuario.
        2) SQLite3: Para interactuar con la base de datos.
        3) Pandas: Para manipular y mostrar los datos en DataFrames y tablas.
        4) FPDF: Librería personalizada para generar archivos PDF.

    - Diccionario de objetos:
        Objeto	                Tipo/Parámetro      Descripción
        ***********************************************************************
        Variables
        *********
        lst_tipos_vehiculo	    list	            Lista de tipos de vehículos disponibles.
        lst_marcas_vehiculo	    list	            Lista de marcas de vehículos disponibles.
        lst_modelos_vehiculo	list	            Lista de modelos de vehículos disponibles.
        lst_opciones_consulta	list	            Lista de opciones de consulta disponibles.
        v_tipo_consulta	        str 	            Opción de consulta seleccionada por el usuario.
        v_fecha_inicio          date	            Fecha de inicio para el rango de fechas.
        v_fecha_fin	            date	            Fecha de fin para el rango de fechas.
        v_tipo_vehiculo	        list	            Lista de tipos de vehículos seleccionados para filtrar. #Ojo...podría haber un problema, probar
        marca	                list	            Lista de marcas seleccionadas para filtrar.
        modelo              	list	            Lista de modelos seleccionados para filtrar.
        df	                    df	                DataFrame de Pandas que contiene los resultados de la consulta.
        lst_alta_vehiculos	    list	            Lista para almacenar temporalmente los vehículos antes de insertarlos en la base de datos. (No utilizada en este módulo)
        v_num_vehiculos	        int	                Número de vehículos a ingresar. (No utilizada en este módulo)
        v_fecha_operacion	    str	                Fecha de la operación. (No utilizada en este módulo)

    - Cosas por hacer (T2D):
        1) Optimización de consultas: En un caso real, para consultas complejas o sobre grandes 
                                      conjuntos de datos, se deben optimizar las consultas utilizando 
                                      índices y otras técnicas de bbdd.
        2) Validación de fechas: Se puede agregar una validación para asegurarse de que la fecha de 
                                 inicio sea anterior a la fecha de fin, u otras similares.
        3) Personalización de exportaciones: Se podría personalizar el formato de exportación, por 
                                             ejemplo, seleccionando las columnas a exportar.
        4) Seguridad: Implementar medidas de seguridad para proteger los datos, ejemplo: Validar 
                      parámetros de entrada para evitar inyecciones SQL.

Módulo 4 pagina_modificarV(): Interfaz que permite modificar o actualizar la información del registro 
de un vehículo ya creado en la base de datos. 

Descripción
    - Funcionalidades principales:
        1) Búsqueda de vehículos: Permite al usuario buscar un vehículo específico 
                                  utilizando un sistema de filtrado por tipo, marca 
                                  y modelo.
        2) Visualización de datos: Muestra los detalles del vehículo seleccionado en 
                                   un formato legible.
        3) Edición de datos: Permite al usuario modificar los datos del vehículo y 
                             visualizar los cambios propuestos.
        4) Confirmación de cambios: Antes de guardar los cambios, se muestra un resumen 
                                    de las modificaciones para que el usuario las confirme.
        5) Actualización de la base de datos: Si el usuario confirma los cambios, se actualiza 
                                              el registro correspondiente en la base de datos.
    
    - Dependencias externas:
        1) Streamlit: Para crear la interfaz de usuario.
        2) SQLite3: Para interactuar con la base de datos.
        3) Pandas: Para manipular y mostrar los datos en un DataFrame.

    - Diccionario de objetos:
        Objeto	                Tipo/Parámetro      Descripción
        ***********************************************************************
        Variables
        *********
        dic_veh_modificado      Diccionario         Almacena los datos del vehículo a modificar y los cambios realizados.
        vehiculo_id             int                 Identificador único del registro del vehículo.
        conexion                string              Conexión a la base de datos.
        df_vehiculos            DataFrame           Contiene todos los vehículos de la base de datos.
        tipos_vehiculo          list                Contiene valores para filtrar los vehículos.    
        marcas_filtradas        list                Contiene valores para filtrar los vehículos.
        modelos_filtrados       list                Contiene valores para filtrar los vehículos.
        v_fecha_inicio          date                Fecha de inicio para el rango de fechas en la búsqueda.
        v_fecha_fin             date                Fecha de fin para el rango de fechas en la búsqueda.
        cod_op_filtrado         string              Código de operación seleccionado para filtrar los resultados.
        registro_final          DataFrame           Contiene el registro seleccionado para modificar.

    - Flujo del módulo:
        1) Búsqueda del vehículo: El usuario selecciona criterios de búsqueda (tipo, marca, modelo, rango de fechas) 
                                  y se obtiene el registro correspondiente.
        2) Visualización y edición: Se muestra la información del vehículo seleccionado en un formulario editable.
        3) Confirmación de cambios: Se muestran los cambios propuestos y el usuario confirma si desea guardarlos.
        4) Actualización de la base de datos: Si se confirman los cambios, se ejecuta una consulta SQL para 
                                              actualizar el registro en la base de datos.
    
    - Cosas por hacer (T2D):
        1) Validación de datos: Se pueden seguir agregando validaciones más exhaustivas de los datos ingresados 
                                por el usuario para evitar errores.
        2) Optimización de consultas: El MVP funciona bien para mostrar funcionalidad, pero a mayor volumen de
                                      datos o, en ambiente de producción, se requieren cambios en arquitectura para consultas 
                                      complejas y mejorar rendimiento.
        3) Seguridad: Se ha mencionado, y es una aspecto natural si alguien decide aprovechar este código
                      para uso público, se debn proteger los datos.
        4) Historial de cambios: Si bien registra la fecha de la última modificación, resulta obvio mejorar esta
                                 funcionalidad para poder hacer auditoría en un sistema que registra movimientos
                                 monetarios, por lo tanto, otro cambio necesario es mejorar el historial de los 
                                 cambios realizados en cada registro.
    
    - Errores conocidos:
        1) Hasta el momento de esta versión, no se ha podido realizar el update del registro modificado, realiza 
           todo el flujo, pero no se ha detectado por qué no se actualiza la bbdd.
           
Módulo 5 pagina_modificarT(): Interfaz que permite modificar o actualizar la información del registro de una tarifa 
ya creada en la base de datos. 

Descripción
    - Funcionalidades principales:
        1) Crear nuevas tarifas: Permite al usuario ingresar los datos de una nueva tarifa (tipo, tarifa base, 
                                 sobrecargo por peso, etc.) y la almacena en la base de datos con un nuevo código.
        2) Modificar una tarifa existente: Permite al usuario seleccionar una tarifa existente y modificar sus datos.
        3) Consulta de tarifas: Muestra una tabla con todas las tarifas existentes para facilitar la selección o revisión.
        4) Validación de datos: Verifica que los datos ingresados sean válidos antes de guardarlos en la base de datos.
        5) Control de versiones: Al crear un nuevo registro, para un tipo de tarifa, cambia el estado de la tarifa anterior
                                 a inactivo, y deja el nuevo registro en estado activo.
    
    - Dependencias externas:
        1) Streamlit: Para crear la interfaz de usuario.
        2) SQLite3: Para interactuar con la base de datos.
        3) Pandas: Para manipular y mostrar los datos en un DataFrame.

    - Diccionario de objetos:
        Objeto	                    Tipo/Parámetro      Descripción
        ***********************************************************************
        Variables
        *********
        v_guarda_opcion             int                 Almacena la opción seleccionada por el usuario (crear o modificar).
        tarifas                     list                Lista de tuplas que contiene todos los registros de la tabla tarifario.
        df_tarifas                  DataFrame           Contiene los datos de las tarifas en un formato tabular.
        v_codigo_tarifa_a_modificar str                 Código de la tarifa a modificar.
        v_tarifa_seleccionada       tuple               Tupla que contiene los datos de la tarifa seleccionada.
        
    - Flujo del módulo:
        1) Selección de opción: El usuario elige entre crear una nueva tarifa o modificar una existente.
        2) Ingreso de datos: El usuario ingresa los datos de la nueva tarifa o selecciona la tarifa existente a modificar.
        3) Validación de datos: Se verifica que los datos ingresados sean válidos (por ejemplo, que la tarifa base 
                                sea positiva).
        4) Actualización de la base de datos: Se ejecuta una consulta SQL para insertar o actualizar el registro de la tarifa.
        5) Visualización de resultados: Se muestra un mensaje de confirmación al usuario indicando si la operación se realizó 
                                        correctamente.

    - Cosas por hacer (T2D):
        1) Validación más exhaustiva: Se pueden seguir agregando validaciones más completas de los datos (este es un MVP), 
                                      por ejemplo, para verificar que el tipo de tarifa sea válido, o que rol del usuario,
                                      le permite modificar una tarifa.
        2) Permisos de usuario: Se podrían implementar diferentes niveles de permisos para restringir el acceso a ciertas 
                                funciones.
        3) Historial de cambios detallado: Se podría almacenar un historial más detallado de los cambios realizados en las
                                           tarifas.

Módulo 6 pagina_cobro(): Interfaz que se encarga de gestionar el proceso de cobro del sistema de peaje. Permite calcular 
                         el cobro para cada vehículo, en función de su tipo, generar un código de operación único para 
                         cada transacción, y registrarlo en la base de datos. 

Descripción
    - Funcionalidades principales:
        1) Consulta de vehículos pendientes: Obtiene una lista con los vehículos pendientes de cobro.
        2) Cálculo del cobro: Calcula el cobro basado en el tipo de vehículo y las tarifas configuradas
                              en la base de datos.
        3) Registro del cobro: Inserta un nuevo registro en la tabla de cobros con los detalles de la transacción.
        4) Actualización del estado del vehículo: Actualiza el estado del vehículo en la tabla de vehículos para 
                                                  indicar que ya ha sido cobrado.
        5) Generación de código de operación: Genera un código alfanumérico de 8 caracteres, único para cada transacción.
        6) Exportación de resultados: Permite exportar los resultados del proceso de cobro en diferentes 
                                      formatos (CSV, Excel, PDF).
    - Dependencias externas:
        1) Streamlit: Para crear la interfaz de usuario.
        2) SQLite3: Para persistencia de los datos.
        3) Pandas: Para manipular y mostrar los datos en un DataFrame.
        4) random: Para generar números aleatorios y crear códigos únicos.
        5) string: Para manipular cadenas de texto.

    - Diccionario de objetos:
        Objeto	                    Tipo/Parámetro      Descripción
        ***********************************************************************
        Variables
        *********
        v_cod_alfanum               str                 Conjunto de todos los caracteres alfanuméricos usados para crear códigos.
        pepinillo                   str                 Conexión a la base de datos.
        cursor                      cursor              Cursor de la base de datos para ejecutar consultas.
        df_pendientes               DataFrame           Contiene los vehículos pendientes de cobro.
        cobro                       float               Contiene valor del cobro calculado para un vehículo.
        fecha_operacion             date                Fecha y hora de la operación de cobro.
        cod_op                      str                 Código de operación generado para la transacción.
        registros_procesados        list                Lista de diccionarios que contienen los detalles de los cobros procesados.
        df_cobros_procesados        DataFrame           Muestra los cobros procesados.

    - Flujo del módulo:
        1) Consulta de vehículos pendientes: Se obtienen los vehículos pendientes de cobro de la base de datos.
        2) Procesamiento de cobros: Si hay vehículos pendientes, se itera sobre ellos y se realiza el siguiente 
           proceso para cada vehículo:
           a) Se calcula el cobro en función del tipo de vehículo.
           b) Se genera un código de operación único.
           c) Se inserta un nuevo registro en la tabla de cobros.
           d) Se actualiza el estado del vehículo en la tabla de vehículos.
        3) Visualización de resultados: Se muestra un DataFrame con los cobros 
                                        procesados y se ofrece la opción de exportar 
                                        los resultados en diferentes formatos.

    - Cosas por hacer (T2D):
        1) Optimización de consultas: Mismas de los módulos anteriores.
        2) Validación de datos: Mismas de los módulos anteriores.
        3) Personalización de tarifas: Agregar nuevos ponderadores al polinomio de cálculo.
        
Módulo 7 pagina_valida(): Este módulo se diseñó, específicamente, para demostrar de forma interactiva 
                          los conceptos de herencia y relaciones entre clases en Python. Permitie a un
                          usuario seleccionar entre clases y sus instancias, y se puede visualizar cómo 
                          funciona la herencia y la relación entre las clases. La interfaz permite mostrar, 
                          experimentar y comprobar, didácticamente, las características de la herencia y 
                          relación entre clases. 

Descripción
    - Funcionalidades principales:
        1) Creación de instancias: Crea instancias de diferentes las distancias clases definidas en el sistema
                                   (Vehículo, Automóvil, Particular, Carga, Bicicleta, Motocicleta) para realizar pruebas.
        2) Selección de clases: Permite al usuario seleccionar una clase y una instancia de clase de listas desplegables.
        3) Comparación de instancias: Compara si una instancia es de un tipo de clase específico utilizando la función isinstance.
        4) Visualización de resultados: Muestra un mensaje indicando si un objeto es instancia de una clase ('True' o 'False').

    - Dependencias externas:
        1) Streamlit: Se usa para crear la interfaz de usuario y mostrar los resultados.

    - Diccionario de objetos:
        Objeto	                Tipo/Parámetro      Descripción
        ***********************************************************************
        Variables
        *********
        clases_disponibles      list                Lista con los nombres de las clases disponibles para seleccionar.
        instancias              dict                Diccionario que almacena las instancias creadas de cada clase.
        clase_a                 class               Variable para almacenar una clases seleccionada por el usuario.
        clase_b                 class               Variable para almacenar una clases seleccionada por el usuario.
        instancia_a             instance            Variable para almacenar la instancia seleccionada.
        clase_b_obj             class               Variable para almacenar la clase a la que se compara.
        resultado               boolean             Variable booleana que indica si la instancia es de la clase especificada.

    - Flujo del módulo:
        1) Creación de instancias: Se crean instancias de diferentes clases para tener ejemplos concretos.
        2) Interfaz de usuario: Se crea una interfaz con dos listas desplegables para que el usuario seleccione las clases a comparar.
        3) Comparación: Al hacer clic en el botón "Comparar", se obtiene la instancia y la clase seleccionadas y se utiliza isinstance para verificar la relación.
        4) Visualización: Se muestra el resultado de la comparación en un mensaje claro.

    - Cosas por hacer (T2D):
        1) Enriquecer el contexto: Agregar explicaciones más detalladas, se podría agregar una sección de explicación teórica sobre la herencia 
                                  y la función isinstance para ayudar a los usuarios a comprender mejor el concepto.
        2) Visualización más avanzada: Se podría utilizar una biblioteca de visualización para mostrar los diagramas de clases y las relaciones de herencia.         

Módulo 8 pagina_ayuda(): Este módulo tiene como objetivo principal servir como un manual de usuario básico para la aplicación. 
                         Proporciona una introducción a las funcionalidades principales del sistema, además de una guía rápida 
                         para el usuario a través de los primeros pasos. 

Descripción
    - Funcionalidades principales:
        1) Proporcionar información al usuario: Ofrece una guía básica sobre el funcionamiento del sistema de peaje FS.
        2) Guía de inicio rápido: Presenta una secuencia simple de pasos para comenzar a utilizar el sistema.
        3) Solución de problemas conocidos: Ofrece una sección básica de solución de problemas con errores comunes o conocidos (Workaround).

"""
# IMPORTACION DE LIBRERIAS
# ************************

import sqlite3                  # BBDD
import pandas as pd             # librería para el manejo de datos
import streamlit as st          # librería que permite construir la interfaz 
import random                   # generación de cadenas aleatorias
import string                   # manejo de cadenas
import datetime                 # manejo de fechas
import logging                  # generar log para rastreo de errores
from io import BytesIO          # para generar el archivo binario y exportar PDF
from pandas import ExcelWriter  # para exportar EXCEL
from fpdf import FPDF           # para generar PDF
from datetime import datetime   # retornar una fecha, manipulación y conversión de fechas
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s') # Config del log de errores detallado

# ESTRUCTURA DE CLASES
# ********************

# Super Clase Vehículo
class Vehiculo:
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas):
        self.v_marca         = v_marca
        self.v_modelo        = v_modelo
        self.v_nro_de_ruedas = v_nro_de_ruedas

# Clase Automóvil ==> hereda de Vehículo
class Automovil(Vehiculo):
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada):
        super().__init__(v_marca, v_modelo, v_nro_de_ruedas)
        self._v_velocidad  = v_velocidad
        self._v_cilindrada = v_cilindrada

    def __str__(self):
        return f"E automóvil marca {self.v_marca}, es modelo {self.v_modelo}, alcanza una velocidad de {self.v_velocidad} km/h, y su motor tiene una cilindrada {self.v_cilindrada} cc"    
    
    @property
    def v_velocidad(self):
        """
        Devuelve la velocidad máxima del automóvil en km/h.
        """
        return self._v_velocidad

    @v_velocidad.setter
    def v_velocidad(self, v_valor):
        """
        Establece la velocidad máxima del automóvil.

        Parámetros: v_valor es un número entero positivo que representa la velocidad en km/h.
        
        Retorna: None
        """
        if not isinstance(v_valor, int):
            raise TypeError("La velocidad debe ser un número entero.")
        if v_valor < 0:
            raise ValueError("La velocidad no puede ser negativa.")
        self._v_velocidad = v_valor

    @property
    def v_cilindrada(self):
        """
        Devuelve la cilindrada del motor en cc.
        """
        
        return self._v_cilindrada

    @v_cilindrada.setter
    def v_cilindrada(self, v_valor):
        """
        Establece la cilindrada del motor en cc.

        Parámetros: v_valor, es un número entero positivo que representa la cilindrada en cc.
        """
        if not isinstance(v_valor, int):
            raise TypeError("La cilindrada debe ser un número entero.")
        if v_valor < 0:
            raise ValueError("La cilindrada no puede ser negativa.")
        self._cilindrada = v_valor
    
    
# Subclase Particular ==> hereda de Automóvil
class Particular(Automovil):
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada, v_puestos):
        super().__init__(v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada)
        self._v_puestos = v_puestos 

    @property
    def v_puestos(self):
        """
        Devuelve el número de puestos del vehículo particular.
        """
        return self._v_puestos

    @v_puestos.setter
    def v_puestos(self, v_valor): # bastante poco probable, sólo con fines pedagógicos
        """
        Establece el número de puestos del vehículo particular.

        Parámetros: v_valor (int), es un nuevo número de puestos. Debe ser un número entero positivo.
        """
        if not isinstance(v_valor, int):
            raise TypeError("El número de puestos debe ser un entero.")
        if v_valor <= 0:
            raise ValueError("El número de puestos debe ser mayor que cero.")
        self._v_puestos = v_valor

    def __str__(self):
        """
        Devuelve una representación en cadena de caracteres del vehículo particular.
        """
        return f"El vehículo particular {super().__str__()}, dispone de {self.v_puestos} puestos"        

# Subclase Carga ==> hereda de Automóvil
class Carga(Automovil):
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada, v_carga_kgs):
        super().__init__(v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada)
        self.v_carga_kgs = v_carga_kgs

# Clase Bicicleta ==> hereda de Vehículo
class Bicicleta(Vehiculo):
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas, tipo_de_bicicleta):
        super().__init__(v_marca, v_modelo, v_nro_de_ruedas)
        self._tipo_de_bicicleta = tipo_de_bicicleta

    @property
    def tipo_de_bicicleta(self):
        """
        Devuelve el tipo de bicicleta.
        """
        return self._tipo_de_bicicleta

    @tipo_de_bicicleta.setter
    def tipo_de_bicicleta(self, v_nuevo_tipo):
        """
        Establece el tipo de bicicleta.

        Parámetros: v_nuevo_tipo (str), que almacena el nuevo tipo de bicicleta.
        """
        if not isinstance(v_nuevo_tipo, str):
            raise TypeError("El tipo de bicicleta debe ser una cadena de texto.")
        self._tipo_de_bicicleta = v_nuevo_tipo
    
    def __str__(self):
        """
        Devuelve una representación en cadena de caracteres de la bicicleta.
        """
        return f"La bicicleta {super().__str__()}, es de tipo {self.tipo_de_bicicleta}"

# Subclase Motocicleta ==> hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, v_marca, v_modelo, v_nro_de_ruedas, tipo_de_bicicleta, v_motor, v_cuadro, v_nro_radios):
        super().__init__(v_marca, v_modelo, v_nro_de_ruedas, tipo_de_bicicleta)
        self._v_motor      = v_motor
        self._v_cuadro     = v_cuadro
        self._v_nro_radios = v_nro_radios

    @property
    def v_motor(self):
        return self._v_motor

    @v_motor.setter
    def v_motor(self, v_nuevo_motor):
        if not isinstance(v_nuevo_motor, str):
            raise TypeError("El motor debe ser una cadena de texto.")
        self._v_motor = v_nuevo_motor

    @property
    def v_cuadro(self):
        return self._v_cuadro

    @v_cuadro.setter
    def v_cuadro(self, v_nuevo_cuadro):
        if not isinstance(v_nuevo_cuadro, str):
            raise TypeError("El cuadro debe ser una cadena de texto.")
        self._v_cuadro = v_nuevo_cuadro

    @property
    def v_nro_radios(self):
        return self._v_nro_radios

    @v_nro_radios.setter
    def v_nro_radios(self, v_nuevo_nro_radios):
        if not isinstance(v_nuevo_nro_radios, int):
            raise TypeError("El número de radios debe ser un entero.")
        if v_nuevo_nro_radios <= 0:
            raise ValueError("El número de radios debe ser mayor que cero.")
        self._v_nro_radios = v_nuevo_nro_radios

    def __str__(self):
        return f"La motocicleta {super().__str__()}, tiene un motor de {self.v_motor}, un cuadro {self.v_cuadro}, y sus ruedas cuentan con {self.v_nro_radios} radios de acero"


# ESTRUCTURA DE LAS PÁGINAS DE LA APLICACIÓN
# ******************************************

# Título principal de la aplicación
v_nom_sistema = 'MVP PEAJES FS V 0.8'
st.title(v_nom_sistema)

# Función mostrar el título en la barra lateral
def f_titulo_lateral(v_nom_sistema):
    """
    Establece el título lateral

    Parámetros: Recibe una cadena de texto
    
    Retorna: Muestra el título que es lo hace parametrizable y
    reutilizable para todas las pantallas.
    """
    st.sidebar.title(v_nom_sistema)
    
# Llamada a la función para crear el título
f_titulo_lateral(v_nom_sistema)

# Peajes FS Version Development
def pagina_principal(): # HOME O INICIO, SE PRESENTA INFORMACIÓN DEL README
    """
    En Streamlit cada página se construye como una función.
    
    Se usan las clases del framework para construir objetos como
    
    tablas o inputs
    
    Parámetros: None
    
    Retorna: Renderiza la página según las clases utilizadas
    
    """
    st.title('SECCION: Acerca del Sistema...')

    # Sección 1: Presentación
    v_col1, v_col2 = st.columns([2, 1])
    with v_col1:
        st.write('Este proyecto, **MVP Peajes FS**, es una aplicación basada en Python diseñada para gestionar datos de vehículos y tarifas asociadas. Proporciona una interfaz fácil de usar desarrollada usando el Framework STREAMLIT que sirve para:')

        st.markdown('''
            1. **Mostrar la relación entre instancias y clases:** Compara clases e instancias de clases, y determina si un objeto es instancia o no de otra clase.
            2. **Ingreso de nuevos vehículos:** Añade nuevos vehículos a la base de datos.
            3. **Gestión de datos:** Modificar, eliminar y buscar registros de vehículos usando filtros avanzados.
            4. **Cálculo de tarifas:** Usando como clave el tipo de vehículo, utiliza un polinomio de variables para calcular una tarifa y registrar la recaudación.
            5. **Generación de informes:** Exportar datos en varios formatos (CSV, PDF, Excel). 
                   ''')
    with v_col2:
        st.image('./assets/img/peajes.jpg')

    # Sección 2: Características del sistema
    v_col1, v_col2 = st.columns([1, 2])
    with v_col1:
        st.image('./assets/img/MVPpeajesv0.8.svg')
    with v_col2:
        st.subheader('Diagrama de Clases')
        st.write("Las instancias de las clases, por ejemplo:")
        st.write("      :blue[un_auto = Particular(atributos)]")
        st.write("crean representaciones de los vehículos en memoria pero, para efectos de ajustar el prototipo a algunos elementos de la pauta, las clases sólo reflejarán el encapsulamiento de lógica específica de cada tipo de vehículo, por ejemplo, establecer un valor de atributo o retornar su valor semántico")
        st.markdown('''
            * **Clase Vehiculo:** Clase base para todos los vehículos, defie atributos comunes como marca, modelo y número de ruedas.
            * **Automovil:** Hereda de Vehiculo y agrega atributos específicos para automóviles como velocidad y cilindrada.
            * **Particular:** Hereda de Automovil y agrega el atributo "puestos".
            * **Carga:** Hereda de Automovil y agrega el atributo "carga_kgs".
            * **Bicicleta:** Hereda de Vehiculo y agrega el atributo "tipo_de_bicicleta".
            * **Motocicleta:** Hereda de Bicicleta y agrega atributos específicos para motocicletas como motor, cuadro y número de radios (radios=rayos o varillas metálicas).
        ''')
    data = {
            'Clase Padre': ['Vehiculo', 'Automóvil', 'Bicicleta'],
            'Clase Hija(s)': ['Automóvil, Bicicleta', 'Particular, Carga', 'Motocicleta'],
            'Tipo de Relación': ['Herencia', 'Herencia', 'Herencia'],
            'Cardinalidad': ['1 a muchos', '1 a muchos', '1 a muchos']
            }

    df = pd.DataFrame(data)
    st.subheader("Relaciones entre Clases")
    st.table(df)

    # Sección 3: Otras características del sistema
    st.subheader("Estructura de Datos en SQLite3")
    st.markdown('''
            La base de datos vehiculos está diseñada para gestionar información relacionada con diferentes tipos de vehículos, sus características, las tarifas asociadas y el historial de cobros. Se compone de tres tablas principales:.
            
            * **Recaudacion:** Almacena información sobre los cobros realizados, incluyendo el tipo de vehículo, fecha de la operación, monto cobrado y un código de operación.
            * **Tarifario:** Contiene las tarifas para cada tipo de vehículo, incluyendo una tarifa base, una tarifa por exceso de peso y un tipo de tarifa.
            * **Vehiculos:** Describe los detalles de cada vehículo, como marca, modelo, número de ruedas, tipo de vehículo (particular, carga, bicicleta, motocicleta), y otras características específicas.
        ''')
    
    v_col1, v_col2 = st.columns([1, 1])
    with v_col1:
        st.subheader("Funciones de acceso a datos (Data Access Functions)")
        st.markdown('''
            Se ha separado la lógica de la aplicación de la lógica de persistencia de los datos, se desarrollaron funciones para interactuar directamente con la base de datos SQLite3.
            
            * **pagina_insertar():** Recibe un objeto de una clase como parámetro, y lo inserta en la base de datos.
            * **mostrar_vehiculo():** Consulta la base de datos y devuelve objetos de las clases correspondientes. Se agregó un filtro avanzado y exportacióna distintos formatos.
            * **pagina_modificarV(), pagina_modificarT(), editar_registro(), actualizar_registro():** Reciben un objeto sin modificar, 
            permite editarlo, y luego, actualiza los registros correspondientes en la base de datos.
            * **Eliminar:** Tratándose de un sistema transaccional, no se implementaron métodos para eliminar 
            objetos de la bbdd por razones de auditoría, en su reemplazo se consideró registrar la última actualización.  
            Por lo tanto sólo se puede crear un registro, o modificarlo. Tampoco se puede modificar información de los ingresos.
        ''') 
        
    with v_col2:
        st.image('./assets/img/diagrama_clases2.PNG')
    
    # Creamos dataFrames para cada tabla y armar los diccionarios
    
    recaudacion_df = pd.DataFrame({
    'Campo'      : ['id', 'tipo', 'fecha_operacion', 'cobro', 'cod_op'],
    'Tipo'       : ['int', 'str', 'text', 'float', 'str'],
    'Descripción': ['Identificador único de cada registro de cobro',
                   'Tipo de vehículo',
                   'Fecha y hora en que se realizó el cobro',
                   'Monto cobrado',
                   'Código de operación asociado al cobro']
                })
    
    tarifario_df = pd.DataFrame({
    'Campo'      : ['id', 'tipo', 'cod_tarifa', 'base_rate', 'overrate_weight', 'type_rate', 'ultima_actualizacion', 'estado'],
    'Tipo'       : ['int', 'str', 'str', 'float', 'float', 'float', 'text', 'boolean'],
    'Descripción': ['Identificador único de cada tarifa',
                    'Tipo de vehículo al que corresponde la tarifa',
                    'Código de la tarifa',
                    'Tasa base',
                    'Tasa adicional por peso (aplicable a vehículos de carga)',
                    'Tasa adicional por tipo de vehículo',
                    'Fecha de la última actualización de la tarifa',
                    'Indica si la tarifa está activa (1) o inactiva (0)']
                    })

    vehiculos_df = pd.DataFrame({
    'Campo'      : ['id', 'tipo', 'marca', 'modelo', 'nro_ruedas',  'velocidad', 'cilindrada', 
                    'puestos', 'carga_kgs', 'tipo_bici', 'motor', 'cuadro','nro_radios', 
                    'estado_cobro', 'fecha_actualizacion'],
    'Tipo'       : ['int', 'str', 'str', 'str', 'int',  'int', 'int', 
                    'int', 'int', 'str', 'str', 'str','int', 
                    'boolean', 'text'],
    'Descripción': ['Identificador único de cada vehículo',
                    'Tipo de vehículo (Particular, Carga, Bicicleta, Motocicleta)',
                    'Marca del vehículo',
                    'Modelo del vehículo',
                    'Número de ruedas del vehículo',
                    'Velocidad máxima del vehículo',
                    'Cilindrada del motor',
                    'Número de asientos',
                    'Capacidad de carga en kilogramos',
                    'Tipo de bicicleta (urbana, montaña, etc.)',
                    'Tipo de motor',
                    'Tipo de cuadro',
                    'Número de radios de las ruedas (para bicicletas)',
                    'Indica si el vehículo ha sido cobrado (1) o no (0)',
                    'Fecha de la última actualización del registro del vehículo']
                })
    
    st.subheader("Diccionario de datos: Base de Datos VEHICULOS.DB")
    st.markdown('''
            Algunas consideraciones sobre el modelo de datos del prototipo (MVP)
            
            * **Campos tipo DATE:** SQLite no posee un tipo de dato "date", por lo que se usa el tipo TEXT y se hacen las conversiones.
            * **PK y FK:** No se ha definido índices ni FK, por el volumen de datos y tratarse de un MVP.
            * **Campos redundantes:** Algunos campos podrían ser redundantes, como el tipo de vehículo en la tabla Recaudacion, ya que esta información podría obtenerse de la tabla Vehiculos.
            * **Recaudacion y Vehiculos:** Están relacionadas por el id, porque para cada cobro, hay un único vehículo, y por el  tipo de vehículo (aunque no está explícito en el esquema actual).
            * **Recaudacion y Tarifario:** Están relacionadas por el tipo de vehículo y el código de tarifa utilizado para calcular el cobro.
        ''')
    
    st.write("Tabla Recaudacion")
    st.table(recaudacion_df)

    st.write("Tabla Tarifario")
    st.table(tarifario_df)

    st.write("Tabla Vehiculos")
    st.table(vehiculos_df)

    
# *****************************************************************************
# *************************PAGINA INGRESO**************************************
# ************ESTA ES LA PÁGINA PARA INSERTAR VEHÍCULOS************************

def pagina_ingreso(): 
    '''
    En Streamlit cada página se construye como una función.
    
    Se usan las clases del framework para construir objetos como
    
    tablas o inputs
    
    Parámetros: None
    
    Retorna: Renderiza la página según las clases utilizadas
    '''
    st.title('SECCION: Ingreso de Vehículos')
    
    # Función para insertar vehículos en la base de datos
    def insertar_vehiculo(vehiculo):
        '''
        Abre una conexión a la bbdd y realiza una inserción
        de uno o más registros nuevos.
        
        Parámetros: Recibe una tupla y valida el número de argumentos
        que se le pasan.
        
        Retorna: Nuevos datos que se verán reflejados en la tabla vehículos en 
        estado de cobro=0, esperando ser procesados en recaudación.
        '''
        # Primero validamos que los datos pertenezcan a la clase superclase y, además, 
        # se verifica la cardinalidad de los argumentos que se le pasan
        
        if not isinstance(vehiculo, tuple) or len(vehiculo) != 14: # Validamos la clase y el tipo usando el metodo 'isinstance'
            raise ValueError(f'La tupla no es válida, debe tener 14 elementos, pero tiene {len(vehiculo)}')
        
        # Luego de algunos problemas validando la tupla, encontré que, para asegurarnos, al prepararla antes de
        # insertar los datos, convertimos valores None a cadenas vacías o ceros, según correspondía para controlar 
        # cualquier excepción por tipo de dato en las validaciones. Finalmente, modifique la forma de crear los registros
        # y corregí los datos históricos para que fuesen consistentes desde el orígen. Se mantuvo la validación. 
        
        vehiculo = tuple(str(val) if val is None else val for val in vehiculo)
        
        # Abrimos la conexión a la BBDD e instanciamos un cursor
        try:
            # pepinillo, nombre de mi conexión, se puede llamar de cualquier forma
            pepinillo = sqlite3.connect('vehiculos.db') 
            cursor    = pepinillo.cursor()
            cursor.execute('''
                           INSERT INTO vehiculos (tipo, marca, modelo, nro_ruedas, velocidad, 
                           cilindrada, puestos, carga_kgs, tipo_bici, motor, cuadro, nro_radios, 
                           estado_cobro, fecha_actualizacion) 
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', vehiculo )            
            pepinillo.commit()  # Actualizamos la BBDD
            
        except sqlite3.Error as e:
            print('Error al insertar vehículo:', e)
        finally:
            if pepinillo:
                pepinillo.close()
    
      
    # ''Función para mostrar sólo los vehículos que no han sido procesados (where estado_cobro = 0) todos los vehículos almacenados
    def mostrar_vehiculos():
        '''
        Abre una conexión a la bbdd y realiza una consulta sql
        
        Parámetros: None
        
        Retorna: Todos los datos de la tabla vehículos.
        Para este MVP, es viable hacer un select*, 
        al crecer la base será necesario implementar más filtros
        '''
        pepinillo = sqlite3.connect('vehiculos.db')
        df_flag        = pd.read_sql('SELECT * FROM vehiculos WHERE estado_cobro = 0', pepinillo) # La consulta es convertida en dataframe, facilitando otros procesos
        pepinillo.close()
        return df_flag
  
    # Creamos una lista para almacenar temporalmente los vehículos
    lst_alta_vehiculos = []

    # Preguntamos al usuario cuántos vehículos desea crear
    v_num_vehiculos = st.number_input("¿Cuántos vehículos desea crear?", min_value=1, step=1)
    
    # Agregamos una fecha, con la fecha de la actualización del registro o, con la fecha de la operación de alta del vehículo
    v_fecha_operacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for i in range(v_num_vehiculos):
        st.subheader(f"Ingrese los datos del vehículo {i + 1} de {v_num_vehiculos}...")

        # Selección de tipo de vehículo
        v_tipo_vehiculo = st.selectbox(f"Seleccione el tipo de vehículo {i + 1}", 
                                    ["Particular", "Carga", "Bicicleta", "Motocicleta"])

        # Datos comunes a todos los vehículos
        v_marca         = st.text_input(f"Marca del vehículo {i + 1}")
        v_modelo        = st.text_input(f"Modelo del vehículo {i + 1}")
        v_nro_de_ruedas = st.selectbox(f"Número de ruedas del vehículo {i + 1}", [2, 4, 6, 8, "Otro"])

        if v_nro_de_ruedas == "Otro":
            v_nro_de_ruedas = st.number_input(f"Ingrese el número de ruedas para el vehículo {i + 1}", min_value = 1, max_value = 12)

        if v_tipo_vehiculo == "Particular":
            v_velocidad  = st.number_input(f"Velocidad del vehículo {i + 1} en km/h", min_value = 0, max_value = 260)
            v_cilindrada = st.number_input(f"Cilindrada del vehículo {i + 1} en cc",  min_value = 0, max_value = 9999)
            v_puestos    = st.number_input(f"Número de puestos del vehículo {i + 1}", min_value = 1, max_value = 10)
            vehiculo     = ("Particular", v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada, 
                            v_puestos, 0, '', 0, '', 0, 0, v_fecha_operacion)

        elif v_tipo_vehiculo == "Carga":
             v_velocidad  = st.number_input(f"Velocidad del vehículo {i + 1} en km/h", min_value = 0, max_value = 260)
             v_cilindrada = st.number_input(f"Cilindrada del vehículo {i + 1} en cc", min_value  = 0, max_value = 9999)
             v_carga_kgs  = st.number_input(f"Capacidad de carga del vehículo {i + 1} en kg", min_value = 0)
             vehiculo     = ("Carga", v_marca, v_modelo, v_nro_de_ruedas, v_velocidad, v_cilindrada, 
                            1, v_carga_kgs, '', '', '', 0, 0, v_fecha_operacion)

        elif v_tipo_vehiculo == "Bicicleta":
             v_tipo_de_bicicleta = st.selectbox(f"Tipo de bicicleta {i + 1}", ["Urbana", "Carrera"])
             vehiculo            = ("Bicicleta", v_marca, v_modelo, v_nro_de_ruedas, 0, 0, 1, 0, 
                                 v_tipo_de_bicicleta, '', '', 0, 0, v_fecha_operacion)

        elif v_tipo_vehiculo == "Motocicleta":
             v_tipo_de_bicicleta = st.selectbox(f"Tipo de bicicleta {i + 1}", ["Urbana", "Carrera", "Deportiva"])
             v_motor             = st.selectbox(f"Tipo de motor {i + 1}", ["2T", "4T"])
             v_cuadro            = st.selectbox(f"Tipo de cuadro {i + 1}", ["Doble Cuna", "Multitubular", "Doble Viga"])
             v_nro_radios        = st.number_input(f"Número de radios {i + 1}", min_value = 0)
             vehiculo            = ("Motocicleta", v_marca, v_modelo, v_nro_de_ruedas, 0, 0, 1, 0, 
                                 v_tipo_de_bicicleta, v_motor, v_cuadro, v_nro_radios, 0, v_fecha_operacion)

        lst_alta_vehiculos.append(vehiculo) # Creamos una lista que irá guardando los vehículos creados
        
        if st.button(f"Agregar vehículo {i + 1}"):    
            insertar_vehiculo(vehiculo)
            st.success(f"Vehículo {i + 1} agregado exitosamente")
    
    # Mostrar resumen de los vehículos ingresados
    st.subheader("Vehículos ingresados")
    df_vehiculos = mostrar_vehiculos()
    st.dataframe(df_vehiculos)
#''    
# *****************************************************************************
# *************************PAGINA CONSULTA*************************************
# **********ESTA ES LA PÁGINA PARA REALIZAR VARIOS TIPOS DE CONSULTAS**********
    
def pagina_consulta(): 
    st.title("SECCIÓN: Consulta Vehículos y Recaudación")

    # Conectar a la base de datos
    pepinillo = sqlite3.connect('vehiculos.db')

    # Obtener los tipos de vehículos, marcas y modelos disponibles para los filtros
    lst_tipos_vehiculo   = pd.read_sql("SELECT DISTINCT tipo FROM vehiculos", pepinillo)['tipo'].tolist()
    lst_marcas_vehiculo  = pd.read_sql("SELECT DISTINCT marca FROM vehiculos", pepinillo)['marca'].tolist()
    lst_modelos_vehiculo = pd.read_sql("SELECT DISTINCT modelo FROM vehiculos", pepinillo)['modelo'].tolist()

    # Opciones de consulta predefinidas
    lst_opciones_consulta = ["Por tipo de vehículo", "Por rango de fechas", "Vehículos procesados en un día", "Ingresos recaudados por día o rango"]
    v_tipo_consulta       = st.selectbox("Seleccione el tipo de consulta", lst_opciones_consulta)

    # Campos de entrada según el tipo de consulta seleccionada
    v_tipo_vehiculo = None
    v_fecha_inicio = None
    v_fecha_fin = None

    if v_tipo_consulta == "Por tipo de vehículo":
        v_tipo_vehiculo = st.multiselect("Seleccione el tipo de vehículo", lst_tipos_vehiculo)

    elif v_tipo_consulta == "Por rango de fechas":
        v_fecha_inicio = st.date_input("Fecha de inicio")
        v_fecha_fin    = st.date_input("Fecha fin")

        # Campos adicionales para filtrar
        marca  = st.multiselect("Seleccione la marca", lst_marcas_vehiculo)
        modelo = st.multiselect("Seleccione el modelo", lst_modelos_vehiculo)
        v_tipo_vehiculo = st.multiselect("Seleccione el tipo de vehículo (opcional)", lst_tipos_vehiculo)

    elif v_tipo_consulta == "Vehículos procesados en un día":
        st.write('Ingrese fechas de inicio y fin o, si es el mismo día, inicio y fin son iguales')
        v_fecha_inicio = st.date_input("Fecha de inicio")
        v_fecha_fin    = st.date_input("Fecha fin")

    elif v_tipo_consulta == "Ingresos recaudados por día o rango":
        st.write('Ingrese fechas de inicio y fin o, si es el mismo día, inicio y fin son iguales')
        v_fecha_inicio = st.date_input("Fecha de inicio")
        v_fecha_fin    = st.date_input("Fecha fin")

    # Botón para ejecutar la consulta
    if st.button("Ejecutar consulta", key='ejecutar_consulta'):
        try:
            df_flag = pd.DataFrame()  # Inicializamos un df vacío fuera del bloque if
            
            if v_tipo_consulta == "Por tipo de vehículo":
                if v_tipo_vehiculo:
                    query = "SELECT * FROM vehiculos WHERE tipo IN ({})".format(','.join('?'*len(v_tipo_vehiculo)))
                    df_flag = pd.read_sql(query, pepinillo, params=v_tipo_vehiculo)
                else:
                    st.warning("Debe seleccionar al menos un tipo de vehículo.")

            elif v_tipo_consulta == "Por rango de fechas":
                if v_fecha_inicio and v_fecha_fin:
                    query = """
                        SELECT v.*, r.fecha_operacion, r.cobro 
                        FROM vehiculos v 
                        INNER JOIN recaudacion r ON v.id = r.id
                        WHERE r.fecha_operacion BETWEEN ? AND ?
                    """
                    params = [v_fecha_inicio, v_fecha_fin]

                    if marca:
                        query += " AND v.marca IN ({})".format(','.join('?'*len(marca)))
                        params.extend(marca)

                    if modelo:
                        query += " AND v.modelo IN ({})".format(','.join('?'*len(modelo)))
                        params.extend(modelo)

                    if v_tipo_vehiculo:
                        query += " AND v.tipo IN ({})".format(','.join('?'*len(v_tipo_vehiculo)))
                        params.extend(v_tipo_vehiculo)

                    df_flag = pd.read_sql(query, pepinillo, params=params)
                else:
                    st.warning("Debe seleccionar un rango de fechas.")

            elif v_tipo_consulta == "Vehículos procesados en un día":
                if v_fecha_inicio and v_fecha_fin:
                    query = '''
                        SELECT DATE(r.fecha_operacion) as fecha, v.tipo, COUNT(*) AS cantidad_vehiculos 
                        FROM recaudacion r
                        INNER JOIN vehiculos v ON v.id = r.id
                        WHERE DATE(r.fecha_operacion) BETWEEN ? AND ?
                        GROUP BY fecha, v.tipo
                    '''
                    df_flag = pd.read_sql(query, pepinillo, params=(v_fecha_inicio, v_fecha_fin))
                else:
                    st.warning("Debe seleccionar un rango de fechas.")

            elif v_tipo_consulta == 'Ingresos recaudados por día o rango':
                if v_fecha_inicio and v_fecha_fin:
                    query = """
                        SELECT DATE(r.fecha_operacion) as fecha, v.tipo, SUM(r.cobro) AS total_recaudado
                        FROM recaudacion r
                        INNER JOIN vehiculos v ON v.id = r.id
                        WHERE r.fecha_operacion BETWEEN ? AND ?
                        GROUP BY fecha, v.tipo
                    """
                    df_flag = pd.read_sql(query, pepinillo, params=(v_fecha_inicio, v_fecha_fin))

                    # Calcular el total general
                    total_general = df_flag['total_recaudado'].sum()

                    # Agregar fila con el total general usando pd.concat
                    total_row = pd.DataFrame({'fecha': ['TOTAL'], 'tipo': ['TODOS'], 'total_recaudado': [total_general]})
                    df_flag = pd.concat([df_flag, total_row], ignore_index=True)
                else:
                    st.warning("Debe seleccionar un rango de fechas.")

            # Guardar los resultados en la sesión (solo si df tiene datos)
            if not df_flag.empty:
                st.session_state['df_consulta'] = df_flag
                st.dataframe(df_flag)
            else:
                st.warning("No se encontraron resultados para esta consulta.")

        except Exception as e:
            st.error(f"Error al ejecutar la consulta: {str(e)}")

    # Opciones de exportación
    if 'df_consulta' in st.session_state and not st.session_state['df_consulta'].empty:
        with st.expander("Exportar resultados"):
            opcion_exportar = st.radio("Seleccione el formato de exportación", ('CSV', 'Excel', 'PDF'), key='export_option')

            if st.button("Convertir", key='convertir1'):
                df_consulta = st.session_state['df_consulta']

                if opcion_exportar == 'CSV':
                    csv = df_consulta.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Descargar como CSV",
                        data=csv,
                        file_name='consulta.csv',
                        mime='text/csv',
                        key='download_csv'
                    )

                elif opcion_exportar == 'Excel':
                    try:
                        import xlsxwriter
                        output = BytesIO()
                        writer = pd.ExcelWriter(output, engine='xlsxwriter')
                        df_consulta.to_excel(writer, sheet_name='Consulta', index=False)
                        writer.close()
                        output.seek(0)
                        st.download_button(
                            label="Descargar como Excel",
                            data=output,
                            file_name="consulta.xlsx",
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            key='download_excel'
                        )
                    except Exception as e:
                        st.error(f"Error al exportar a Excel: {str(e)}")

                elif opcion_exportar == 'PDF':
                    try:
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", size=12)
                        pdf.cell(200, 10, txt="Resultados de la Consulta", ln=1, align='C')

                        for i, row in df_consulta.iterrows():
                            pdf.cell(200, 10, txt=f"{row.to_string(index=False)}", ln=1)

                        pdf_output = pdf.output(dest='S').encode('latin-1')

                        st.download_button(
                            label="Descargar como PDF",
                            data=pdf_output,
                            file_name='consulta.pdf',
                            mime='application/pdf',
                            key='download_pdf'
                        )
                    except Exception as e:
                        st.error(f"Error al exportar a PDF: {str(e)}")
    else:
        st.write("No hay datos para exportar.")

    pepinillo.close()


# ''*****************************************************************************
# ***************************PAGINA MODIFICAR VEHÍCULO*************************
# ***********PÁGINA PARA ACTUALIZAR O CORREGIR INFORMACIÓN VEHÍCULOS***********           

# **************BLOQUE 1: PRE-PROCESOS MODIFICAR REGISTRO*********************
# *****************************************************************************

def f_ejecutar_update(dic_veh_modificado, vehiculo_id, conexion):
    """
    Realiza el UPDATE en la base de datos
    
    Parámetros: Recibe un diccionario, un id y un string de conexión
    
    Retorna: Mensaje de confirmación
    """
    st.write('Solo para estar seguros:', dic_veh_modificado, vehiculo_id) # Se hace una verificación, volcando el contenido de las variables que serán procesadas en este bloque 
    valores = [v if v is not None and v != "" else "valor_por_defecto" for v in valores]
    try:
        v_fecha_actualizacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Se captura la fecha de hoy en formato largo
        dic_veh_modificado['fecha_actualizacion'] = v_fecha_actualizacion    # Se agrega la fecha de la operación al diccionario

        # Construcción dinámica del UPDATE
        #campos  = ", ".join([f"{campo} = ?" for campo in dic_veh_modificado.keys()]) # Se itera sobre las claves del diccionario para crear una etiqueta y mostrar su contenido 
        #valores = list(dic_veh_modificado.values())                                  # Lista con los valores del diccionario (lo que queremos modificar)
        #valores.append(vehiculo_id)                                                  # Se agrega el id del vehículo a la lista valores, que contiene los valores
        #query = f"UPDATE vehiculos SET {campos} WHERE id = ?"                        # armamos la query con un set que contiene los datos campo
        
        # Construcción dinámica de la consulta utilizando un diccionario para mapear campos y valores
        campos_valores = {campo: valor for campo, valor in dic_veh_modificado.items()}
        campos_valores['id'] = vehiculo_id  # Agregar el id al diccionario
        placeholders = ', '.join(f"{campo} = :{campo}" for campo in campos_valores)
        query = f"UPDATE vehiculos SET {placeholders}"

        # Ejecución del UPDATE
        cursor = conexion.cursor()
        cursor.executemany(query, campos_valores) # En query le paso los campos que quiero modificar y en la lista valores los "valores"  
        conexion.commit()
        logging.debug(f"Query ejecutada: {query}")
        logging.debug(f"Valores: {valores}")
        st.success(f"Registro con ID {vehiculo_id} actualizado correctamente.")
    except Exception as e:
        logging.error(f"Error al actualizar el registro: {e}")
        st.error(f"Error al actualizar el registro: {e}")


    # *************************************************************************
    # *********************BLOQUE 2: BUSQUEDA DRILLDOWN ***********************
    
def f_buscar_registro(conexion):
    # Primero, creamos una query para obtener todos los registros, incluidos los campos de la tabla Recaudacion
    
    query_union = """
        SELECT v.*, r.fecha_operacion, r.cod_op 
        FROM vehiculos v 
        JOIN recaudacion r ON v.id = r.id
    """

    # Para facilitar el manejo de los datos del cursor, lo convertimos en un dataframe
    df_vehiculos = pd.read_sql(query_union, conexion)

    # Filtro Drill-Down
    tipo_seleccionado   = st.selectbox("Selecciona el tipo de vehículo", df_vehiculos['tipo'].unique())
    marcas_filtradas    = df_vehiculos[df_vehiculos['tipo'] == tipo_seleccionado]['marca'].unique()
    marca_seleccionada  = st.selectbox("Selecciona la marca", marcas_filtradas)
    modelos_filtrados   = df_vehiculos[(df_vehiculos['tipo'] == tipo_seleccionado) & (df_vehiculos['marca'] == marca_seleccionada)]['modelo'].unique()
    modelo_seleccionado = st.selectbox("Selecciona el modelo", modelos_filtrados)
    
    # Implementamos un filtro por rango de fecha que facilita al usuario refinar su búsqueda
    v_fecha_inicio = st.date_input("Fecha de inicio")
    v_fecha_fin    = st.date_input("Fecha de fin")
    
    # Creamos la query para rango fecha
    query_fecha = '''
                SELECT v.*, r.fecha_operacion, r.cod_op
                FROM vehiculos v
                JOIN recaudacion r ON v.id = r.id
                WHERE v.tipo = ?
                AND v.marca = ?
                AND v.modelo = ?
                AND r.fecha_operacion BETWEEN ? AND ?
            '''
    # Ejecutamos la consulta con los parámetros y generamos el df
    df_filtrado = pd.read_sql(query_fecha, conexion, params=(tipo_seleccionado, marca_seleccionada, modelo_seleccionado, v_fecha_inicio, v_fecha_fin))
    st.dataframe(df_filtrado)
    
    # Filtro por código de operación
    cod_op_filtrado = st.selectbox("Selecciona un código de operación", df_filtrado['cod_op'].unique())
    
    # Mostrar el registro filtrado
    registro_final = df_filtrado[df_filtrado['cod_op'] == cod_op_filtrado]
    if not registro_final.empty:
        st.write(registro_final)
        return registro_final.to_dict(orient='records')[0]  # Devolver el registro como diccionario
    else:
        st.warning("No se encontró ningún registro.")
        return None

    # ***********************************************************************************
    # ***************************BLOQUE 3: EDITA Y COMPARA REGISTROS ********************

def f_editar_registro(dic_veh_a_modificar, conexion): # Falta chequear por qué no recibe la conexión a la bbdd, es un error
    if dic_veh_a_modificar:
        st.write('Editar el registro')

        dic_veh_modificado = dic_veh_a_modificar.copy() # Generamos una copia para poder comparar después de los cambios
        for key, value in dic_veh_a_modificar.items():
            if key != 'id':                             # Impedimos que se modifique el id por error
                dic_veh_modificado[key] = st.text_input(f'{key}', value)

        if st.button('Guardar cambios', key='guardar_cambios1'):
            # Compara los diccionarios para detectar los cambios
            if dic_veh_modificado != dic_veh_a_modificar:
                # Mostrar los cambios
                cambios = {key: (dic_veh_a_modificar[key], dic_veh_modificado[key]) for key in dic_veh_modificado if dic_veh_modificado[key] != dic_veh_a_modificar[key]}
                for campo, (valor_antiguo, valor_nuevo) in cambios.items():
                    st.write(f'{campo}: {valor_antiguo} -> {valor_nuevo}')
                
                if st.button('Confirmar cambios', key='confirmar_cambios'):
                    # Asegurarse de que los valores vacíos sean cadenas vacías
                    for key in dic_veh_modificado:
                        if dic_veh_modificado[key] is None:
                            dic_veh_modificado[key] = " "

                    # Construir la tupla de valores para la actualización
                    
                    valores = tuple(dic_veh_modificado.values())
                    return valores
            else:
                st.warning("No se detectaron cambios.")
    else:
        st.error("No se seleccionó ningún registro para modificar.")

def pagina_modificarV():
    st.title("SECCIÓN: Modificar Datos Vehículo")
    
    # Conectar a la base de datos
    pepinillo = sqlite3.connect('vehiculos.db')
      
    # BLOQUE 2: Buscar y seleccionar un vehículo para modificar
    dic_veh_a_modif = f_buscar_registro(pepinillo)
    
    if dic_veh_a_modif:
        dic_veh_modificado = f_editar_registro(dic_veh_a_modif, pepinillo)
        
        if dic_veh_modificado:
            # Verifica cambios entre los datos originales y los modificados
            cambios = {
                key: dic_veh_modificado[key] for key in dic_veh_modificado
                if dic_veh_modificado.get(key) != dic_veh_a_modif.get(key)
            }
            
            if st.button("Guardar cambios", key="guardar_cambios2"):
                if cambios:
                    st.write("Cambios detectados:", cambios)
                    
                    try:
                        # Asegúrate de que se pase dic_veh_a_modif como el diccionario original
                        f_ejecutar_update(dic_veh_modificado, dic_veh_a_modif['id'], pepinillo)
                        st.success("Registro actualizado correctamente.")
                    except Exception as e:
                        st.error(f"Error al actualizar el registro: {str(e)}")
                else:
                    st.error("No se detectaron cambios.")
        else:
            st.warning("No se detectaron modificaciones en el formulario.")
    else:
        st.warning("No se ha seleccionado ningún vehículo para modificar.")
    
    # Cerrar la conexión a la base de datos
    pepinillo.close()


# *****************************************************************************
# ****************************PAGINA MODIFICAR TARIFA**************************
# ***********PÁGINA PARA ACTUALIZAR O CORREGIR INFORMACIÓN TARIFARIA***********  

# Armamos la consulta dinámica SQL que recibe una query y parámetros
def f_query_gral(query, params=()):
    """
    Establece una conexión y ejecuta una query dinámica con sus parámetros
    
    Parámetros: Recibe una query variable y y parámetros de la consulta
    
    Retorna: Los registros de la bbdd que coinciden con los parámetros de la query
    """
    pepinillo    = sqlite3.connect('vehiculos.db')
    cursor       = pepinillo.cursor()
    cursor.execute(query, params)
    pepinillo.commit()
    v_resultados = cursor.fetchall()
    pepinillo.close()
    return v_resultados

# Función para actualizar el estado de una tarifa
def f_cambiar_estado_tarifa(v_codigo_tarifa_a_modificar, estado):
    """
    Ejecuta la modificación de una tarifa seleccionada
    
    Parámetros: Un código de tarifa de la forma abc-### y un estado booleano 0/1
    
    Retorna: Mensaje de confirmación
    
    """
    query = "UPDATE tarifario SET estado = ? WHERE cod_tarifa = ?"
    f_query_gral(query, (estado, v_codigo_tarifa_a_modificar))
    return st.success("Tarifa actualizada correctamente.")
    
# Página para crear o modificar tarifas
def pagina_modificarT():
    """
    'Renderiza una página streamlit con el formulario para crear una nueva tarifa o modificar una existente.
    
    Parámetros: None
    
    Retorna: Un formulario y una tabla
    """
    st.title("SECCIÓN: Crear o Modificar Tarifas")

    # Muestra opciones para crear o modificar
    v_guarda_opcion = st.selectbox("Seleccione una opción", ["Crear Nueva Tarifa", "Modificar Tarifa Existente"])

    # Conectar a la base de datos y obtener los datos de la tabla tarifario
    tarifas    = f_query_gral("SELECT * FROM Tarifario") # trae todos los registros de la tabla Tarifario 
    df_tarifas = pd.DataFrame(tarifas, columns = ['id', 'tipo', 'cod_tarifa', 'base_rate', 'overrate_weight', 'type_rate', 'ultima_actualizacion', 'estado'])
    st.dataframe(df_tarifas)

    if v_guarda_opcion == "Crear Nueva Tarifa":
        # Crear un formulario para ingresar los datos de la nueva tarifa
        with st.form("crear_tarifa"):
            tipo            = st.selectbox("Tipo de tarifa", ["Particular", "Carga", "Motocicleta", "Bicicleta", "Emergencia"])
            base_rate       = st.number_input("Tarifa base")
            overrate_weight = st.number_input("Sobretarifa por peso")
            type_rate       = st.number_input("Tarifa por tipo")

            # Generar el código de tarifa automáticamente
            ultimo_id  = df_tarifas['id'].max()
            nuevo_id   = ultimo_id + 1
            cod_tarifa = f"{tipo[:3].lower()}-{str(nuevo_id).zfill(3)}" # zfill rellena con 0 hasta completar la cifra en este caso forma el código

            # Botón para enviar el formulario
            v_crear_tarifa = st.form_submit_button("Crear Tarifa")
            if v_crear_tarifa:
                # Validar los datos
                if base_rate > 0 and type_rate >= 0:
                    # Insertar la nueva tarifa en la base de datos
                    query = """
                    INSERT INTO tarifario (tipo, cod_tarifa, base_rate, overrate_weight, type_rate, ultima_actualizacion, estado)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """
                    fecha_actualizacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    f_query_gral(query, (tipo, cod_tarifa, base_rate, overrate_weight, type_rate, fecha_actualizacion, 1))
                    st.success(f"Tarifa {cod_tarifa} creada con éxito.")
                else:
                    st.error("Los valores ingresados no son válidos. Asegúrese de que las tarifas sean correctas.")

    elif v_guarda_opcion == "Modificar Tarifa Existente":
        # Permite al usuario seleccionar la tarifa a modificar
        v_codigo_tarifa_a_modificar = st.selectbox("Selecciona el tipo de vehículo", df_tarifas['cod_tarifa'].unique())
        
        # Obtiene los datos de la tarifa seleccionada
        v_tarifa_seleccionada = f_query_gral("SELECT * FROM tarifario WHERE id = ?", (v_codigo_tarifa_a_modificar,))
        if v_tarifa_seleccionada:
            v_tarifa = v_tarifa_seleccionada[0]
            with st.form("modificar_tarifa"):
                tipo = st.selectbox("Tipo de tarifa", ["Particular", "Carga", "Motocicleta", "Bicicleta", "Emergencia"], index=["Particular", "Carga", "Motocicleta", "Bicicleta", "Emergencia"].index(v_tarifa[1]))
                base_rate       = st.number_input("Tarifa base", value          = v_tarifa[3])
                overrate_weight = st.number_input("Sobretarifa por peso", value = v_tarifa[4])
                type_rate       = st.number_input("Tarifa por tipo", value      = v_tarifa[5])

                v_modifica_tarifa = st.form_submit_button("Modificar Tarifa")
                if v_modifica_tarifa:
                    # Actualizar la tarifa en la base de datos
                    if base_rate > 0 and type_rate >= 0:
                        # Cambia el estado de la tarifa anterior a 0 y la nueva a 1
                        f_cambiar_estado_tarifa(v_codigo_tarifa_a_modificar, 0)
                        query = """
                        UPDATE tarifario
                        SET tipo = ?, base_rate = ?, overrate_weight = ?, type_rate = ?, ultima_actualizacion = ?, estado = ?
                        WHERE cod_tarifa = ?
                        """
                        fecha_actualizacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        f_query_gral(query, (tipo, base_rate, overrate_weight, type_rate, fecha_actualizacion, 1, v_codigo_tarifa_a_modificar))
                        st.success(f"Tarifa {v_tarifa[2]} modificada con éxito.")
                    else:
                        st.error("Los valores ingresados no son válidos.")
        else:
            st.error("No se encontró la tarifa con el código proporcionado.")
    
# '*****************************************************************************
# ****************************PAGINA PROCESO COBRANZA**************************
# ****SE PROCESAN LAS ALTAS DE VEHÍCULOS EN ESTADO 0, O PENDIENTES DE COBRO****     

# Lógica pre-proceso de cobro    
def f_generar_codigo(length):
    """
    Genera un código alfanumérico de 8 caracteres
    esto permite individualizar la transacción y diferenciarla
    con distintos propósitos (ACID)
    
    Parámetros: Recibe un largo de cadena, valor entero positivo 
    
    Retorna: Código alfanumérico de 8 caracteres de tipo string
    """
    v_cod_alfanum = string.ascii_letters + string.digits # Crea un conjunto de números y letras
    return ''.join(random.choice(v_cod_alfanum) for i in range(length)) # Escoge y une 8 caracteres del conjunto
    
def f_cobro(v_tipo_vehiculo):
    """
    Aplica una tarifa en función del tipo de vehículo
    
    Parámetros: Recibe una cadena con el tipo de vehículo
    
    Retorna: Un valor float con el calculo del cobro    
    """
    # Establece una conexión con la base de datos
    pepinillo = sqlite3.connect('vehiculos.db')
    cursor    = pepinillo.cursor()

    # Consultamos la tarifa correspondiente al tipo de vehículo
    cursor.execute("SELECT base_rate, overrate_weight, type_rate FROM Tarifario WHERE tipo=?", (v_tipo_vehiculo,))
    row = cursor.fetchone()  # Retorna 1 registro o fila

    # Calculamos la tarifa
    base_rate, overrate_weight, type_rate = row     # desempaquetamos la fila
    cobro = base_rate + overrate_weight + type_rate # Calcula la tarifa según sus coeficientes del polinomio

    pepinillo.close()
    return cobro # Devuelve un float

# Función principal que renderiza la página
def pagina_cobro():
    st.title("SECCIÓN: Cobro Peaje")
    
    # Conexión a la BBDD y creación de un objeto cursor
    pepinillo = sqlite3.connect('vehiculos.db', check_same_thread=False)
    cursor    = pepinillo.cursor()

    # Obtenemos los vehículos pendientes de cobro al inicio y los convierte en un df
    df_pendientes = pd.read_sql("SELECT * FROM vehiculos WHERE estado_cobro = 0", pepinillo)
    
    if df_pendientes.empty: # Valida que la consulta no retorne vacía
        st.write("No hay registros pendientes de cobro.")
        procesado_previamente = True # Flag para validación
    else:
        st.dataframe(df_pendientes)
        procesado_previamente = False
    
    # Lógica del proceso de cobro
    if st.button("Procesar Cobros", key='procesar_cobros') and not procesado_previamente:
        registros_procesados = []

        for index, row in df_pendientes.iterrows():
            id_vehiculo     = row['id']  # Obtener el id del vehículo
            v_tipo_vehiculo = row['tipo']

            # Calcular cobro
            cobro = f_cobro(v_tipo_vehiculo)
           
            # Insertar TIMESTAMP (es algo pretencioso decirle time stamp, pero cumple el proposito])
            fecha_operacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Generar código de operación
            cod_op = f_generar_codigo(8)

            # Actualizar registro en la base de datos
            cursor.execute("INSERT INTO Recaudacion (tipo, fecha_operacion, cobro, cod_op) VALUES (?, ?, ?, ?)",
                           (v_tipo_vehiculo, fecha_operacion, cobro, cod_op))
            cursor.execute("UPDATE vehiculos SET estado_cobro = 1 WHERE id = ?", (id_vehiculo,))
            registros_procesados.append({'tipo': v_tipo_vehiculo, 'fecha_operacion': fecha_operacion, 'cobro': cobro, 'cod_op': cod_op})

        pepinillo.commit()

        # Mostrar solo los registros procesados en este ciclo
        df_cobros_procesados = pd.DataFrame(registros_procesados)
        st.dataframe(df_cobros_procesados)
        st.write(f"La operación ha sido realizada con éxito. Se procesaron {len(df_cobros_procesados)} registros nuevos.")

        # Guardar el DataFrame en el estado de sesión para exportar
        st.session_state['df_cobros_procesados'] = df_cobros_procesados

    elif procesado_previamente:
        st.write("Todos los cobros ya han sido procesados.")

    # Opciones de exportación
    if 'df_cobros_procesados' in st.session_state and not st.session_state['df_cobros_procesados'].empty:
        with st.expander("Exportar resultados"):
            opcion_exportar = st.radio("Seleccione el formato de exportación", ('CSV', 'Excel', 'PDF'), key='export_option')

            if st.button("Convertir", key='convertir2'):
                df_cobros_procesados = st.session_state['df_cobros_procesados']
                
                if opcion_exportar == 'CSV':
                    # Convertimos el DataFrame en un archivo CSV y habilitamos la descarga
                    csv = df_cobros_procesados.to_csv(index = False).encode('utf-8')
                    st.download_button(
                        label     = "Descargar como CSV",
                        data      = csv,
                        file_name = 'cobros_procesados.csv',
                        mime      = 'text/csv',
                        key       = 'download_csv'
                    )
                
                elif opcion_exportar == 'Excel':
                    try:
                        import xlsxwriter
                        output = BytesIO()
                        writer = pd.ExcelWriter(output, engine = 'xlsxwriter')
                        df_cobros_procesados.to_excel(writer, sheet_name = 'Cobros', index = False)
                        writer.close()
                        output.seek(0)
                        st.download_button(
                            label     = "Descargar como Excel",
                            data      = output,
                            file_name = "cobros_procesados.xlsx",
                            mime      = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            key       = 'download_excel'
                        )
                    except ModuleNotFoundError:
                        st.error("El módulo xlsxwriter no está instalado. Instálalo usando 'pip install xlsxwriter'.")

                elif opcion_exportar == 'PDF':
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.cell(200, 10, txt="Tabla de Cobros Procesados", ln = 1, align = 'C')
                    
                    # Agregar los datos al PDF
                    for i, row in df_cobros_procesados.iterrows():
                        pdf.cell(200, 10, txt = f"{row['tipo']}, {row['fecha_operacion']}, {row['cobro']}, {row['cod_op']}", ln=1)
                    
                    # Obtener el contenido del PDF como bytes
                    pdf_output = pdf.output(dest = 'S').encode('latin-1')
                    
                    # Descarga del PDF
                    st.download_button(
                        label     = "Descargar como PDF",
                        data      = pdf_output,
                        file_name = 'cobros_procesados.pdf',
                        mime      = 'application/pdf',
                        key       = 'download_pdf'
                    )

    else:
        st.write("No hay datos para exportar.")

    pepinillo.close()


# *****************************************************************************
# *******************PAGINA PROCESO VALIDACIÓN DE INSTANCIAS*******************
# ********COMPARACIÓN Y VALIDACIÓN ENTRE CLASES E INSTANCIAS DE LA CLASE*******  

def pagina_valida():
    st.title("SECCIÓN: Chequea instancias")

    # Lista de clases disponibles para seleccionar
    clases_disponibles = ["Vehiculo", "Automovil", "Particular", "Carga", "Bicicleta", "Motocicleta"]
    
    # Creamos instancias de prueba
    particular_test  = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga_test       = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta_test   = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta_test = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Cuna", 21)
    vehiculo_test    = Vehiculo("Test", "Test", 4)
    automovil_test   = Automovil("Test", "Test", 4, 100, 1500)

    # Creamos un diccionario con los nombres de las clases y las instancias
    instancias = {
        "Vehiculo"    : vehiculo_test,
        "Automovil"   : automovil_test,
        "Particular"  : particular_test,
        "Carga"       : carga_test,
        "Bicicleta"   : bicicleta_test,
        "Motocicleta" : motocicleta_test
             }

    # Creamos un formulario con dos listas desplegables para que el usuario escoja qué quiere evaluar
    with st.form("form_comparacion_clases"):
        st.write("RECUERDA: La primera selección es la INSTANCIA y, la segunda, la CLASE.")
        clase_a = st.selectbox("Selecciona la primera clase (instancia)", clases_disponibles)
        clase_b = st.selectbox("Selecciona la segunda clase (clase)", clases_disponibles)

        # Agregamos un botón para realizar la comparación
        if st.form_submit_button("Comparar"):
            try:
                # Obtenemos las instancias correspondientes a los nombres seleccionados
                instancia_a = instancias[clase_a]
                clase_b_obj = globals()[clase_b]

                # Se realiza la comparación y se muestra el resultado
                resultado = isinstance(instancia_a, clase_b_obj)
                st.write(f"{clase_a} es instancia con relación a {clase_b}: {resultado}")
                
            except KeyError:
                st.error("Error: Clase o Instancia no encontrada.")
            except Exception as e:
                st.error(f"Ocurrió un error inesperado: {str(e)}")


#''****************************************************************************
# *******************************PAGINA DE AYUDA*******************************
# ****PROVEE INFORMACIÓN AL USUARIO SOBRE EL SISTEMA Y SOLUCIÓN A PROBLEMAS****  

def pagina_ayuda():
    st.title('SECCION: Manual de Usuario') # PROVEE INFORMACIÓN AL USUARIO SOBRE EL SISTEMA Y SOLUCIÓN A PROBLEMAS

    st.header('Introducción')
    st.markdown('El "Sistema de Peaje FS" es una herramienta diseñada para gestionar el registro y cobro de peajes para diferentes tipos de vehículos. Esta aplicación permite a los usuarios ingresar nuevos vehículos, consultar la base de datos, modificar tarifas y realizar cobros de peaje.')

    st.header('Guía de Inicio Rápido')
    st.write('1. Para instalar el sistema, siga las instrucciones del archivo "Readme", instale el archivo "requirements.txt" y luego, desde la consola, ejecute el comando "streamlit run peajesFSv0.8.py".')
    st.write('2. Después de un par de segundos aparecerá la interfaz')
    st.image('./assets/img/iniciorapido001.PNG')
    st.write('3. Finalmente, para comenzar a utilizar el sistema, simplemente seleccione la opción deseada en el menú lateral.')

    st.header('Acerca del Sistema')
    st.write('1. Por defecto el sistema despliega la página "Acerca del Sistema".')
    st.write('2. Si se halla en otra sección de la aplicación y desea volver al inicio, desde el menú lateral, basta seleccionar la opción "Acerca del Sistema".')
    st.write('3. Navegue por la sección, desplazándose con el scroll del mouse o con flecha arriba o flecha abajo.')
    st.write('4. Las imagenes se pueden expandir, basta presionar el borde superior derecho donde aparece un ícono con flechas opuestas.')
    st.image('./assets/img/acerca001.PNG')
    st.write('5. Luego de verlas con detalle, se pueden contraer, para ello basta presionar el borde superior derecho donde se verá, nuevamente, el ícono con flechas opuestas.')
    st.image('./assets/img/acerca002.PNG')
    
    st.header('Ingreso de Vehículos')
    st.write('1. Seleccione la opción "Ingreso de Vehículos" en el menú.')
    st.image('./assets/img/IngresoVeh002.PNG')
    st.write('2. Indique el número de vehículos que desea crear. Puede ingresar un valor o presionar los signos "+" y "-".')
    st.image('./assets/img/IngresoVeh003.PNG')
    st.write('3. Se abrirán tantos formularios como se haya indicado en el paso previo.')
    st.image('./assets/img/IngresoVeh001.PNG')
    st.write('4. Ingrese los datos del vehículo solicitados o seleccionelos de los menús desplegables, como marca, modelo y tipo.')
    st.image('./assets/img/Ingreso002.PNG')
    st.write('5. Una vez llenado un formulario, haga clic en "Agregar vehículo" para guardar los datos. ')
    st.image('./assets/img/Ingreso004.PNG')
    st.write('6. Verá que la tabla al pie se actualizará y mostrará que un registro ha sido agregado.')
    st.image('./assets/img/Ingreso001.PNG')
    
    st.header("Consulta Vehículos")
    st.write("1. Seleccione la opción 'Consulta Vehículos' en el menú.")
    st.image('./assets/img/Consultas001.PNG')
    st.write("2. Seleccione el tipo de consulta, por tipo de vehículo, rango de fechas, vehículos procesados o ingresos por día.")
    st.image('./assets/img/Consultas002.PNG')
    st.write("3. Luego selecciona el tipo de vehículo (Particular, Carga, Bicicleta, Motocicleta).")
    st.image('./assets/img/Consultas003.PNG')
    st.write("4. Ejecuta la consulta")
    st.image('./assets/img/Consultas004.PNG')    
    st.write("5. Puedes usar más de un filtro para personalizar tus consultas")
    st.image('./assets/img/Consultas005.PNG')
    st.write("6. Puedes buscar por rango de fechas.")
    st.image('./assets/img/Consultas007.PNG')
    st.write("7. También puedes aprovechar los widgets de la aplicación que permiten ver a pantalla completa, buscar por cadena o descargar a CSV.")
    st.image('./assets/img/Consultas008.PNG')
    st.write("8. Finalmente tienes la opción de convertir tu consulta a formato EXCEL, PDF o CSV.")
    st.image('./assets/img/Consultas006.PNG')

    
    st.header("Modificar Vehículo")
    st.write("1. Seleccione la opción 'Modificar Vehículo' en el menú.")
    st.image('./assets/img/ModificaVehiculo001.PNG')
    st.write("2. Se despliega un formulario para seleccionar los filtros.")
    st.image('./assets/img/ModificaVehiculo.PNG')
    st.write("3. Los filtros son progresivos de lo general a lo particular, utilice los menús desplegables o escoja las opciones.")
    st.image('./assets/img/ModificaVehiculo002.PNG')
    st.write("4. Luego de aplicar los filtros y si aún quedan registros para un mismo día, se selecciona por código de operación.")
    st.image('./assets/img/ModificaVehiculo003.PNG')    
    st.write("5. Definido un único registro, se despliega un formulario con sus campos editables.")
    st.image('./assets/img/ModificaVehiculo004.PNG')  
    st.write("6. Hechos los cambios, el sistema los detecta y muestra para su confirmación.")
    st.image('./assets/img/ModificaVehiculo005.PNG')
    st.write("7. Una vez confirmado el cambio retorna un mensaje de confirmación y actualiza la pantalla.")
    st.image('./assets/img/ModificaVehiculo006.PNG')

    
    st.header('Modificar Tarifas')
    st.write('1. Seleccione la opción "Modificar Tarifas" en el menú.')
    st.image('./assets/img/Tarifario005.PNG')
    st.write('2. Seleccione si desea crear una nueva tarifa o modificar una existente.')
    st.image('./assets/img/Tarifario006.PNG')
    st.write('3. Si escoge "Crear Nueva Tarifa", se despliega un formulario para ingresar los valores, al finalizar presiona "Crear Tarifa".')
    st.image('./assets/img/Tarifario001.PNG')
    st.write('4. Si escoge "Modificar Tarifa", escoge un código y se despliega un formulario para editar los valores, al finalizar presiona "Actualizar Tarifa".')
    st.image('./assets/img/Tarifario007.PNG') 
     
    st.header("Cobro Peaje")
    st.write("1. Seleccione la opción 'Cobro Peaje' en el menú.")
    st.image('./assets/img/cobro20.PNG')
    st.write('2. Para realizar el proceso de "Cobro", se requiere que existan cobros pendientes, es decir, vehículos creados, pero cuyo estado de cobro = 0')
    st.image('./assets/img/cobro19.PNG')
    st.write('3. Si no hay cobros pendientes, el sistema muestra un mensaje y la tabla vacía')
    st.image('./assets/img/cobro18.PNG')
    st.write('4. Para procesar los cobros, basta con presionar el botón "Procesar Cobros".')
    st.image('./assets/img/cobro02.PNG')    
    st.write('5. Una vez procesados los registros, se muestra un resumen indicando el número de operación único para cada registro.')
    v_col1, v_col2 = st.columns([2, 1])
    with v_col1:
        st.image('./assets/img/cobro03.PNG')
    with v_col2:
        st.image('./assets/img/cobro07.PNG')
    st.write('6. Finalmente, está la opción de generar un archivo como comprobante de la operación que se puede exportar a EXCEL, CSV o PDF.')
    st.image('./assets/img/cobro04.PNG')
    st.write('7. Luego de realizada la operación, si se refresca la pantalla, se observará que no hay registros pendientes.')
    st.image('./assets/img/cobro05.PNG')
    
    st.header("Valida Clases")
    st.write('1. Seleccione la opción "Valida Clases" en el menú.')
    st.image('./assets/img/ChequeaInstancias000.PNG')
    st.write('2. Escoja una instancia de clase y una clase, desde los menús desplegables y presione "Comparar".')
    st.image('./assets/img/ChequeaInstancias001.PNG')
    st.write("3. El sistema compara y retorna TRUE o FALSE, si una objeto, es o no, instancia de una clase.")
    v_col1, v_col2 = st.columns([2, 1])
    with v_col1:
        st.image('./assets/img/ChequeaInstancias004.PNG')
    with v_col2:
        st.image('./assets/img/ChequeaInstancias005.PNG')
    
    st.header("Solución de Problemas conocidos - Workarounds")
    st.write("Si encuentra algún problema, por favor, contacte al administrador del sistema.")
    st.write("**Errores conocidos:**")
    st.markdown('1. **Ingreso de vehículos:** Si se vuelve a presionar el botón de "Agregar Vehículo", se vuelve a crear otro objeto identico, no se ha controlado, pero basta con no hacerlo por ahora.')
    st.markdown('2. **Consultas:** Si se define un mismo día, es decir, fecha inicio = fecha final, no retorna resultados, igual para un rango, deja la fecha final fuera. Se produce porque hay fechas largas y cortas y significa limpiar la base o modificar los registros con fechas cortas. Para evitarlo, basta con agregar un día más al filtro.')
    st.markdown('3. **Modificar Vehículo y Modificar Tarifa:** No está realizando el update en la base de datos, es posible que los valores null o vacíos estén provocando el problema, es una funcionalidad opcional. Caso en estudio, prioridad baja.')
    st.markdown('4. **Librería "ExcelWriter" no instalada:** La versión local de la aplicación, funciona de acuerdo a lo que se indica en los manuales, incluyendo la exportación a los formatos EXCEL, CSV y PDF, sin embargo, **la versión WEB**, indica que la librería "ExcelWriter" no está presente y que debe importarse. Investigando el problema, esta es una 	librería de Pandas, que al parecer genera un conflicto en streamlit, por el manejo del contexto de las variables, objetos y su estado. Hay varias soluciones, como modificar el código importando otra librería más compatible, manejar callbacks, etc., pero por el alcance del MVP, no se implementarán por ahora.')

# ESTRUCTURA DEL MENU
# *******************

page = st.sidebar.selectbox("Menu:", ["Acerca del Sistema", "Ingreso de Vehículos", "Consulta Vehículos", "Modificar Vehículo", "Modificar Tarifas", "Cobro Peaje", "Valida Clases", "Manual de Usuario"])

if page == "Acerca del Sistema":
    pagina_principal()
elif page == "Ingreso de Vehículos":
    pagina_ingreso()
elif page == "Consulta Vehículos":
    pagina_consulta()
elif page == "Modificar Vehículo":
    pagina_modificarV()    
elif page == "Modificar Tarifas":
    pagina_modificarT()
elif page == "Cobro Peaje":
    pagina_cobro()
elif page == "Valida Clases":
    pagina_valida()    
elif page == "Manual de Usuario":
    pagina_ayuda()
