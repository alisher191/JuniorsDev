import asyncio
import socket

#domain :5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET -> IP протокол 4й версии
# SOCK_STREAM -> говорит о том, что речь пойдет о поддержке протокола TCP

# Серверный сокет ↓
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Для повторного использования номера порта нашего сокета
server_socket.bind(('localhost', 5000)) # Привязка к определенному сокету и домену
server_socket.listen() # Прослушка входящего буфера на предмет каких-то входящих подключений

while True:
    """
    Отношения между клиентом и сервером это всегда длящиеся отношения и
    мы не знаем сколько времени это взаимодействие займет, поэтому, обычно, как 
    правило, используется бесконечный цикл while true
    """
    