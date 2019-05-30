from remote import Remote
from client import Client

client = Client("192.168.0.10", 65432)
remote = Remote(client)

def main():
	global client, remote
	ss = input("Enter 1 when you want to start")
	if ss == "1":
		remote.RUN()
	del remote, client


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		remote.stop()
		pass
