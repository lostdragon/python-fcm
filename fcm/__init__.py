from .fcm import OAuthFCM, FCM, TopicManager  # pylint: disable=unused-import

# -----------------------------------------------------------------------------

# Set default logging handler to avoid "No handler found" warnings.
import logging

assert FCM

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

del NullHandler

# -----------------------------------------------------------------------------
