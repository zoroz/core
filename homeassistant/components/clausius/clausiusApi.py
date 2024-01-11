"""Module provides the Clausius API client."""
from __future__ import annotations

import logging

import aiohttp

from .MyClimateControl import MyClimateControl
from .MyRelaySensor import MyRelaySensor
from .MyTemperatureSensor import MyTemperatureSensor


class clausiusApi:
    """A class for interacting with the Clausius API."""

    _attr_json_data: dict
    _attr_sensors: list[MyTemperatureSensor]
    _attr_relays: list[MyRelaySensor]
    _attr_circuits: list[MyClimateControl]

    def __init__(self, base_url) -> None:
        """Initialize the Clausius API client.

        Args:
            base_url (str): The base URL of the Clausius API.
        """
        self.base_url = base_url

    async def async_init(self) -> None:
        """Initialize the Clausius API client.

        Args:
            base_url (str): The base URL of the Clausius API.

        Raises:
            requests.exceptions.HTTPError: If there is an HTTP error while retrieving data from the API.
        """

        logging.info("Initializing Clausius API client with base URL %s", self.base_url)
        try:
            async with aiohttp.ClientSession() as session, session.get(
                f"{self.base_url}/gwd/clausius/sensors"
            ) as response:
                response.raise_for_status()
                self._attr_json_data = await response.json()
        except aiohttp.ClientError as e:
            logging.error("Failed to get data from API: %s", e)
            self._attr_json_data = {}
            self._attr_sensors = []
            self._attr_relays = []
            self._attr_circuits = []
        else:
            self._attr_sensors = [
                MyTemperatureSensor(sensor["name"] or sensor["id"], sensor["value"])
                for sensor in self._attr_json_data["sensors"]
            ]
            self._attr_relays = [
                MyRelaySensor(sensor["name"] or sensor["code"], sensor["isOn"])
                for sensor in self._attr_json_data["relays"]
            ]
            self._attr_circuits = [
                MyClimateControl(sensor["code"], 20, self)
                for sensor in self._attr_json_data["circuits"]
            ]

    def get_sensors(self) -> list[MyTemperatureSensor]:
        """Get the list of temperature sensors.

        Returns:
            A list of MyTemperatureSensor objects representing the temperature sensors.
        """
        return self._attr_sensors

    def get_relays(self) -> list[MyRelaySensor]:
        """Get the list of relay sensors.

        Returns:
            A list of MyRelaySensor objects representing the relay sensors.
        """
        return self._attr_relays

    def get_circuits(self) -> list[MyClimateControl]:
        """Get the list of circuits associated with the Clausius API.

        Returns:
            A list of MyClimateControl objects representing the circuits.
        """
        return self._attr_circuits

    async def async_set_temperature(self, entityId: str, temperature: float) -> None:
        """Set the temperature for a circuit.

        Args:
            entityId (str): The id of the circuit.
            temperature (float): The temperature to set.
        """
        try:
            async with aiohttp.ClientSession() as session, session.get(
                f"{self.base_url}/gwd/clausius/{entityId}/temperature?temperature={temperature}"
            ) as response:
                response.raise_for_status()
        except aiohttp.ClientError as e:
            logging.error("Failed to get data from API: %s", e)
