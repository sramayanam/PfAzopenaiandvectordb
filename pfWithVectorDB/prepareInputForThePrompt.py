from promptflow import tool
from typing import List
from promptflow_vectordb.core.contracts import SearchResultEntity


@tool
def my_python_tool(vecdbresults: List[dict]) -> str:
    def format_document(doc: dict):
        return f"Content: {doc['Content']}\nSource: {doc['Title']}"
    concatenateInputs = []
    for result in vecdbresults:
        content = SearchResultEntity.from_dict(result).text
        title = SearchResultEntity.from_dict(
            result).original_entity['title'][:-9]
        concatenateInputs.append({'Content': content, 'Title': title})
    finalString = "\n\n".join([format_document(input)
                              for input in concatenateInputs])
    return finalString
