import requests

def check_url(url):
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
            "status": status,
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


def bulk_check(urls):
    results = []
    for url in urls:
        url = url.strip()
        if url:
            results.append(check_url(url))
    return results
