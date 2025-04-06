"""
This module defines the client for interacting with the Termii API.

Classes:
    TermiiClient: A client for sending requests to the Termii API.

Usage example:
    client = Termii(api_key='your_api_key')
"""

class Termii:
    """
    A client for interacting with the Termii API.
    This class provides methods to send requests to the Termii API using the provided API key.

    Attributes:
        api_key (str): The API key for authenticating with the Termii API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the Termii client with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Termii API.
        """
        self.api_key = api_key