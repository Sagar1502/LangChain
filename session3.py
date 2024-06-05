from langchain_community.document_loaders.csv_loader import CSVLoader
loader=CSVLoader(file_path="C:\\Users\\DELL\\OneDrive\\Documents\\data science file\\Visadataset.csv")
data=loader.load()
print(data)
print(data[0])
print(data[0].page_content)
print(data[0].metadata)
