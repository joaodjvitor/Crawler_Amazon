# Crawler_Amazon

O projeto a seguir se trata de um scrapping na página: https://www.amazon.com.br/, para que assim seja obtidos o nome, preço e link dos produtos da mesma.

## I - Para obter os resultados do projeto foi utilizados as seguintes tecnologias:

- Python 3
- Beautiful soup 4
- Requests
- Flask
- Flask_cors

## II - Como fazer a execução do projeto:

- Para que o projeto seja executado com sucesso, deve ser instalado as suas depedencias, elas são instaladas da seguinte forma: 
   
   pip install -r requirements.txt
   
- Agora para que o programa seja compilado deve ser utilizado o seguinte comando: 
   
   python3 -m flask run

## III - Endpoint

- O único Endpoint é utilizado da seguinte forma:
   
   localhost5000/search/o_nome_do_produto_que_busca
