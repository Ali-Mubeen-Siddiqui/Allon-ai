from tools.web import *
from tools.general import *

functions = [
    {
        "name": "open_site",
        "description": "The function opens any site in a web browser.",
        "parameters": {
            "type": "object",
            "properties": {
                "site_url": {
                    "type": "string",
                    "description": "URL of the site to be opened"
                }
            },
            "required": ["site_url"]  
        }
    },

    {
        "name": "get_current_time",
        "description": "returns current date,time or year according to format given as parameters",
        "parameters": {
            "type": "object",
            "properties": {
                "format": {
                    "type": "string",
                    "description": "format of time ,i.e format we put in strftime() ,put the format only with the required features"
                }
            },
            "required": ["format"]  
        }
    },

    {
        "name": "write_to_file",
        "description": "The function opens a file with the given filename and creates one if not present, and writes the given text in that file.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "text to be written"
                },
                "filename":{
                    "type":"string",
                    "description":"the file to be created or opened WITH the extension "
                }
            },
            "required": ["text","filename"]  
        }
    }


]

funcs_table = {
    "open_site":open_site,
    "get_current_time": get_current_time,
    "write_to_file":write_to_file
}
