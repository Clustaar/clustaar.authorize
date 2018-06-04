class Ability(object):
    """
    Ability role is to allow or deny access to actions to user.
    It's composed of an Authorizations object that defines the permissions.
    """

    def __init__(self, authorizations):
        """
        Args:
            authorizations (Authorizations): an Authorizations object
        """
        self._authorizations = authorizations

    def authorize(self, action, *args, **kwargs):
        """
        If no permission allows action to be executed
        an exception generated by `authorizations` is raised.
        If allowed it does nothing.

        Args:
            action (Action): action to validate access
            kwargs (dict): arguments passed to the access method associated to `action`
        Returns:
            None
        """
        if not self.can(action, *args, **kwargs):
            raise self._authorizations.generate_error(action, kwargs)

    def can(self, action, *args, **kwargs):
        """ Returns if current ability allows action to be executed

        Args:
            action (Action): action to validate access

        Returns:
            bool: True if allowed, false otherwise
        """
        return self._authorizations.can(action, *args, **kwargs)
