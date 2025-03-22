import socket

HOST = '127.0.0.1'  # 로컬호스트
PORT = 65432        # 사용할 포트

#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버가 {PORT} 포트에서 대기 중...")

conn, addr = server_socket.accept()
print(f"클라이언트 연결됨: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"받은 데이터: {data.decode()}")
    conn.sendall(b"Hello Client!")  # 클라이언트에게 응답

conn.close()
server_socket.close()
