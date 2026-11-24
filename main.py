
from pyscript import document, display

weather_instruments = {
    "Thermometer": ("Air Temperature", "Degrees Celsius (°C)", "Measures how hot or cold the air is."),
    "Barometer": ("Atmospheric Pressure", "Hectopascals (hPa)", "Measures air pressure to help monitor weather changes."),
    "Anemometer": ("Wind Speed", "Kilometers per hour (km/h)", "Measures how fast the wind is blowing."),
    "Hygrometer": ("Relative Humidity", "Percent (%)", "Measures the amount of moisture in the air."),
    "Rain Gauge": ("Rainfall", "Millimeters (mm)", "Measures the amount of rainfall in an area."),
    "Wind Vane": ("Wind Direction", "Cardinal Directions", "Identifies the direction from which the wind is blowing."),
    "Weather Balloon": ("Atmospheric Conditions", "Varies", "Collects atmospheric data at different altitudes."),
    "Pyranometer": ("Solar Radiation", "Watts per square meter (W/m²)", "Measures incoming solar radiation.")
}


def check_element(e):
    document.getElementById("elements").innerHTML = ""

    instrument_name = document.getElementById("weather_instruments").value
    instrument_name_final = instrument_name.strip().title()

    result = weather_instruments.get(instrument_name_final, ("Instrument not included in the dataset", " - ", " - "))

    document.getElementById("elements").innerHTML = f"""
    <b>Weather Instrument:</b> {instrument_name_final}<br>
    <b>What It Measures:</b> {result[0]}<br>
    <b>Unit of Measurement:</b> {result[1]}<br>
    <b>Purpose:</b> {result[2]}
    """
