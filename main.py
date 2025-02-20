from lib.retrival import CorpusRetrival

def main():
    retrival = CorpusRetrival(path="data/alice.txt", chunk_size=1000, database_name="test")

    while True:
        prompt = input(">>> ")
        result = retrival.get(query_text=prompt, result_count=2)
        response_list = result["documents"][0]

        for index, response in enumerate(response_list):
            print(f"{index} => {response}")




if __name__ == "__main__":
    main()

