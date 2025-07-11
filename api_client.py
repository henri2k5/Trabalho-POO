import requests

class RAWGClient:
    BASE_URL = "https://api.rawg.io/api/games"
    API_KEY = "7cd884fbb481408aa168d716f213589a"  

    @staticmethod
    def buscar_jogo(nome_jogo):
        params = {"search": nome_jogo, "key": RAWGClient.API_KEY}
        resposta = requests.get(RAWGClient.BASE_URL, params=params)
        if resposta.status_code == 200:
            resultados = resposta.json()["results"]
            if resultados:
                jogo = resultados[0]
                return {
                    "nome": jogo["name"],
                    "nota": jogo.get("rating", "N/A"),
                    "genero": jogo["genres"][0]["name"] if jogo["genres"] else "Indefinido"
                }
        return None