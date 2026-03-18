# tools
# Web Search Tool
websearch_return_schema = {
    "type": "object",
    "properties": {
        "url": {
            "type": "string",
            "description": "The url of this webpage"
        },
        "summary":{
            "type": "string",
            "description": "Summarize the information in the website in a detailed and clear way, do not change the specialized vocabularies in it. **You are not allowed to get rid of important information in the web page.**"
        },
        "title":{
            "type": "string",
            "description": "The title of the webpage"
        }
    },
    "required": ["url", "summary"]
}
keywords_definition = """
For this field, you must type in the keywords of the content of the info you want to know from the internet:
e.g. you can search about news about climate technology by using this input: 
```python
["technology", "news", "climate"]
```
Or you can type in the full sentence or multiple full sentences.: 
```python
["The CEO of OpenAI. "]
```
**The result fetched would be better if you use affirmative form.**
"""
websearch_description = """
The tool that can find you the info you needed in the internet. 
- The content of the webpages is summarized by a llm when calling this tool. 
- The tool would return the summary of the webpages and the url. 
- **YOU MUST ADD THE UTL REFERENCE IN YOUR RESULT IF YOU USE THE INFO FETCHED BY THIS TOOL. NOTE THAT THE URL WOULD BE RETURNED WITH SUMMARY TO YOU AFTER CALLING THIS TOOL.**
"""