""" helper functions for yaml usage """

class myyaml():
    """ myyaml """

    _yaml = None
    parser = None

    def __init__(self):
        """ __init__ """
        pass

    def available(self):
        """ available() """
        if not myyaml._yaml:
            try:
                import yaml
                myyaml._yaml = yaml
                myyaml.parser = yaml.parser
            except ImportError:
                return False
        return True

    def safe_load(self,value_string):
        """ safe_load() """
        return myyaml._yaml.safe_load(value_string)

    def safe_dump(self, results):
        """ safe_dump() """
        return myyaml._yaml.safe_dump(results)
