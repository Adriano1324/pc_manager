import logging
import os
from json import loads

from core.modules.process import Process
from kafka import KafkaConsumer


class CommandExecutor(Process):
    def __init__(self, name):
        super().__init__(name)
        self.consumed_messages: int = 0

    def run(self):
        try:
            # To consume latest messages and auto-commit offsets
            consumer = KafkaConsumer(
                "topic_test",
                bootstrap_servers="0.0.0.0:9092",
                value_deserializer=lambda x: loads(x.decode("utf-8")),
                auto_offset_reset="latest",
                enable_auto_commit=True,
            )
            print(consumer)
            for message in consumer:
                value = message.value
                print(value.get("key"))
                if value.get("key") == "cmd_command":
                    os.system(value.get("value"))

        except Exception as e:
            logging.info("Connection successful", e)
