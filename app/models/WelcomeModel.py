"""
    Sample Model File
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    """
    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")
    """
