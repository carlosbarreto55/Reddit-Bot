import requests
from pprint import pprint
from config import Config
# from src import config


class RedditSearcher:
    def __init__(self):
        self.config= Config
        self.base_url = self.config.BASE_URL
        self.headers = {
            'User-Agent' : self.config.USER_AGENT
        }


    def search_posts(self,keywords,limit=50,sort= 'relevance',time_filter ='all'):

            """
            Search reddit posts using keywords

            Args: API Params
                keywords : keywords used for the search
                limit : number of result that the API is gonna show
                sort: category that the api is gonna filter the results
                time_filter : category of time that the APi is gonna show
            """
    

            params= {
                'q': keywords,
                'sort': sort,
                'limit': limit,
                't':time_filter

            }


            try:
                response = requests.get(self.base_url,headers=self.headers,params=params)
                response.raise_for_status()
                
                
                apidata= response.json()
                posts = []
                # This loop is gonna access every dic object inside the json´s response and extract the followign information:
                for post in apidata ['data']['children']:
                    post_data= post['data']
                    posts.append ({
                    'title' : post_data['title'],
                    'subreddit' : post_data['subreddit'],
                    'post_author' : post_data ['author_fullname'],
                    'num_comments' : post_data['num_comments'],
                    'post_url' : post_data ['permalink'],
                 
                    })
                return posts




            except requests.HTTPError as e:
               print (f"HTTP Error :{e}")
               return None



from pprint import pprint

# Supondo que RedditSearcher está no mesmo arquivo ou foi importado corretamente

def main():
    searcher = RedditSearcher()
    termo = input("Digite o termo de busca: ")
    try:
        limite = int(input("Quantos posts você quer buscar? "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    resultados = searcher.search_posts(termo, limit=limite)
    if not resultados:
        print("Nenhum resultado encontrado ou houve um erro na busca.")
        return

    print(f"\nMostrando {len(resultados)} resultados para '{termo}':\n")
    for i, post in enumerate(resultados, 1):
        print(f"Post {i}:")
        print(f"  Título: {post['title']}")
        print(f"  Subreddit: {post['subreddit']}")
        print(f"  Autor: {post['post_author']}")
        print(f"  Comentários: {post['num_comments']}")
        print("-" * 40)

if __name__ == "__main__":
    main()

