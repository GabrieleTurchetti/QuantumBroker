from .backends import *


class VirtualProvider:
    
    def __init__(self, tokens: dict[str, str | bool]) -> None:
        """Initialize a virtual provider."""
        self._tokens = tokens
        self._providers : dict[str, Provider] = {}
        
        for provider_name, token in tokens.items():
            try:
                if token:
                    provider = globals()[provider_name]
                    if issubclass(provider, Provider):
                        provider = provider(token)
                    self.register_provider(provider)
            except KeyError:
                raise ValueError(f"Unknown provider: {provider_name}")
        
    def register_provider(self, provider: Provider) -> None:
        """Register a provider."""
        provider_name = provider.__class__.__name__.lower()
        self._providers[provider_name] = provider
        
    def available_providers(self) -> list[Provider]:
        """Return a list of available providers."""
        return [*self._providers.values()]
        
    def available_backends(self) -> list[Backend]:
        """Return a list of available backends."""
        backends = []
        for provider in self._providers.values():
            backends += provider.available_backends()
        return backends
    
    def get_provider(self, name: str) -> Provider:
        """Return a provider."""
        return self._providers[name.lower()]
    
    def get_backend(self, provider: str, name: str) -> Backend:
        """Return a backend."""
        return self._providers[provider.lower()].get_backend(name)
    
    def __str__(self) -> str:
        """Return a string representation of the provider."""
        return f"VirtualProvider(providers={self._providers})"
    
    def __repr__(self) -> str:
        """Return a string representation of the provider."""
        return self.__str__()
        
