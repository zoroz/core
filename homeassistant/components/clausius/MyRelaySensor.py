"""Platform for binary sensor integration."""
from homeassistant.components.binary_sensor import BinarySensorEntity


class MyRelaySensor(BinarySensorEntity):
    """Representation of a Sensor."""

    def __init__(self, name, isOn) -> None:
        """Initialize the sensor.

        Args:
            name (str): The name of the sensor.
            isOn (bool): The initial state of the sensor.

        """
        self._name = name
        self._isOn = isOn

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def isOn(self):
        """Return the state of the sensor."""
        return self._isOn

    @property
    def is_on(self):
        """Returns the current state of the relay sensor.

        Returns:
            bool: True if the relay sensor is on, False otherwise.
        """
        return self._isOn
