from sqlalchemy import create_engine
import yaml
import sys
from utils.formater import UnseenFormatter


class connection(object):
    
    def __init__(self, **kwargs):
        self.kwargs = locals()
    
    def from_config(self, filename):
        if filename:
            config_yaml = yaml.load(filename)
            if config_yaml.get('db_config'):
                self.kwargs = config_yaml.get('db_config')

    def _build_conection_string(self):
        return UnseenFormatter(self._connection_string(), **self.kwargs)

    def _connection_string(self):
        _str_connection = ''
        dbtype = self.kwargs.get('dbtype')
        if dbtype:
            if dbtype == 'sqlite':
                _str_connection = 'sqlite:///{dbpath}'
            elif dbtype == 'postgresql':
                _str_connection = 'postgresql://{username}:{password}@{dbhost}:{dbport}/{dbname}'
            elif dbtype == 'mysql':
                _str_connection = 'mysql://{username}:{password}@{dbhost}:{dbport}/{dbname}'
            elif dbtype == 'oracle':
                _str_connection = 'oracle://{username}:{password}@{dbhost}:{dbport}/{dbname}'
            elif dbtype == 'mssql':
                if sys.platform == 'linux':
                    _str_connection = 'mssql+pyodbc:///?odbc_connect=DRIVER=FreeTDS;SERVER={dbhost};PORT={port};DATABASE={dbname};UID={uid};PWD={password};TDS_Version={tds_v};'
                else:
                    _str_connection = 'mssql+pyodbc:///?odbc_connect=DRIVER=FreeTDS;SERVER={dbhost};PORT={port};DATABASE={dbname};UID={uid};PWD={password};'
        return _str_connection

    def make_connection(self):
        return create_engine(self._build_conection_string())