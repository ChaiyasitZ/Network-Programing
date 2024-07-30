import asyncio, time

async def ioioio(wela, chue_khanom):
    print('เริ่มอบ %s เวลาผ่านไปแล้ว %.5f วินาที'%(chue_khanom, time.time()-t0))
    await asyncio.sleep(wela)
    print('อบ%sเสร็จ ผ่านไปแล้ว %.5f วินาที'%(chue_khanom, time.time()-t0))
    return '*'+chue_khanom+'อบเสร็จ*'

async def main():
    cococoru = [ioioio(3, 'ข้าว'), ioioio(3, 'ไข่'), ioioio(1, 'ครัวซอง')]
    phonlap = await asyncio.gather(*cococoru)
    print(phonlap)

t0 = time.time()
asyncio.run(main())

