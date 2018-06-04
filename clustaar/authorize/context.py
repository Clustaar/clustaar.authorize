class Context(dict):
    """Object filled by resolvers when evaluating a rule"""
    def __init__(self, args=(), kwargs=None):
        """
        Args:
            args (list): arguments received from ability caller
            kwargs (dict): keyword arguments received from ability caller
        """
        kwargs = kwargs or {}
        super().__init__(kwargs)
        self.args = args
        self.kwargs = kwargs
