"""Platform for sensor integration."""
from homeassistant.components.sensor import SensorEntity


class MyTemperatureSensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, name, state) -> None:
        """Initialize the sensor.

        Args:
            name (str): The name of the sensor.
            state (str): The initial state of the sensor.

        """
        self._name = name
        self._state = state

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "°C"  # or '°F' depending on your preference

    @property
    def device_class(self):
        """Return the class of this device, from component DEVICE_CLASSES."""
        return "temperature"
