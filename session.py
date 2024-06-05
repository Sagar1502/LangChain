from langchain_google_genai import GoogleGenerativeAI
key = 'AIzaSyA5kPLqk7tipZD5BA--oGSs4F54beP3QJA'
llm=GoogleGenerativeAI(model="gemini-pro",google_api_key=key)
print(
    llm.invoke(
        "list of 5 indian cricketer"
    )
)