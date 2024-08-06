import asyncio

async def main():
    print('Chaiyasit')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(5)
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(5)

asyncio.run(main())