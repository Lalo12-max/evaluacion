# Rent4you Datawarehouse - Proyecto de Evaluación

## Descripción
Este repositorio contiene los datos preprocesados y análisis para el datawarehouse de la empresa de alquiler de vehículos Rent4you.

## Estructura del Proyecto
rent4you-datawarehouse/
├── data/
│   ├── raw/                    # Datos originales
│   └── processed/              # Datos preprocesados
│       ├── dim_tiempo.csv      # Dimensión temporal
│       ├── dim_sucursal.csv    # Dimensión sucursales
│       ├── dim_vehiculo.csv    # Dimensión vehículos
│       ├── dim_cliente.csv     # Dimensión clientes
│       ├── dim_empleado.csv    # Dimensión empleados
│       ├── fact_alquileres.csv # Hechos de alquileres
│       └── fact_gastos.csv     # Hechos de gastos
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_ventas_por_sucursal.ipynb
│   └── 03_analisis_rentabilidad.ipynb
├── scripts/
│   └── data_generator.py       # Script generador de datos
└── README.md


## Datasets Incluidos

### Dimensiones
- **dim_tiempo.csv**: 1,095 registros (3 años de datos diarios)
- **dim_sucursal.csv**: 8 sucursales en diferentes ciudades
- **dim_vehiculo.csv**: 270 vehículos de diferentes tipos
- **dim_cliente.csv**: 1,000 clientes
- **dim_empleado.csv**: 100 empleados

### Tablas de Hechos
- **fact_alquileres.csv**: 10,000 registros de alquileres
- **fact_gastos.csv**: 5,000 registros de gastos

## Análisis Disponibles
1. Análisis de ventas por sucursal
2. Análisis de rentabilidad
3. Segmentación de clientes
4. Eficiencia de empleados

## Requisitos
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter
- plotly

## Instalación
```bash
pip install pandas numpy matplotlib seaborn jupyter plotly