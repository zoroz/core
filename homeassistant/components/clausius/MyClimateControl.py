"""Platform for climate integration."""
import logging
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature

_LOGGER = logging.getLogger(__name__)


class MyClimateControl(ClimateEntity):
    """Representation of a Sensor."""

    def __init__(self, code, temperature) -> None:
        """Initialize the climate control."""
        self._name = code
        self._temperature = temperature
        self.unique_id = "clausius_" + code
        self._attr_unique_id = self.unique_id
        self._attr_min_temp = 15
        self._attr_max_temp = 30

    @property
    def name(self) -> str:
        """Return the name of the climate control."""
        return self._name

    @property
    def temperature(self) -> float | None:
        """Return the current temperature."""
        return self._temperature

    @property
    def current_temperature(self) -> float | None:
        """Return the current temperature."""
        return self._temperature

    @property
    def temperature_unit(self) -> UnitOfTemperature:
        """Return the unit of measurement."""
        return UnitOfTemperature.CELSIUS

    @property
    def hvac_mode(self) -> HVACMode:
        """Return the current HVAC mode."""
        return HVACMode.HEAT

    @property
    def hvac_modes(self) -> list[HVACMode]:
        """Return the list of available HVAC modes."""
        return [HVACMode.HEAT]

    @property
    def supported_features(self) -> ClimateEntityFeature:
        """Return the list of supported features."""
        return ClimateEntityFeature.TARGET_TEMPERATURE

    def set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        _LOGGER.info("Setting temperature to %s", temperature)
        self._temperature = temperature
        self.schedule_update_ha_state()
        # Here you would add the code to send the new temperature to your device
