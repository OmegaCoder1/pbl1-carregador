import random
import time
import socket
import uuid


HOST = "145.223.27.42"  # IP da VPS
PORT = 8015

def send_request(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(message.encode())  # estou enviando a mensagem como bits
    response = client.recv(1024).decode()
    print("Resposta:", response)
    client.close()
    return response


class User:
    def __init__(self, name, car_model, economy, battery):
        self.name = name
        self.car_model = car_model
        self.economy = economy
        self.battery = battery
        self.x = round(random.uniform(100, 200))  # Coordenada X do carro
        self.y = round(random.uniform(100, 200))  # Coordenada Y do carro
        self.id = round(random.uniform(100, 200))  # ID DO CARRO
        self.balance = 0  # saldo

def create_random_user():
    names = ["Alice", "Bruno", "Carlos", "Diana", "Eduardo"]
    car_models = ["Tesla", "BYD"]
    name = random.choice(names)
    car_model = random.choice(car_models)
    economy = random.randint(100, 400)
    battery = random.randint(70, 100)
    
    return User(name, car_model, economy, battery)


def show_menu(user):
    print("\n=== MENU ===")
    print(f"Usuário: {user.name} | Carro: {user.car_model} | Economia: {user.economy} km/kWh | Bateria: {user.battery}% | Localização: {user.x},{user.y} | ID: {user.id} | SALDO: {user.balance} ")
    print("1 - Start")
    print("2 - Alterar localização")
    print("3 - Alertar bateria")
    print("4 - Postos reservados")
    print("5 - Encerrar reservas")
    print("6 - Encerrar todas as reservas (ADM Geral)")
    print("7 - GERAR PIX 7")
    print("0 - Sair")

def main():
    user = create_random_user()
    
    while True:
        show_menu(user)
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            print("Iniciando a movimentação do carro...")
        elif choice == "2":
            print("Alterando localização...")
            try:
                new_x = float(input("Digite a nova coordenada X: "))
                new_y = float(input("Digite a nova coordenada Y: "))
                
                # Atualiza as coordenadas do usuário
                user.x = new_x
                user.y = new_y
                
                print(f"Localização atualizada para X: {user.x} | Y: {user.y}")
            except ValueError:
                print("Por favor, insira valores numéricos válidos para X e Y.")
        elif choice == "3":
            message = f"low_battery,{user.x},{user.y},{user.id}"
            send_request(message)
            print(f"resposta final: {send_request}")
            print("Alerta de bateria enviado!")
        elif choice == "4":
            message = f"all_station_id,{user.id}"
            send_request(message)
            print("Exibindo postos reservados...")
        elif choice == "5":
            print("Encerrando reservas...")
            message = f"release_stations_by_id,{user.id}"
            send_request(message)
            
        elif choice == "6":
            print("Encerrando reservas...")
            message = f"release_all_stations"
            send_request(message)
            print("Encerrando TODAS as reservas...")
        elif choice == "7":
            valor = input("Qual foi o valor?: ")
            print("gerando pix")
            pix = str(uuid.uuid4())
            print(pix)
            break
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
