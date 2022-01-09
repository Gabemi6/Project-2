import pandas as pd
#Leer archivo CSV y convertirlo en dataframe de pandas
Data_Frame = pd.read_csv (r'synergy_logistics_database.csv')
#Agrupar datos por origen y destino, hacer sumatoria de los valores totales
Data_Frame = Data_Frame.groupby(['origin', 'destination'], as_index=False)['total_value'].sum()
#Ordenar de forma descendente
Data_Frame=Data_Frame.sort_values('total_value', ascending=False)
#Imprimir primeros 10
print("\nCountries ordered by total value:\n")
print (Data_Frame.head(10))

#Leer archivo CSV y convertirlo en dataframe de pandas
df2=pd.read_csv (r'synergy_logistics_database.csv')
#Agrupar datos por metodo de transporte, hacer sumatoria de los valores totales
df2= df2.groupby(['transport_mode'], as_index=False)['total_value'].sum()
#Ordenar de forma descendente
df2=df2.sort_values('total_value',ascending=False)
#Imprimir dataframe
print("\nTransportation mode ordered by total value:\n")
print(df2)

#Agrupar datos por origen y destino, hacer sumatoria de los valores totales
df3=pd.read_csv (r'synergy_logistics_database.csv')
#Crear mascara del dataframework para filtrar datos de exportacion e importacion
maskExports=df_mask=df3['direction']=='Exports'
maskImports=df_mask=df3['direction']=='Imports'
#Aplicar mascara para realizar el filtrado
filtered_df_Exports = df3[maskExports]
filtered_df_Imports = df3[maskImports]
#Agrupar datos con respecto al origen y hacer sumatoria de valor total de importaciones y exportacionens
tv_country_Exports=filtered_df_Exports.groupby(['origin'],as_index=False)['total_value'].sum()
tv_country_Imports=filtered_df_Imports.groupby(['origin'],as_index=False)['total_value'].sum()
#Sumar total de exportaciones e importaciones para calcular el porcentaje
tv_percentage_Exports=tv_country_Exports['total_value'].sum()
tv_percentage_Imports=tv_country_Imports['total_value'].sum()
#Calcular porcentaje de cada elemento tanto de importaciones como de exportaciones
tv_country_Exports['Percentage']=100*tv_country_Exports['total_value']/tv_percentage_Exports
tv_country_Imports['Percentage']=100*tv_country_Imports['total_value']/tv_percentage_Imports
#Ordenar DF por porcentaje de forma descendente
tv_country_Exports.sort_values(by='Percentage', ascending=False, inplace=True)
tv_country_Imports.sort_values(by='Percentage', ascending=False, inplace=True)
#Realizar la suma del acumulado de importaciones y exportaciones
tv_country_Exports['Total percentage']=tv_country_Exports['Percentage'].cumsum()
tv_country_Imports['Total percentage']=tv_country_Imports['Percentage'].cumsum()
#Obtener los elementos que juntos no superen el 85%
top_80_Exports= tv_country_Exports[tv_country_Exports['Total percentage']<85]
top_80_Imports= tv_country_Imports[tv_country_Imports['Total percentage']<85]
#Imprimir exportaciones e importaciones
print("\n85% de Exportaciones:\n")
print(top_80_Exports)
print("\n85% de Importaciones:\n")
print(top_80_Imports)



"""import pandas as pd

Data_Frame = pd.read_csv (r'synergy_logistics_database.csv')
Data_Frame = Data_Frame.groupby(['origin', 'destination'], as_index=False)['total_value'].sum()
Data_Frame=Data_Frame.sort_values('total_value', ascending=False)
print (Data_Frame.head(10))

df2=pd.read_csv (r'synergy_logistics_database.csv')
df2= df2.groupby(['transport_mode'], as_index=False)['total_value'].sum()
df2=df2.sort_values('total_value',ascending=False)
print (df2.head(5))

df3=pd.read_csv (r'synergy_logistics_database.csv')
tv_country=df3.groupby(['origin'],as_index=False)['total_value'].sum()
tv_percentage=tv_country['total_value'].sum()
tv_country['percent']=100*tv_country['total_value']/tv_percentage
tv_country.sort_values(by='percent', ascending=False, inplace=True)
tv_country['cumsum']=tv_country['percent'].cumsum()
top_80= tv_country[tv_country['cumsum']<85]

print(top_80)"""


