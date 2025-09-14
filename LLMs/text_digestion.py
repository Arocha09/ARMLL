from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator



text_data = "This is some sample text data."


# Split the text into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(text_data)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create a vector store
vectorstore = Chroma.from_texts(texts, embedding=embeddings)

# Create an index
index = VectorstoreIndexCreator().create(vectorstore)

# Save the index and embeddings to disk
index.save_to_disk('index.pkl')
embeddings.save_to_disk('embeddings.pkl')