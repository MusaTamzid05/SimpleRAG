from lib.rag import WebRAG

def main():
    url_list = ["https://en.wikipedia.org/wiki/Red_Dead_Redemption_2"]
    rag = WebRAG(url_list=url_list,
            chunk_size=1000,
            database_name="web",
            generator_type="groq"
            )
    rag.run()





if __name__ == "__main__":
    main()

