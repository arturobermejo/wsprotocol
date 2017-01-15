from server import Websocket, WebsocketServer


class WsEvents(Websocket):

    def onMessage(self, message):
        self.broadcast(message)

    def onConnect(self):
        print(len(self.connections))

    def onDisconnect(self):
        print('close')


server = WebsocketServer(ws_cls=WsEvents)
server.run()
