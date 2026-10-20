from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from utils.thirds_client import ThirdsError, check_api_key


class ThirdsProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # Lists the newest PDF job. This reads account history and uses no credits.
        try:
            check_api_key(credentials.get("api_key", ""))
        except ThirdsError as e:
            raise ToolProviderCredentialValidationError(str(e)) from None
