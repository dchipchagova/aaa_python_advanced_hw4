import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    """
    Runs and prints coroutines in a given order (sorted by a number).
    """
    # Необходимо выполнить все полученные корутины, затем
    # упорядочить их результаты по полю number и вернуть строку,
    # состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    # YOUR CODE GOES HERE
    united_tickets = await asyncio.gather(*coros)
    united_tickets = sorted(united_tickets, key=lambda x: x.number)
    return ''.join(ticket.key for ticket in united_tickets)


async def just_return_ticket(ticket: Ticket) -> Ticket:
    """
    Func for creating a coroutine.
    """
    return ticket


async def main() -> None:
    """
    Runs coroutine.
    """
    r1 = Ticket(number=2, key='мыла')
    r2 = Ticket(number=1, key='мама')
    r3 = Ticket(number=3, key='раму')

    tickets = [r1, r2, r3]

    coros = [just_return_ticket(ticket) for ticket in tickets]
    answer = await coroutines_execution_order(coros)
    print(answer)


if __name__ == '__main__':
    asyncio.run(main())
