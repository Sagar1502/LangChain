from langchain_google_genai import GoogleGenerativeAIEmbeddings
api_key="AIzaSyA5kPLqk7tipZD5BA--oGSs4F54beP3QJA"
embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key,timeout=100)
vector=embeddings.embed_query("hello, world")
print(vector[:5])
print(len(vector))

"""
Sentence represents with a vector has 768 value
dimensionality : 768 
"""
print("sagar samantasinghar")