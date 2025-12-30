def slugify(title: str) -> str:
    """
    Convert a string into a URL slug.
    """
    title = title.strip().lower()
    allowed = []
    for ch in title:
        if ch.isalnum():
            allowed.append(ch)
        elif ch in (" ", "_", "-"):
            allowed.append("-")
        # else: drop character completely
    slug = "".join(allowed)
    # collapse duplicate dashes
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug

Note: the above code was written by chatGPT

What the code does:
    - The code takes in a string called title, and converts it into URL form
    - To do this, it first removes all leading and trailing whitespace from 
      title and changes all letters to lowercase
    - It then iterates through each character of the string and keeps letters
      and digits as-is, and replaces every space, underscore and dash  with a
      dash. Every other character is dropped
    - After that it collapses any group of dashes consisting of more than one
      dash into a single dash
    - It then returns this modified string

Good aspects of the code:
    - The program logic is very easy to understand
    - All variables are appropriately named
    - Correctly handles edge cases such as title being:
        - an empty string, slugify("") = ""
        - a single character, slugify("A") = "a"
        - a single space, slugify(" ") = ""

Risky aspects of the code:
    - No method to ensure the input parameter title is a string aside from the
      type hint
    - isalnum() would even allow accented characters or other characters which
      may not be desired in a URL slug
    - The function also removes dots, so www.google.com -> wwwgooglecom, which
      may not be the desired answer

Improvements:
    - Raise a TypeError if not isinstance(title, str) at the top to ensure title
      is a string, or add a line title = str(title) instead and comment how this
      may hide a bug of title not being a string, e.g. bool -> "bool". Whichever
      method is preferred
    - Use a stricter function than isalnum() or comment how this may allow 
      unwanted characters such as accented characters for example
    - Allow dots, or comment how dots are removed and how this may lead to an
      undesired result
    - The collapsing of dashed groups could be integrated into the first for 
      loop itself. E.g. using a variable called prev_ch to see if the previous
      character was also a dash and if so not appending the current dash. This would improve the time complexity from worst case O(n^2) to worst case
      O(n) and make the code look cleaner
    - Additionally, in the final slug there may be leading and trailing dashes
      which may not be desired. Hence, depending on the problem specification, 
      these may be removed from the final slug
    - Additionally the docstring could be more specific, e.g. saying that
      leading and trailing whitespace is removed, or that all duplicate dashes
      are collapsed for example
    - Include normal tests such as:
      - "abc"
      - "www.google.com"
    - Include edge case tests such as:
      - an empty string, e.g. ""
      - a single character, e.g. "A"
      - a single space, e.g. " "

