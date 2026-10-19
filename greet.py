def greet(name):
    """Return a greeting string for the given name.

    Returns 'Hello, world!' when *name* is empty or None.
    """
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"
