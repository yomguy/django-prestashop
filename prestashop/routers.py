
class PrestaRouter(object):
    """
    A router to control all database operations on models in prestashop
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'prestashop':
            return 'prestashop'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'prestashop':
            return 'prestashop'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'prestashop' or \
           obj2._meta.app_label == 'prestashop':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'prestashop':
            return db == 'prestashop'
        return None
