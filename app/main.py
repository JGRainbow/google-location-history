import os
from utils import load_location_data_as_dataframe, create_geodataframe, clean_geodataframe, save_geodataframe_as_geojson

def main():
    DATA_DIR = '../data'
    DATA_PATH = os.path.join(DATA_DIR, 'Location History.json')

    df = load_location_data_as_dataframe(DATA_PATH)
    gdf = create_geodataframe(df)
    _gdf = clean_geodataframe(gdf)
    out_path = os.path.join(DATA_DIR, 'location_history.geojson')
    save_geodataframe_as_geojson(_gdf, out_path)

if __name__ == '__main__':
    main()