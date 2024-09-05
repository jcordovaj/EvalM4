# EvalM4
Evaluación Final Módulo 4 Bootcamp Full Stack Python

## Diagrama de Clases

%%mermaid
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

## Otra alternativa

@startuml
class Vehiculo {
  -v_marca: String
  -v_modelo: String
  -v_nro_de_ruedas: int
}

class Automovil {
  -v_velocidad: int
  -v_cilindrada: int
}

class Particular {
  -v_puestos: int
}

class Carga {
  -v_carga_kgs: int
}

class Bicicleta {
  -tipo_de_bicicleta: String
}

class Motocicleta {
  -v_motor: String
  -v_cuadro: String
  -v_nro_radios: int
}

Vehiculo <|-- Automovil
Vehiculo <|-- Bicicleta
Automovil <|-- Particular
Automovil <|-- Carga
Bicicleta <|-- Motocicleta
@enduml

## Alternativa 3 TXT

Vehiculo
+-----------------------------+
| - v_marca: String            |
| - v_modelo: String           |
| - v_nro_de_ruedas: int       |
+-----------------------------+

Automovil (hereda de Vehiculo)
+-----------------------------+
| - v_velocidad: int           |
| - v_cilindrada: int          |
+-----------------------------+

Particular (hereda de Automovil)
+-----------------------------+
| - v_puestos: int             |
+-----------------------------+

Carga (hereda de Automovil)
+-----------------------------+
| - v_carga_kgs: int           |
+-----------------------------+

Bicicleta (hereda de Vehiculo)
+-----------------------------+
| - tipo_de_bicicleta: String  |
+-----------------------------+

Motocicleta (hereda de Bicicleta)
+-----------------------------+
| - v_motor: String            |
| - v_cuadro: String           |
| - v_nro_radios: int          |
+-----------------------------+

## Otra prueba


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```  
