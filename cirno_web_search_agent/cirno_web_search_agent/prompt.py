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
            "description": "The summary of this webpage, **DO NOT ALTER THE INFORMATION OF THIS WEBPAGE AND USE THE EXPERTISE PHRASES INSIDE IT.**"
        }
    },
    "required": ["url", "summary"]
}
