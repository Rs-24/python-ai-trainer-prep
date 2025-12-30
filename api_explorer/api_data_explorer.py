import requests
import sys

def get_num_facts() -> int:
    """
    Gets the number of facts to show from the command line. Returns one if no
    valid number is given. The only input is sys.argv (there are no input 
    parameters to the function), and the only output is num_facts
    """
    num_facts = 1
    if len(sys.argv) > 1:
        try:
            if int(sys.argv[1]) > 0:
                num_facts = int(sys.argv[1])
        except ValueError:
            print("Number of facts to print must be a positive integer. Defaulting to 1")
    return num_facts

def get_facts(n: int, url: str) -> None:
    """
    Obtains n number of facts from the API and the length of each fact. The
    only inputs are n and the url, and the function does not return anything 
    """
    for _ in range(0, n):
        try:
            response = requests.get(url, timeout = 10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            continue

        try:
            data = response.json()
        except ValueError:
            print("Failed to parse JSON from response")
            continue

        fact = data.get("fact", "No fact found")
        length = data.get("length", "No fact found")
        print(f"Cat fact: {fact}")
        print(f"Length: {length}")


def main():
    url = "https://catfact.ninja/fact"
    n = get_num_facts()
    get_facts(n, url)

if __name__ == "__main__":
    main()

