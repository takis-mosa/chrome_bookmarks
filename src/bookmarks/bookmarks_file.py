import json

from .bookmarks_dict import get_urls_from_dict


def get_urls_from_file(s):
    """Return a list of URLs from a Chrome bookmarks file

    s -- a string containing a path to the Chrome bookmarks file
    """
    return []

if __name__ == "__main__":
    urls = get_urls_from_file("$HOME/.config/google-chrome/Default/Bookmarks")
    print(urls)
