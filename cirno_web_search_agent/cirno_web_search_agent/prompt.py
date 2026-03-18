# tools
websearch_return_schema = {
    "type": "object",
    "properties": {
        "url": {
            "type": "string",
            "description": "The url of this webpage"
        },
        "summary":{
            "type": "string",
            "description": "Summarize the information in the website in a detailed way, do not change the specialized vocabularies in it. **You are not allowed to get rid of important information in the web page.**"
        }
    },
    "required": ["url", "summary"]
}
websearch_exa_agent_system_prompt = """
Use clear and logical tone to respond to the query. 
**Do not alter the meaning of the webpages you get** 
"""