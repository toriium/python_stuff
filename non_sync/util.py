from contextlib import contextmanager
from datetime import datetime
import time

GLOBAL = [1,]

def long_func(number: int):
    print(f'[long_process:{number}] --------- START ---------')

    GLOBAL.append(GLOBAL[-1] + 1)
    print(f'[long_process:{number}] GLOBAL:{GLOBAL}')

    time.sleep(3)
    print(f'[long_process:{number}] realized long_process')

    print(f'[long_process:{number}] --------- END ---------')

async def async_long_func(number: int):
    print(f'[async_long_func:{number}] --------- START ---------')

    GLOBAL.append(GLOBAL[-1] + 1)
    print(f'[async_long_func:{number}] GLOBAL:{GLOBAL}')

    time.sleep(3)
    print(f'[async_long_func:{number}] realized long_process')

    print(f'[async_long_func:{number}] --------- END ---------')

@contextmanager
def time_execution():
    star = datetime.now()
    yield
    print('--'*20)
    print(f'The execution took {datetime.now() - star} time ')
