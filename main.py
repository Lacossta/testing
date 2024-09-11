import asyncio

# class Person:
#     def __init__(self, name: str, isMan: bool = True):
#         self._name = name
#         self._isMan = isMan
#
#     async def changeOrientation(self):
#         for i in range(1, 10):
#             print(i)


async def changeOrientation():
    await asyncio.sleep(1)
    for i in range(1, 1000):
        print(i)


async def printTest():
    print("Test1")
    print("Test2")

asyncio.run(changeOrientation())
asyncio.run(printTest())


# print(f"{jecka.name} просто")
# print(f"Статус - {jecka.isMan}")



# class Driver(Person):
#     def __init__(self, name, isMan):
#         super().__init__(name, isMan)
#         print(self._name)