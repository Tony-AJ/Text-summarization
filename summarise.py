import sumy 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text: str, sentence_count: int = 5) -> str:
    """
    Summarizes the given text using LSA (Latent Semantic Analysis).
    :param text: The input article.
    :param sentence_count: Number of sentences in the summary.
    :return: Summarized text.
    """
    if not text.strip():
        return "Error: Empty text provided."
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    
    return " ".join(sentence.__str__().strip() for sentence in summary)

def main():
    """Handles user input and generates the summary."""
    article_text = input("Enter the article text: ")
    try:
        sentence_count = int(input("Enter the number of summary sentences: "))
        if sentence_count <= 0:
            raise ValueError("Sentence count must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    summary = summarize_text(article_text, sentence_count)
    print("\nSummary:", summary)

if __name__ == "__main__":
    main()
