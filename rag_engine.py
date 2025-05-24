import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

DATA_PATH = "docs/faqs_en.json"
INDEX_PATH = "embeddings/index.faiss"
META_PATH = "embeddings/meta.json"

# In-memory data
faq_texts = []
faq_metadata = []

def load_faq_data():
    global faq_texts, faq_metadata

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        faqs = json.load(f)

    questions = [item["Question"] for item in faqs]
    answers = [item["Answer"] for item in faqs]
    categories = [item["Category"] for item in faqs]

    embeddings = model.encode(questions, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    # Save index
    os.makedirs("embeddings", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    # Save metadata
    faq_texts = answers
    faq_metadata = [{"question": q, "category": c} for q, c in zip(questions, categories)]
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(faq_metadata, f, indent=2)

    print(f"[INFO] Indexed {len(questions)} FAQs.")

def search_faq(query, k=1):
    index = faiss.read_index(INDEX_PATH)

    with open(META_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    query_vector = model.encode([query])
    D, I = index.search(np.array(query_vector), k)

    if I[0][0] == -1:
        return "Sorry, I couldn't find an answer to that question."

    idx = I[0][0]
    return f"📌 *Category:* {metadata[idx]['category']}\n\n💬 {faq_texts[idx]}"

if __name__ == "__main__":
    load_faq_data()
    print(search_faq("How do I apply for LKG admission?"))
