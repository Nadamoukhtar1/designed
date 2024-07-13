def fetch_outfit_details(code):
    outfit_details = {
        "name": "Casual Shirt",
        "size": "M",
        "color": "Blue"
    }
    return outfit_details

# Example usage
if __name__ == "__main__":
    outfit_code = "1234567890"
    outfit_details = fetch_outfit_details(outfit_code)
    print(outfit_details)
