def convertir_kalvin_celsius(k):
    '''Función que convierte la temperatura Kalvin a Celsius'''
    return k - 273.15
def convertir_kalvin_celsius(k):
    '''Función que convierte la temperatura Kalvin a Celsius'''
    return k - 273.15
def convertir_kalvin_celsius(k):
    '''Función que convierte la temperatura Kalvin a Celsius'''
    return k - 273.15
def filtrar_region(data, lat_min, lat_max, lon_min, lon_max, **kwargs):
    '''Filtra un dataset por rango de latitud y longitud.
    Maneja el caso en que la región cruza el meridiano 0 (lon_min > lon_max).
    Parámetros:
    lat_min, lat_max: rango de latitud
    lon_min, lon_max: rango de longitud (0-360)'''
    #Codigo que asegura que los datos ingresados esten dentro del dominio correcto
    condicion_lat = (data.latitude >= lat_min) & (data.latitude <= lat_max)
    #Si lon_min > lon_max, la región cruza el meridiano 0, como Europa y África -> usar OR (|)
    if lon_min > lon_max:
        condicion_lon = (data.longitude >= lon_min) | (data.longitude <= lon_max)
    else:
        #Sudamerica no cruza el meridiano, por lo tanto se agrega la condicion de que la longitud este entre lon_min y lon_max
        condicion_lon = (data.longitude >= lon_min) & (data.longitude <= lon_max)
    return data.where(condicion_lat & condicion_lon, drop=True)
def resumen_estadistico(df, *columnas):
    '''Recibe cualquier cantidad de nombres de columnas y devuelve su resumen.'''
    return df[list(columnas)].describe()
convertir_m_mm = lambda x: x * 1000