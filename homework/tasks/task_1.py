from asyncio import Task
from typing import Callable, Coroutine, Any
import asyncio


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    """
    Print steps of the lifecycle of the coroutine.
    """
    # На вход приходит одна из стадий жизненного цикла корутины,
    # необходимо вернуть результат её выполнения.

    if isinstance(f, Callable):
        # YOUR CODE GOES HERE
        return await f()
    elif isinstance(f, Task):
        # YOUR CODE GOES HERE
        return await f
    elif isinstance(f, Coroutine):
        # YOUR CODE GOES HERE
        return await f
    else:
        raise ValueError('invalid argument')


async def say_hello() -> None:
    """
    Greeting func.
    """
    print('Hello')


async def main() -> None:
    """
    Runs coroutine.
    """
    task = await_my_func(say_hello())
    await task
    task2 = await_my_func(say_hello)
    await task2
    task3 = asyncio.create_task(await_my_func(say_hello()))
    await task3
    task4 = await_my_func('123')
    await task4

if __name__ == '__main__':
    asyncio.run(main())
