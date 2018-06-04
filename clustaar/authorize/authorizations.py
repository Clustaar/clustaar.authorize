from .rules import Deny


class Authorizations(object):
    """
    Authorizations base class.
    Developper must inherit this class to create its own rules.

    Example:
        class AdminAuthorizations(Authorizations):
            def can_view_project(self, project_id):
                return True
    """
    def __init__(self, rules, default_rule=Deny()):
        """
        Args:
            rules (dict<Action, Rule>):
            default_rule (Rule): default action taken if access method is not defined
        """
        self.rules = rules
        self._default_rule = default_rule

    def generate_error(self, rule, kwargs):
        """ Build an error when access defined by rule is not granted
        Args:
            rule (Rule): an access rule
            kwargs (dict): args received when asking for authorization
        Returns:
            Exception: exception raised by Ability if access is not granted
        """
        return Exception("Access denied for {0} ({1})".format(rule.name, kwargs))

    def can(self, action, *args, **kwargs):
        """Returns True if authorized to make action else False

        Args:
            action (Action)

        Returns:
            bool
        """
        rule = self.rules.get(action, self._default_rule)
        return rule(*args, **kwargs)

    def extend(self, rules):
        """Add/Override existing rules in current authorizations

        Args:
            rules (dict<Action, Rule>): new rules
        """
        self.rules.update(rules)
