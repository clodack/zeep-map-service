from channels.consumer import AsyncConsumer


class YourConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    item = {}
    list = ["iu", "iyg", "viu"]
    #list.append(item)


    async def websocket_receive(self, text_data):
        await self.send({"type": "websocket.send",
            "text": "Hello from Django socket"})
        await self.send({"type": "websocket.send",
            "text": str(text_data)})
        
        

    async def websocket_disconnect(self, event):
        pass