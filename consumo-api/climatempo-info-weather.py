import requests
import json

def main():
    option = -1
    token = "92dfab00d4e41847fa34476b87db56ce"
    menu_text = "PREVISÃO DO TEMPO DE CIDADES DO PIAUI \n DIGITE: \n 1 - TERESINA \n 2 - CAMPO MAIOR \n 3 - ALTOS \n 0 - SAIR \n >> "
    
    while option != 0:
        option = int(input(menu_text))
        
        if option == 1:
            id_local = "6951"
            url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+ id_local +"/current?token=" + token
            search(url)

        elif option == 2:
            id_local = "7009"
            url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+ id_local +"/current?token=" + token
            search(url)

        elif option == 3:
            id_local = "7193"
            url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+ id_local +"/current?token=" + token
            search(url)

        elif option == 0:
            print("SAINDO...")
            break

        else:
            print("OPÇÃO INVÁLIDA!")
            break

def search(url):
    response = requests.get(url)
    dict_content = json.dumps(response.json())
    content = json.loads(dict_content)
    
    print(">> " + content["name"] + ", " + content["state"] + ", " + content["country"])
    print(">> Temperatura: " + str(content["data"]["temperature"]) + "°C - Direção dos ventos:" + str(content["data"]["wind_direction"]) + " - Velocidade dos ventos: " + str(content["data"]["wind_velocity"]) + "km/h")
    print(">> Humidade: " + str(content["data"]["humidity"]) + " - Condição: " + content["data"]["condition"] + " - Sensação Térmica: " + str(content["data"]["sensation"]) + "°C")
    print(">> " + content["data"]["date"])

if __name__ == "__main__":
    main()