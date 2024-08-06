import asyncio,time

async def ioioio(wela, chue_ngan):
    print('เริ่ม %s เวลาผ่านไปแล้ว %.5f วินาที'%(chue_ngan, time.time()-t0))
    await asyncio.sleep(wela)
    print('เสร็จสิ้น %s เวลาผ่านไปแล้ว %.5f วินาที'%(chue_ngan, time.time()-t0))
    return

async def main():
    print('== ฟังก์ชัน main เริ่มทำงาน ==')
    task1 = asyncio.create_task(ioioio(1.5, 'งานที่ 1'))
    task2 = asyncio.create_task(ioioio(2.5, 'งานที่ 2'))
    task3 = asyncio.create_task(ioioio(2.4, 'งานที่ 3'))
    print('== ฟังก์ชัน main กำลังรองาน ==')
    await task2
    print('== งานเสร็จแล้ว ==')

t0 = time.time()
asyncio.run(main())    