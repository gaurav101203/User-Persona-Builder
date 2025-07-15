import praw
import warnings
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

model = OllamaLLM(model="phi",temperature=0.2)
warnings.filterwarnings("ignore")
# restart python kernal if issues with langchain import.
reddit = praw.Reddit(
    client_id="your client ID",
    client_secret="your secret key",
    user_agent="MyRedditScraper/0.1 by your_Reddit_username",
    username="your_Reddit_username",
    password="your_Reddit_password"
)

# Target user
target_username = "kojied"

user = reddit.redditor(target_username)

citation = []
# Fetch latest 10 posts
for submission in user.submissions.new(limit=1000):
    citation.append(f"Post:{submission.selftext} with Post ID:{submission.id}")
for comment in user.comments.new(limit=1000):
    citation.append(f"Comment:{comment.body} with Comment ID:{comment.id}")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
context = "\n\n".join(str(p) for p in citation)
texts = text_splitter.split_text(context)

embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
if not texts:
  print("Warning: texts is empty. Check your text extraction process.")

vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k": 10})
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    retriever=vector_index,
    return_source_documents=True

)
question1 = (
    "Based ONLY on the following Reddit posts and comments from the given context, extract the user's behaviors and habits. "
    "Output should:\n"
    "- Be in short, clear, third-person bullet points.\n"
    "- Each point must start with '* '.\n"
    "- Each point must end with citations of Post ID(s) and/or Comment ID(s) in parentheses indicating the source(s) of the insight.\n"
    "- Skip points where there is insufficient data, but include all insights you can confidently extract.\n\n"
    "Example:\n"
    "* Actively tracks expenses and seeks to reduce impulsive purchases (Post ID: abc123).\n"
    "* Enjoys exploring new technology like VR devices (Comment ID: def456).\n\n"
)
question2 = (
    "Based ONLY on the following Reddit posts and comments from the given context, extract the user's goals and needs. "
    "Output should:\n"
    "- Be in short, clear, third-person bullet points.\n"
    "- Each point must start with '* '.\n"
    "- Each point must end with citations of Post ID(s) and/or Comment ID(s) in parentheses indicating the source(s) of the insight.\n"
    "- Skip points where there is insufficient data, but include all insights you can confidently extract.\n\n"
    "Example:\n"
    "* Wants to save money while maintaining lifestyle quality (Post ID: xyz789).\n"
    "* Aims to launch a tech product for AR users (Comment ID: ghi012).\n\n"
)
question3 = (
    "Based ONLY on the following Reddit posts and comments from the given context, extract the user's frustrations. "
    "Output should:\n"
    "- Be in short, clear, third-person bullet points.\n"
    "- Each point must start with '* '.\n"
    "- Each point must end with citations of Post ID(s) and/or Comment ID(s) in parentheses indicating the source(s) of the insight.\n"
    "- Skip points where there is insufficient data, but include all insights you can confidently extract.\n\n"
    "Example:\n"
    "* Frustrated by the high cost of VR equipment (Post ID: vr456).\n"
    "* Finds it hard to balance work and personal projects (Comment ID: work789).\n\n"
)
question4 = (
    "Based ONLY on the following Reddit posts and comments from the given context, extract the user's motivations. "
    "Output should:\n"
    "- Be in 1-3 words per point.\n"
    "- Each point must start with '* '.\n"
    "- Each point must end with citations of Post ID(s) and/or Comment ID(s) in parentheses indicating the source(s).\n"
    "- Skip points where there is insufficient data.\n\n"
    "Example:\n"
    "* Financial independence (Post ID: xyz789).\n"
    "* Exploring AR tech (Comment ID: abc123).\n\n"
)

result1 = qa_chain({"query": question1})
result2 = qa_chain({"query": question2})
result3 = qa_chain({"query": question3})
result4 = qa_chain({"query": question4})

a = result1["result"]
b = result2["result"]
c = result3["result"]
d = result4["result"]

filename = f"{target_username}.txt"
with open(filename, 'w') as file:
    file.write("Behaviors and Habits\n\n" + a + "\n\n")
    file.write("Goals and Needs\n\n" + b + "\n\n")
    file.write("Frustrations\n\n" + c + "\n\n")
    file.write("Motivations\n\n" + d + "\n\n")
