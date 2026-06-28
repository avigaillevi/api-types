from zeep import Client

# ה-client קורא את ה-WSDL ובונה ממנו את הפעולות הזמינות אוטומטית
client = Client("http://127.0.0.1:8002/?wsdl")

print("add(7, 5) ->", client.service.add(7, 5))
print('greet("Joe") ->', client.service.greet("Joe"))