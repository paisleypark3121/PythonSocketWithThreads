import socket
import config

def client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((config.HOST, config.PORT))
    print("CLIENT - connected")
    while True:
      msg=input("CLIENT - messagge: ")
      if not msg:
        s.close()
        break
      #print("CLIENT - sending: ",msg)
      s.sendall(msg.encode("utf-8"))
      data = s.recv(1024)
      if not data:
          break
      print('CLIENT - received: ', data.decode("utf-8"))

  print("SOCKET CLOSED")