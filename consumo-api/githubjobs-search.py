import requests
import json

def main():
    option = -1

    while option != 0:
        menu_text = "DIGITE UMA OPÇÃO: \n 1 - LISTAR VAGAS POR LINGUAGEM \n 2 - LISTAR VAGAS POR CIDADE \n 0 - SAIR \n >> "
    
        option = int(input(menu_text))

        if option == 1:
            language = input("LINGUAGEM: ").lower()
            url = "https://jobs.github.com/positions.json?description=" + language + "&page=1"
            
            search_jobs(url)

        elif option == 2:
            city = input("CIDADE: ").lower()
            city = city.replace(" ", "+")
            url = "https://jobs.github.com/positions.json?location="+ city + "&page=1"
            
            search_jobs(url)

        elif option == 0:
            print("SAINDO...")
            break
        
        else:
            print("OPÇÃO INVÁLIDA!")
            break

def search_jobs(url):
    response = requests.get(url)
    dict_content = json.dumps(response.json())
    content = json.loads(dict_content)
            
    for i in content:
        print(i["title"] + " - " + i["type"] + " - " + i["company"] + " - \n" + i["url"] + " - \n" + i["created_at"])
        print("-----")

if __name__ == "__main__":
    main()