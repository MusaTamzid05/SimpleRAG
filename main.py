from lib.retrival import CorpusRetrival

def main():
    retrival = CorpusRetrival(path="data/alice.txt", chunk_size=1000)


if __name__ == "__main__":
    main()

