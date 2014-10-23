from conf import settings


if settings.backend == 'PySide':
    try:
        from PySide import (QtCore, QtGui, QtWebKit, QtNetwork)
    except ImportError:
        from PyQt4 import (QtCore, QtGui, QtWebKit, QtNetwork)
elif settings.backend == 'PyQt':
    try:
        from PyQt4 import (QtCore, QtGui, QtWebKit, QtNetwork)
    except ImportError:
        from PySide import (QtCore, QtGui, QtWebKit, QtNetwork)
else:
    import warnings
    from exceptions import ImproperlyConfiguredWarning
    warnings.warn((
        "Unknown backend '{}' is specified. "
        "Only the following backends are available. "
        "1) 'PySide', 2) 'PyQt'."
    ).format(settings.backend), ImproperlyConfiguredWarning)
    # Use PySide
    try:
        from PySide import (QtCore, QtGui, QtWebKit, QtNetwork)
    except ImportError:
        from PyQt4 import (QtCore, QtGui, QtWebKit, QtNetwork)
