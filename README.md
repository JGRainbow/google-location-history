# Google Location History

`google-location-history` is a Python library for loading and saving Google Locations stored from a mobile device.

## Installation

Clone this repository

```bash
git clone git@github.com:JGRainbow/google-location-history.git
```

## Usage
* Download Location History as a `JSON` file from [Google Takeout](https://takeout.google.com/settings/takeout?pli=1)
* Run the main file to convert this into a `GeoJSON` file

```bash
python -m app/main.py
```
* View/Analyse the `GeoJSON` in any GIS software you choose, for example [QGIS](https://download.qgis.org)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)