head = {
    "value": 12,
    "next": {
        "value": 8,
        "next": {
            "value": 5,
            "next": {
                "value": 4,
                "next": {
                    "value": 4,
                    "next": None
                }
            }
        }
    }
}
print(head['next']['next']['next']['value'])