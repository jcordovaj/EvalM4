# EvalM4
Evaluación Final Módulo 4 Bootcamp Full Stack Python

## Diagrama de Clases

classDiagram
    Vehiculo <|-- Automovil
    Vehiculo <|-- Bicicleta
    Automovil <|-- Particular
    Automovil <|-- Carga
    Bicicleta <|-- Motocicleta

    class Vehiculo{
      String v_marca
      String v_modelo
      int v_nro_de_ruedas
    }

    class Automovil{
      int v_velocidad
      int v_cilindrada
    }

    class Particular{
      int v_puestos
    }

    class Carga{
      int v_carga_kgs
    }

    class Bicicleta{
      String tipo_de_bicicleta
    }

    class Motocicleta{
      String v_motor
      String v_cuadro
      int v_nro_radios
    }
