"""
In this case the envs need be in the system.
 I suggest to use pycharm plugin "EnvFile", it runs your code passing the value from specified .env
"""

from decouple import config

DB_HOST = config("DB_HOST")
DB_HOST_DEFAULT = config("DB_HOST_WRONG", default='mysql_server_default')
VAR_BOOL = config("ENABLE", cast=bool)
VAR_ALL = config("ALL", default='1', cast=int)

PYTHONPATH = config("PYTHONPATH")
PROCESSOR_ARCHITECTURE = config("PROCESSOR_ARCHITECTURE")

print(DB_HOST)
print(DB_HOST_DEFAULT)
print(VAR_BOOL)

print(PYTHONPATH)
print(PROCESSOR_ARCHITECTURE)
