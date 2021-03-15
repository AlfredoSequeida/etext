from etext.providers import PROVIDERS


class ProviderNotFoundException(Exception):
    def __init__(self, provider: str):
        self.provider = provider

    def __str__(self):
        return (
            f"{self.provider} not found. The valid provider options are\n"
            f"{', '.join(PROVIDERS.keys())}"
        )


class NoMMSSupportException(Exception):
    def __init__(self, provider: str):
        self.provider = provider

    def __str__(self):
        return f"{self.provider} does not support mms"


class NumberNotValidException(Exception):
    def __init__(self, number: str):
        self.number = number

    def __str__(self):
        return (
            f"{self.number} not valid. "
            "It must be a valid US phone number 10 digits in length."
        )
