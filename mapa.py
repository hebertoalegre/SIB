import os
import json
import geopandas as gpd
from unidecode import unidecode
from shapely.geometry import Polygon


###############################################################################################

#                                           FUNCIONES                                         #  

###############################################################################################
def decode_arcs(arcs, arc_indices, transform=None):
    """
    Decodifica los arcos de TopoJSON a coordenadas.
    """
    coordinates = []
    for arc_index in arc_indices:
        reverse = arc_index < 0
        arc = arcs[~arc_index if reverse else arc_index]
        if reverse:
            arc = arc[::-1]  # Invertir si es un arco negativo
        if transform:
            arc = [
                [transform["scale"][0] * x + transform["translate"][0],
                 transform["scale"][1] * y + transform["translate"][1]]
                for x, y in arc
            ]
        coordinates.extend(arc)
    return coordinates



###############################################################################################

#                                             GEOJSON                                         #  

###############################################################################################


topo_path = os.path.abspath('deptos.json')  # Ruta al archivo
with open(topo_path, "r", encoding="utf-8") as file:
    topojson_data = json.load(file)


features = topojson_data["objects"]["departamentos_gtm"]["geometries"]
arcs = topojson_data["arcs"]
transform = topojson_data.get("transform")


geojson_features = []
for feature in features:
    # Decodificar los arcos
    coordinates = decode_arcs(arcs, feature["arcs"][0], transform)  # Solo funciona para polígonos simples
    geom = Polygon(coordinates)
    properties = feature.get("properties", {})
    geojson_features.append({"type": "Feature", "geometry": geom, "properties": properties})

gdf = gpd.GeoDataFrame.from_features(geojson_features)

gdf["centroide_lat"] = gdf.geometry.centroid.y
gdf["centroide_lon"] = gdf.geometry.centroid.x
gdf['Departamento'] = gdf['Departamento'].apply(lambda row: unidecode(row).upper())
gdf['KEY_EVOL'] = [6,12,17,16,18,15,22,21,20,24,23,19,25,26,8,7,27,9,11,10,14,13]
gdf.columns =  [ "GEOMETRY", "KEY_DEPTO", "DEPARTAMENTO","CENTROIDE_LAT", "CENTROIDE_LON", "KEY_EVOL"]


gdf.to_excel(os.path.join(os.path.abspath('outputs'), 'departamentos.xlsx'), index=False)
print(gdf)
