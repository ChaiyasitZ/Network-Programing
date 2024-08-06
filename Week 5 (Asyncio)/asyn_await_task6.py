import asyncio, time

async def ioioio(wela, chue_ngan):
    print('เริ่ม %s เวลาผ่านไปแล้ว %.6f วินาที'%(chue_ngan, time.time()-t0))
    await asyncio.sleep(wela)
    print('%sเสร็จสิ้นเวลาผ่านไปแล้ว %.6f วินาที'%(chue_ngan, time.time()-t0))
    return '*'+chue_ngan+'เสร็จสิ้น*'
    
async def main():
    cococoru = [ioioio(1.5,'งานที่ 1'),ioioio(2.5,'งานที่ 2'),ioioio(2,'งานที่ 3')]
    phonlap = await asyncio.wait(cococoru)
    print(phonlap)

t0 = time.time()
asyncio.run(main())

