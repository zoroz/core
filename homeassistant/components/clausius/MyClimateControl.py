"""Platform for climate integration."""
import logging
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature


class MyClimateControl(ClimateEntity):
    """Representation of a Sensor."""

    _attr_hvac_modes = [HVACMode.HEAT]
    _attr_hvac_mode = HVACMode.HEAT
    _attr_max_temp = 35
    _attr_min_temp = 5
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_target_temperature_step = 1
    _attr_temperature_unit = UnitOfTemperature.CELSIUS

    def __init__(self, code, temperature, api) -> None:
        """Initialize the climate control."""
        self._api = api
        self._name = code
        self._attr_current_temperature = temperature
        self._attr_unique_id = "clausius_" + code
        self._target_temperature = temperature
        # self._target_temperature_high = temperature
        # self._target_temperature_low = temperature
        self._current_temperature = temperature

    @property
    def name(self) -> str:
        """Return name."""
        return self._name

    @property
    def current_temperature(self) -> float:
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self) -> float:
        """Return the temperature we try to reach."""
        return self._target_temperature

    # @property
    # def target_temperature_high(self) -> float | None:
    #     """Return the highbound target temperature we try to reach."""
    #     return self._target_temperature_high

    # @property
    # def target_temperature_low(self) -> float | None:
    #     """Return the lowbound target temperature we try to reach."""
    #     return self._target_temperature_low

    async def async_update(self) -> None:
        """Fetch new state data for this entity.

        This is the only method that should fetch new data for Home Assistant.
        """
        logging.info("Fetching new state data for %s", self.name)
        await self._api.async_set_temperature(self._name, self._target_temperature)
        # Here you would add the code to fetch the current state of your device
        # For example:
        # self._temperature = await self._device.get_temperature()
        # self._hvac_mode = await self._device.get_hvac_mode()

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        logging.info("Setting temperature for %s to %s", self._name, temperature)
        self._attr_current_temperature = temperature
        self.schedule_update_ha_state()
        self.async_write_ha_state()
        # Here you would add the code to send the new temperature to your device

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set new target HVAC mode."""
        logging.info("Setting HVAC mode to %s", hvac_mode)
        self._attr_hvac_mode = hvac_mode
        self.schedule_update_ha_state()
        self.async_write_ha_state()
        # Here you would add the code to send the new HVAC mode to your device
