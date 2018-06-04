from .conditions import FalseCondition, TrueCondition
from .context import Context


class AccessRule(object):
    def __init__(self, resolvers=(), condition=FalseCondition()):
        """
        Args:
            resolvers (list<callable>): list of resolvers
            condition (Condition): a condition
        """
        self._resolvers = resolvers
        self._condition = condition

    def __call__(self, *args, **kwargs):
        """Returns whether or not if rules allows action

        Args:
            params (dict): params received

        Returns:
            bool
        """
        context = Context(args=args, kwargs=kwargs)
        for resolver in self._resolvers:
            resolver(context)

        return self._condition(context)


class Deny(AccessRule):
    """Condition that always deny access"""
    def __init__(self):
        super().__init__(condition=FalseCondition())


class Allow(AccessRule):
    """Condition that always allows access"""
    def __init__(self):
        super().__init__(condition=TrueCondition())
