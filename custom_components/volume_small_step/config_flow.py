"""Config flow for Volume Small Step — enables UI setup without configuration.yaml."""

from __future__ import annotations

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.core import HomeAssistant

from . import DOMAIN


class VolumeSmallStepConfigFlow(ConfigFlow, domain=DOMAIN):
    """One-shot config flow: no options, just create the entry."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict | None = None
    ) -> ConfigFlowResult:
        # Prevent creating a second entry
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        # No form needed — create the entry immediately
        return self.async_create_entry(title="Volume Small Step", data={})