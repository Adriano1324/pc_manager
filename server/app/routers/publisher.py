import json

from app.core.gateways.kafka import Kafka
from app.core.models.kafka_message import KafkaMessage
from app.dependencies.kafka import get_kafka_instance
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("")
async def send(data: KafkaMessage, server: Kafka = Depends(get_kafka_instance)):
    try:
        topic_name = server._topic
        await server.aioproducer.send_and_wait(
            topic_name, json.dumps(data.dict()).encode("ascii")
        )
    except Exception as e:
        await server.aioproducer.stop()
        raise e
    return "Message sent successfully"
