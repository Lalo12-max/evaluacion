import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurar semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

def generar_dim_tiempo():
    """Genera la dimensión tiempo"""
    fechas = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')
    
    dim_tiempo = pd.DataFrame({
        'fecha_id': range(1, len(fechas) + 1),
        'fecha': fechas,
        'año': fechas.year,
        'mes': fechas.month,
        'trimestre': fechas.quarter,
        'dia_semana': fechas.dayofweek + 1,
        'es_fin_semana': (fechas.dayofweek >= 5).astype(int),
        'temporada': ['Alta' if mes in [6,7,8,12] else 'Baja' for mes in fechas.month]
    })
    
    return dim_tiempo

def generar_dim_sucursal():
    """Genera la dimensión sucursal"""
    sucursales = [
        {'nombre': 'Rent4you Madrid Centro', 'ciudad': 'Madrid', 'region': 'Centro', 'tipo': 'Urbana'},
        {'nombre': 'Rent4you Barcelona Port', 'ciudad': 'Barcelona', 'region': 'Cataluña', 'tipo': 'Puerto'},
        {'nombre': 'Rent4you Valencia Aeropuerto', 'ciudad': 'Valencia', 'region': 'Levante', 'tipo': 'Aeropuerto'},
        {'nombre': 'Rent4you Sevilla Centro', 'ciudad': 'Sevilla', 'region': 'Andalucía', 'tipo': 'Urbana'},
        {'nombre': 'Rent4you Bilbao Industrial', 'ciudad': 'Bilbao', 'region': 'País Vasco', 'tipo': 'Industrial'},
        {'nombre': 'Rent4you Málaga Costa', 'ciudad': 'Málaga', 'region': 'Andalucía', 'tipo': 'Turística'},
        {'nombre': 'Rent4you Zaragoza Centro', 'ciudad': 'Zaragoza', 'region': 'Aragón', 'tipo': 'Urbana'},
        {'nombre': 'Rent4you Palma Aeropuerto', 'ciudad': 'Palma', 'region': 'Baleares', 'tipo': 'Aeropuerto'}
    ]
    
    dim_sucursal = pd.DataFrame({
        'sucursal_id': range(1, len(sucursales) + 1),
        'nombre_sucursal': [s['nombre'] for s in sucursales],
        'ciudad': [s['ciudad'] for s in sucursales],
        'region': [s['region'] for s in sucursales],
        'tipo_sucursal': [s['tipo'] for s in sucursales],
        'fecha_apertura': pd.to_datetime(['2020-01-15', '2019-03-20', '2021-06-10', 
                                        '2018-11-05', '2022-02-28', '2020-07-12',
                                        '2021-09-18', '2019-12-03'])
    })
    
    return dim_sucursal

def generar_dim_vehiculo():
    """Genera la dimensión vehículo"""
    tipos = ['Coche', 'Moto', 'Camioneta', 'Remolque']
    marcas_coches = ['Toyota', 'Volkswagen', 'Ford', 'Renault', 'Seat']
    marcas_motos = ['Yamaha', 'Honda', 'Kawasaki', 'BMW']
    marcas_camionetas = ['Ford Transit', 'Mercedes Sprinter', 'Iveco Daily']
    marcas_remolques = ['Humbaur', 'Böckmann', 'Brenderup']
    
    vehiculos = []
    vehiculo_id = 1
    
    # Generar coches
    for _ in range(150):
        vehiculos.append({
            'vehiculo_id': vehiculo_id,
            'tipo_vehiculo': 'Coche',
            'marca': random.choice(marcas_coches),
            'modelo': f'Modelo {random.randint(1, 20)}',
            'año': random.randint(2018, 2024),
            'categoria_precio': random.choice(['Económico', 'Medio', 'Premium']),
            'estado': random.choice(['Excelente', 'Bueno', 'Regular'])
        })
        vehiculo_id += 1
    
    # Generar motos
    for _ in range(50):
        vehiculos.append({
            'vehiculo_id': vehiculo_id,
            'tipo_vehiculo': 'Moto',
            'marca': random.choice(marcas_motos),
            'modelo': f'Modelo {random.randint(1, 15)}',
            'año': random.randint(2019, 2024),
            'categoria_precio': random.choice(['Económico', 'Medio', 'Premium']),
            'estado': random.choice(['Excelente', 'Bueno', 'Regular'])
        })
        vehiculo_id += 1
    
    # Generar camionetas
    for _ in range(40):
        vehiculos.append({
            'vehiculo_id': vehiculo_id,
            'tipo_vehiculo': 'Camioneta',
            'marca': random.choice(marcas_camionetas),
            'modelo': f'Modelo {random.randint(1, 10)}',
            'año': random.randint(2018, 2024),
            'categoria_precio': random.choice(['Medio', 'Premium']),
            'estado': random.choice(['Excelente', 'Bueno', 'Regular'])
        })
        vehiculo_id += 1
    
    # Generar remolques
    for _ in range(30):
        vehiculos.append({
            'vehiculo_id': vehiculo_id,
            'tipo_vehiculo': 'Remolque',
            'marca': random.choice(marcas_remolques),
            'modelo': f'Modelo {random.randint(1, 8)}',
            'año': random.randint(2018, 2024),
            'categoria_precio': random.choice(['Económico', 'Medio']),
            'estado': random.choice(['Excelente', 'Bueno', 'Regular'])
        })
        vehiculo_id += 1
    
    return pd.DataFrame(vehiculos)

def generar_dim_cliente():
    """Genera la dimensión cliente"""
    clientes = []
    
    for i in range(1, 1001):
        clientes.append({
            'cliente_id': i,
            'edad': random.randint(18, 75),
            'genero': random.choice(['M', 'F']),
            'tipo_cliente': random.choice(['Particular', 'Empresa']),
            'ciudad_residencia': random.choice(['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Málaga', 'Zaragoza', 'Palma']),
            'segmento_riesgo': random.choice(['Bajo', 'Medio', 'Alto'])
        })
    
    return pd.DataFrame(clientes)

def generar_dim_empleado():
    """Genera la dimensión empleado"""
    empleados = []
    cargos = ['Vendedor', 'Supervisor', 'Gerente', 'Técnico']
    
    for i in range(1, 101):
        empleados.append({
            'empleado_id': i,
            'nombre': f'Empleado {i}',
            'cargo': random.choice(cargos),
            'sucursal_id': random.randint(1, 8),
            'fecha_contratacion': pd.to_datetime('2018-01-01') + timedelta(days=random.randint(0, 2190)),
            'experiencia_años': random.randint(1, 15)
        })
    
    return pd.DataFrame(empleados)

def generar_fact_alquileres():
    """Genera la tabla de hechos de alquileres"""
    alquileres = []
    
    for i in range(1, 10001):
        tipo_vehiculo = random.choice(['Coche', 'Moto', 'Camioneta', 'Remolque'])
        categoria = random.choice(['Económico', 'Medio', 'Premium'])
        
        # Precios base por tipo y categoría
        precios_base = {
            'Coche': {'Económico': 25, 'Medio': 45, 'Premium': 80},
            'Moto': {'Económico': 15, 'Medio': 25, 'Premium': 40},
            'Camioneta': {'Económico': 60, 'Medio': 90, 'Premium': 120},
            'Remolque': {'Económico': 20, 'Medio': 35, 'Premium': 50}
        }
        
        dias_alquiler = random.randint(1, 14)
        precio_base = precios_base[tipo_vehiculo][categoria]
        precio_total = precio_base * dias_alquiler * random.uniform(0.8, 1.2)
        
        alquileres.append({
            'alquiler_id': i,
            'fecha_id': random.randint(1, 1095),  # 3 años de datos
            'sucursal_id': random.randint(1, 8),
            'vehiculo_id': random.randint(1, 270),
            'cliente_id': random.randint(1, 1000),
            'empleado_id': random.randint(1, 100),
            'dias_alquiler': dias_alquiler,
            'precio_total': round(precio_total, 2),
            'descuento': round(precio_total * random.uniform(0, 0.15), 2),
            'seguro_contratado': random.choice([0, 1])
        })
    
    return pd.DataFrame(alquileres)

def generar_fact_gastos():
    """Genera la tabla de hechos de gastos"""
    gastos = []
    tipos_gasto = ['Mantenimiento', 'Personal', 'Marketing', 'Alquiler Local', 'Combustible', 'Seguros']
    
    for i in range(1, 5001):
        tipo_gasto = random.choice(tipos_gasto)
        
        # Rangos de montos por tipo de gasto
        rangos_monto = {
            'Mantenimiento': (50, 500),
            'Personal': (1500, 3000),
            'Marketing': (200, 2000),
            'Alquiler Local': (800, 2500),
            'Combustible': (100, 800),
            'Seguros': (300, 1200)
        }
        
        monto = random.uniform(*rangos_monto[tipo_gasto])
        
        gastos.append({
            'gasto_id': i,
            'fecha_id': random.randint(1, 1095),
            'sucursal_id': random.randint(1, 8),
            'tipo_gasto': tipo_gasto,
            'monto': round(monto, 2),
            'descripcion': f'{tipo_gasto} - Sucursal {random.randint(1, 8)}'
        })
    
    return pd.DataFrame(gastos)

def main():
    """Función principal para generar todos los datasets"""
    print("Generando datasets para Rent4you Datawarehouse...")
    
    # Generar dimensiones
    print("Generando dimensiones...")
    dim_tiempo = generar_dim_tiempo()
    dim_sucursal = generar_dim_sucursal()
    dim_vehiculo = generar_dim_vehiculo()
    dim_cliente = generar_dim_cliente()
    dim_empleado = generar_dim_empleado()
    
    # Generar hechos
    print("Generando tablas de hechos...")
    fact_alquileres = generar_fact_alquileres()
    fact_gastos = generar_fact_gastos()
    
    # Guardar archivos CSV
    print("Guardando archivos CSV...")
    dim_tiempo.to_csv('../data/processed/dim_tiempo.csv', index=False)
    dim_sucursal.to_csv('../data/processed/dim_sucursal.csv', index=False)
    dim_vehiculo.to_csv('../data/processed/dim_vehiculo.csv', index=False)
    dim_cliente.to_csv('../data/processed/dim_cliente.csv', index=False)
    dim_empleado.to_csv('../data/processed/dim_empleado.csv', index=False)
    fact_alquileres.to_csv('../data/processed/fact_alquileres.csv', index=False)
    fact_gastos.to_csv('../data/processed/fact_gastos.csv', index=False)
    
    print("¡Datasets generados exitosamente!")
    print(f"Dimensión Tiempo: {len(dim_tiempo)} registros")
    print(f"Dimensión Sucursal: {len(dim_sucursal)} registros")
    print(f"Dimensión Vehículo: {len(dim_vehiculo)} registros")
    print(f"Dimensión Cliente: {len(dim_cliente)} registros")
    print(f"Dimensión Empleado: {len(dim_empleado)} registros")
    print(f"Hechos Alquileres: {len(fact_alquileres)} registros")
    print(f"Hechos Gastos: {len(fact_gastos)} registros")

if __name__ == "__main__":
    main()