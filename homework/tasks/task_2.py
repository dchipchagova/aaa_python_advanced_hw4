import asyncio


async def magic_func() -> int:
    """
    Some func, which returns 42.
    """
    return 42


async def fix_this_code() -> int:
    """
    Returns magic_func.
    """
    # С этой функцией что-то не так, необходимо
    # разобраться что именно и починить её.
    # FIX THIS CODE
    return await magic_func()


async def main() -> None:
    """
    Runs coroutine.
    """
    task = asyncio.create_task(fix_this_code())
    answer = await task
    print(answer)


if __name__ == '__main__':
    asyncio.run(main())
