import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {ball + 1} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    str_man_1 = asyncio.create_task(start_strongman('Pasha', 3))
    str_man_2 = asyncio.create_task(start_strongman('Denis', 4))
    str_man_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await str_man_1
    await str_man_2
    await str_man_3

async def main():
    task_man = asyncio.create_task(start_tournament())
    await task_man

asyncio.run(main())
