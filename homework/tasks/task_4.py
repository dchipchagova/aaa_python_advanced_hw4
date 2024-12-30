import asyncio

answer = []


async def task_1(i: int) -> None | int:
    """
    The first task.
    """
    answer.append('1')
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int) -> None | int:
    """
    The second task.
    """
    answer.append('2')
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    """
    Prints the order, in which coroutines are executed.
    """
    # Отследите порядок исполнения корутин при i = 42 и верните число,
    # соответствующее ему.
    # Когда поток управления входит в task_1 добавьте к результату цифру 1,
    # а когда он входит в task_2, добавьте цифру 2.
    # Пример:
    # i = 7
    # return 12212
    await task_1(i)
    # YOUR CODE GOES HERE
    return int(''.join(str(num) for num in answer))


async def main() -> None:
    """
    Runs coroutine.
    """
    await coroutines_execution_order(i=42)


if __name__ == '__main__':
    asyncio.run(main())
