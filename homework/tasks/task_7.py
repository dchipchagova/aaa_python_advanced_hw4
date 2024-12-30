import abc
import asyncio
from concurrent.futures import ThreadPoolExecutor


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    """
    A class to process requests.
    """
    def __init__(self, model: AbstractModel):
        self._model = model

    async def handle_request(self) -> None:
        """
        Processes heavy calculations.
        """
        # Модель выполняет некий тяжёлый код (ознакомьтесь с
        # ним в файле тестов),
        # вам необходимо добиться его эффективного
        # конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины
        # handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин,
        # запущенных конкурентно.
        #
        # YOU CODE GOES HERE
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers=10) as executor:
            await loop.run_in_executor(executor, self._model.compute)


async def main() -> None:
    """
    Runs coroutine.
    """
    with ThreadPoolExecutor(max_workers=100):
        handler = Handler(AbstractModel())
        tasks = [
            asyncio.create_task(handler.handle_request()) for _ in range(3)
        ]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
