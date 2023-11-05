import asyncio

from aiokafka import AIOKafkaConsumer
from sqlalchemy.orm import Session

from db.base import engine
from db.models import UserStats
from db.user_stats import UserStatsRepo


async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        client_id='all',
        bootstrap_servers='localhost:9094',
        group_id="my-group",
        enable_auto_commit=False,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            key = msg.key.decode()
            val = msg.value.decode()
            if key == 'get_user_call':
                user_id = int(val)
                user_stat = UserStats(user_id=user_id)
                with Session(bind=engine.connect()) as session:
                    created_event = UserStatsRepo(session).create_user_stat(
                        user_stat=user_stat
                    )
            #     msg.topic,
            #     msg.partition,
            #     msg.offset,
            #     msg.key,
            #     msg.value,
            #     msg.timestamp,
    finally:
        await consumer.stop()


async def main():
    await consume()


if __name__ == "__main__":
    asyncio.run(main())
