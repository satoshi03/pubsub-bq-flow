import datetime

class Config():
    def _load_from_file(self, config_path):
        with open(config_path, 'r') as f:
            import yaml
            config = yaml.load(f)
            return config
        return None


class PubSubImportConfig(Config):
    def __init__(self, config_path):
        self.topic = ''
        self.subscription = ''
        self.data_key = ''
        self._update_config(self._load_from_file(config_path))

    def _update_config(self, config):
        if not config:
            return

        if 'pubsub' in config:
            self.topic = config['pubsub'].get('topic')
            self.subscription = config['pubsub'].get('subscription')
            self.data_key = config['pubsub'].get('data_key')
        return


class BigQueryExportConfig(Config):
    def __init__(self, config_path):
        self.table_name = ''
        self.table_date_partition = False
        self.schema = {}
        self._update_config(self._load_from_file(config_path))

    def _update_config(self, config):
        if not config:
            return

        if 'bigquery' in config:
            self.table_name = config['bigquery'].get('table_name')
            self.schema = config['bigquery'].get('schema')

            if 'table_date_partition' in config['bigquery']:
                self.table_date_partition = config['bigquery'].get('table_name')

    def get_table_name(self):
        if self.table_date_partition:
            now = datetime.datetime.now()
            return now.strftime(self.table_name)
        else:
            return self.table_name

    def get_schema_string(self):
        return ""
