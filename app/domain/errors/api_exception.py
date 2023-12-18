class ApiException(Exception):
    """
    API exceptions class to handle api exceptions in the application.
    """

    def __init__(self, response_code: int, key: str, message: str):
        self.response_code = response_code
        self.key = key
        self.message = message

    def get_response_code(self):
        """
        Get response code

        Returns:
            int: Response code
        """
        return self.response_code

    def get_message(self):
        """
        Get message

        Returns:
            str: Message
        """
        return self.message

    def get_key(self):
        """
        Get key

        Returns:
            str: Key
        """
        return self.key
