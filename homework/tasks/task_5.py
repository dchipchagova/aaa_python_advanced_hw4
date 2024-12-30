import asyncio
from typing import Coroutine


async def some_func() -> None:
    """
    Some waiting func.
    """
    await asyncio.sleep(5)


async def limit_execution_time(coro: Coroutine,
                               max_execution_time: float) -> None:
    """
    Checks that the coroutine is done, TimeoutError otherwise.
    """
    # Функция принимает на вход корутину, которую необходимо запустить,
    # однако иногда она выполняется слишком долго, это время необходимо
    # ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена,
    # и все они завершились за заданное время.
    # YOUR CODE GOES HERE
    try:
        task = asyncio.create_task(coro)
        await asyncio.wait_for(task, max_execution_time)
    except asyncio.TimeoutError:
        print('Execution time exceed')


async def limit_execution_time_many(*coros: Coroutine,
                                    max_execution_time: float) -> None:
    """
    Checks that all coroutines are done, TimeoutError otherwise.
    """
    # Функция эквивалентна limit_execution_time, но
    # корутин на вход приходит несколько.
    # YOUR CODE GOES HERE
    try:
        await asyncio.wait_for(
            asyncio.gather(*coros), timeout=max_execution_time)
    except asyncio.TimeoutError:
        print('Execution time exceed')


async def main() -> None:
    """
    Runs coroutine.
    """
    await limit_execution_time(some_func(), max_execution_time=10.0)
    await limit_execution_time_many(*[some_func(), some_func()],
                                    max_execution_time=7.0)


if __name__ == '__main__':
    asyncio.run(main())
