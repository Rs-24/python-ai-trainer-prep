# API Explorer

This folder contains a small Python script that calls a public web API (`https://catfact.ninja/fact`) to fetch and display random cat facts in a clean, human-readable way.

## What this shows

- Working with HTTP requests in Python using `requests`
- Parsing JSON responses from a real API
- Handling common errors (network issues, timeouts, non-JSON responses)
- Validating and using command-line arguments with `sys.argv`
- Separating logic into small, well-documented functions

## What’s inside

- `api_data_explorer.py` – main script containing:
  - `get_num_facts()` – reads how many facts to fetch from the command line, defaults to 1 if the input is missing or invalid, and prints a warning for bad input.
  - `get_facts(n, url)` – calls the API `n` times, parses the JSON response, and prints each cat fact and its length. Includes error handling for request failures and JSON parsing errors.
  - `main()` – sets the API URL, gets the number of facts from the user, and coordinates the overall flow of the script.

## How to run

Use Python 3.x, and make sure the `requests` library is installed:

```bash
pip install requests
