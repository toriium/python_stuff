import asyncio
import time

from util import async_long_func, time_execution

await_list = []

async def main():
    print('[main] START')
    print('[main] async_long_func(1)')
    await_list.append(async_long_func(1))

    print('[main] waiting between functions calls')
    time.sleep(1)

    print('[main] async_long_func(2)')
    await_list.append(async_long_func(2))

    print('[main] --------- waiting funcs to end ---------')
    await asyncio.gather(*await_list)
    print('[main] END')



if __name__ == '__main__':
    with time_execution():
        asyncio.run(main())



