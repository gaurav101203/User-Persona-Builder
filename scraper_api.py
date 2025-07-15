import praw
import warnings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0.2,convert_system_message_to_human=True)

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
target_username = "Hungry-Move-6603"

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

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.getenv("GOOGLE_API_KEY"))
if not texts:
  print("Warning: texts is empty. Check your text extraction process.")

vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_index,
    return_source_documents=True

)
question1 = f"tell me about behaviour and habits of this person based on these posts while keeping it short and in third person perspective in points. Also give all the citation from where you are taking the charachteristics."
question2 = f"Tell me about Goals and Needs from the context while keeping it short and in third person perspective in points. Also give all the citation from where you are taking the charachteristics."
question3 = f"Tell me about Frustrations of the person from the given context while keeping it short and in third person perspective in points. Also give all the citation from where you are taking the charachteristics."
question4 = f"Motivations of the person from the given context. Just in one or two words and in points."
result1 = qa_chain({"query": question1})
result2 = qa_chain({"query": question2})
result3 = qa_chain({"query": question3})
result4 = qa_chain({"query": question4})


a = result1["result"]
b = result2["result"]
c = result3["result"]
d = result4["result"]

import re
plain_text1 = re.sub(r"\*\*(.*?)\*\*", r"\1", a)
plain_text2 = re.sub(r"\*\*(.*?)\*\*", r"\1", b)
plain_text3 = re.sub(r"\*\*(.*?)\*\*", r"\1", c)
plain_text4 = re.sub(r"\*\*(.*?)\*\*", r"\1", d)


filename = f"{target_username}.txt"

# Use 'w' to create or overwrite the file safely
with open(filename, 'w') as file:
    file.write(plain_text1 + "\n\n")

# Append additional content
with open(filename, 'a') as file:
    file.write("Goals and Needs" + "\n\n"+plain_text2 + "\n\n")
    file.write("Frustrations"+"\n\n"+plain_text3 + "\n\n")
    file.write("Motivations"+"\n\n"+plain_text4 + "\n\n")