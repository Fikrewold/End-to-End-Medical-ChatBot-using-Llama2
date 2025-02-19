from dotenv import load_dotenv  # ✅ Correct import

load_dotenv() 


import pinecone
import os

# Initialize Pinecone

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
#PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


pinecone.init(
    api_key=PINECONE_API_KEY
    ,  # Replace with your actual Pinecone API key
    environment="us-east-1-aws"  # Match your AWS region
)

# Check if the index exists
index_name = "medical-chatbot"
if index_name in pinecone.list_indexes():
    print(f"Connected successfully to Pinecone index: {index_name}")
else:
    print("Index not found. Check the index name or connection settings.")

# Connect to the index
index = pinecone.Index(index_name)

# Upsert a sample vector
index.upsert(vectors=[("test_id", [0.1] * 384)])

# Perform a query
result = index.query(queries=[[0.1] * 384], top_k=1, include_values=True)

print("Query result:", result)
