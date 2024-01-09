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
    """Set up the Clausius binary sensor platform.

    This function is called by Home Assistant when setting up the Clausius binary sensor platform.
    It retrieves the Clausius API instance from the Home Assistant data and adds the binary sensor entities
    to the Home Assistant using the provided `add_entities` callback.

    :param hass: The Home Assistant instance.
    :param config: The configuration for the Clausius binary sensor platform.
    :param add_entities: The callback function to add entities to Home Assistant.
    :param discovery_info: Optional discovery information.
    """
    api = hass.data[DOMAIN]
    add_entities(await api.get_relays())
