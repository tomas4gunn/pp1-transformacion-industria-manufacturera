"""
Descarga de datos por API — Proyecto PP1 Equipo 1
Transformación de la industria manufacturera en Argentina (2016 - 2026)

Fuente: API de Series de Tiempo de datos.gob.ar (datos oficiales del INDEC).
Documentación de la API: https://datosgobar.github.io/series-tiempo-ar-api/

Genera dos archivos CSV mensuales (enero 2016 en adelante):
  - ucii_indec_2016_2026.csv : Utilización de la Capacidad Instalada en la Industria (%), base 2004
  - (opcional) actualiza el IPI manufacturero si se agregan sus ids en SERIES_IPI

Uso:
  pip install pandas requests
  python obtener_datos_api.py
"""
import io

import pandas as pd
import requests

API = "https://apis.datos.gob.ar/series/api/series/"
DESDE = "2016-01-01"

# UCII mensual base 2004 (dataset 31.3 de INDEC). id de la serie -> nombre de columna
SERIES_UCII = {
    "31.3_UNG_2004_M_18": "ucii_nivel_general",
    "31.3_UPAB_2004_M_35": "ucii_productos_alimenticios_bebidas",
    "31.3_UPT_2004_M_21": "ucii_productos_tabaco",
    "31.3_UPT_2004_M_23": "ucii_productos_textiles",
    "31.3_UPC_2004_M_17": "ucii_papel_carton",
    "31.3_UEI_2004_M_22": "ucii_edicion_impresion",
    "31.3_URP_2004_M_24": "ucii_refinacion_petroleo",
    "31.3_USPQ_2004_M_34": "ucii_sustancias_productos_quimicos",
    "31.3_UCP_2004_M_20": "ucii_caucho_plastico",
    "31.3_UMNM_2004_M_27": "ucii_minerales_no_metalicos",
    "31.3_UIMB_2004_M_33": "ucii_industrias_metalicas_basicas",
    "31.3_UV_2004_M_25": "ucii_vehiculosautomotores",
    "31.3_UMNIA_2004_M_42": "ucii_metalmecanica_no_industria_automotriz",
}


def descargar(series: dict, desde: str = DESDE) -> pd.DataFrame:
    """Pide varias series en una sola llamada (la API acepta hasta 40 ids)."""
    params = {"ids": ",".join(series), "format": "csv", "start_date": desde, "limit": 1000}
    r = requests.get(API, params=params, timeout=60)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    df = df.rename(columns={"indice_tiempo": "fecha"})
    # la API devuelve los nombres "cortos" de cada serie, en el mismo orden pedido
    df.columns = ["fecha"] + list(series.values())
    return df


if __name__ == "__main__":
    ucii = descargar(SERIES_UCII)
    ucii.to_csv("ucii_indec_2016_2026.csv", index=False)
    print(f"UCII: {len(ucii)} meses ({ucii.fecha.iloc[0]} a {ucii.fecha.iloc[-1]}), {ucii.shape[1] - 1} series")
