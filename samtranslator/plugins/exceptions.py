class InvalidPluginException(Exception):
    """Exception raised when the provided plugin configuration is not valid.

    Attributes:
        plugin_name -- name of the plugin that caused this error
        message -- explanation of the error
    """

    def __init__(self, plugin_name, message):  # type: ignore[no-untyped-def]
        self._plugin_name = plugin_name
        self._message = message

    @property
    def message(self):  # type: ignore[no-untyped-def]
        return "The {} plugin is invalid. {}".format(self._plugin_name, self._message)
