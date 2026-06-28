from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Unicode, _returns=Unicode)
    def greet(ctx, name):
        return f"Hello, {name}"

application = Application(
    [CalculatorService],
    tns="entrypoint.soap.demo",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    wsgi_app = WsgiApplication(application)
    server = make_server("127.0.0.1", 8002, wsgi_app)
    print("SOAP server on http://127.0.0.1:8002 - WSDL at http://127.0.0.1:8002/?wsdl")
    server.serve_forever()