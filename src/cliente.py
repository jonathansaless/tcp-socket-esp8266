import socket
 
HOST = '10.8.16.145'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
 
# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)
 
print('Digite suas mensagens')
print('Para sair use CTRL+X\n')
 
# Recebendo a mensagem do usuário final pelo teclado
mensagem = input()
 
# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
    tcp.send(str(mensagem).encode())
    mensagem = input()
 
# Fechando o Socket
tcp.close()
