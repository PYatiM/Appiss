import requests

def check_status(url):
    try:
        response = requests.get(url, timeout=5)

        status = response.status_code

        if 200 <= status < 300:
            category = "Success"
        elif 300 <= status < 400:
            category = "Redirection"
        elif 400 <= status < 500:
            category = "Client Error"
        else:
            category = "Server Error"

        return {
            "url": url,
            "status_code": status,
            "category": category,
            "reason": response.reason,
            "success": True
        }

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    result = check_status(url)

    if result["success"]:
        print(f"\nURL: {result['url']}")
        print(f"Status Code: {result['status_code']}")
        print(f"Category: {result['category']}")
        print(f"Reason: {result['reason']}")
    else:
        print(f"\nFailed to check status: {result['error']}")
