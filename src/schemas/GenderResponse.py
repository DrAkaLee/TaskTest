GenderResponse_SCHEMA = {
    "type": "object",
    "properties": {
        "isSuccess": {
            "type": "boolean"
        },
        "errorCode": {
            "type": "integer"
        },
        "errorMessage": {
            "type": ["string", "null"]
        },
        "idList": {
            "type": "array",
            "items": {
                "type": "number"
            }
        }
    },
        "required": ["errorCode", "isSuccess"]
    }
