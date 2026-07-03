"""Provider-layer error types."""


class ProviderError(RuntimeError):
    """Base provider failure that should degrade, not crash workflows."""


class ProviderDisabled(ProviderError):
    """Raised when a provider requires unavailable configuration."""


class ProviderParseError(ProviderError):
    """Raised when source access succeeds but parsing cannot support claims."""
