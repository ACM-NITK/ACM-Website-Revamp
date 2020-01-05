# Automatic router to indicate the database for each model


# If the model is in SMP app, the database should be 'mongo_db' (Cloud-based mongodb database), else default sqlite database
class SMPRouter:
    route_app_labels = {'SMP'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'mongo_db'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'mongo_db'
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
