import time
from concurrent.futures import ThreadPoolExecutor

from echo_server import echo_server
from reply_server import reply_server
from client import client

start=input("Choose 1 to start with echo, 2 with standard: ")
if start=="1":

  executor = ThreadPoolExecutor(max_workers=2)

  tServer = executor.submit(echo_server)
  time.sleep(2)
  tClient = executor.submit(client)

  print("START")

  executor.shutdown()

  print("FINISH")

elif start=="2":

  executor = ThreadPoolExecutor(max_workers=2)

  tServer = executor.submit(reply_server)
  time.sleep(2)
  tClient = executor.submit(client)

  print("START")

  executor.shutdown()

  print("FINISH")

else:
  print("WRONG START PARAMETER")
