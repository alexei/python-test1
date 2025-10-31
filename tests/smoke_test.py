from python_test1 import hello

message = hello()
if message == "Hello from python-test1!":
    print("Smoke test succeeded")
else:
    raise RuntimeError(message)
