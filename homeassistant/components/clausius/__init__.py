"""Clausius Load Platform integration."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .clausiusApi import clausiusApi

DOMAIN = "clausius"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional("base_url", default="http://192.168.10.2"): cv.url,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Clausius component.

    This function initializes the Clausius component by creating an instance of the Clausius API,
    storing it in the Home Assistant data dictionary, and loading the climate, sensor, and binary_sensor platforms.

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        config (ConfigType): The configuration for the Clausius component.

    Returns:
        bool: True if the setup was successful, False otherwise.
    """
    clausius_config = config[DOMAIN]
    base_url = clausius_config.get("base_url")
    api = clausiusApi(base_url)
    await api.async_init()
    hass.data[DOMAIN] = api
    await hass.helpers.discovery.async_load_platform("climate", DOMAIN, {}, config)
    await hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    await hass.helpers.discovery.async_load_platform(
        "binary_sensor", DOMAIN, {}, config
    )

    return True
