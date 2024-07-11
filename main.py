import sys
import requests

def urls(out_file):
    url2 = sys.stdin.read().splitlines()

    res_urls = []
    bad_urls = []

    for url in url2:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                res_urls.append(url)
            else:
                bad_urls.append(url)
        except requests.exceptions.RequestException:
            bad_urls.append(url)
            continue

    with open(out_file, 'w') as file:
        file.write('\n'.join(res_urls))

    print(f"Saved URLs to: {out_file}")

if __name__ == "__main__":
    out_file = 'urls.txt'
    urls(out_file)
