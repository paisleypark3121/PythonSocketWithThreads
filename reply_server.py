import socket
import config

def reply_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((config.HOST, config.PORT))
    s.listen()
    print("SERVER - waiting for connection")
    conn, addr = s.accept()
    with conn:
      print('SERVER - connected by', addr)
      while True:
        data = conn.recv(1024)
        if not data:
          break
        print("SERVER - received data: ",data.decode("utf-8"))

        msg=input("SERVER - messagge: ")
        if not msg:
          conn.close()
          break
        #print("SERVER - sending: ",msg)
        conn.sendall(msg.encode("utf-8"))

  print("SERVER: SOCKET CLOSED")