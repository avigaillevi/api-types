import calc_pb2
import calc_pb2_grpc
import grpc

with grpc.insecure_channel("localhost:50051") as channel:
    stub = calc_pb2_grpc.CalculatorStub(channel)
    response = stub.Add(calc_pb2.AddRequest(a=7, b=5))
    print("Add(7, 5) ->", response.result)
