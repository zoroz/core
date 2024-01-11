"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Clausius climate platform.

    This function is called by Home Assistant when setting up the Clausius climate platform.
    It initializes the platform and adds the entities to Home Assistant.

    Args:
        hass (HomeAssistant): The Home Assistant instance.
        config (ConfigType): The configuration for the platform.
        add_entities (AddEntitiesCallback): The callback function to add entities to Home Assistant.
        discovery_info (DiscoveryInfoType | None, optional): The discovery information. Defaults to None.
    """
    api = hass.data[DOMAIN]
    add_entities(api.get_circuits())
