from fastapi import WebSocket
import random

class SocketPool:
    __conn: list[WebSocket]

    def __init__(self):
        self.__conn = []

    def add(self, socket: WebSocket):
        self.__conn.append(socket)

    def remove(self, socket: WebSocket):
        self.__conn.remove(socket)

    async def random_send(self, message: dict):
        await random.choice(self.__conn).send_json(message)

    async def broadcast(self, message: dict):
        for socket in self.__conn:
            await socket.send_json(message)