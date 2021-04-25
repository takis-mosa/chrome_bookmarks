from .bookmarks.bookmarks_dict import (
    count_urls_from_dict,
    get_url_from_dict,
    get_urls_from_dict,
)


def test_get_tweakers_url_from_dict():
    """Test that the function returns the URL"""
    info = {
        "url": "https://tweakers.net/",
    }
    result = get_url_from_dict(info)
    expected = "https://tweakers.net/"
    assert result == expected


def test_get_pyside_url_from_dict():
    """Test that the function returns another URL"""
    info = {
        "url": "http://www.pyside.org/",
    }
    result = get_url_from_dict(info)
    expected = "http://www.pyside.org/"
    assert result == expected


def test_get_url_from_simplified_dict():
    """Test that the function returns the URL"""
    info = {"id": "6", "type": "url", "url": "https://tweakers.net/"}
    result = get_url_from_dict(info)
    expected = "https://tweakers.net/"
    assert result == expected


def test_get_url_from_booksmarks_dict():
    """Test that the function returns the URL"""
    info = {
        "id": "2294",
        "name": "JavaScript Guide - JavaScript | MDN",
        "type": "url",
        "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
    }
    result = get_url_from_dict(info)
    expected = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
    assert result == expected


def test_get_urls_from_simplified_bookmarks_dict():
    """Test that the function returns the URLs from a simplified Chrome
    booksmarks structure"""
    info = {
        "roots": {
            "bookmark_bar": {
                "children": [
                    {"url": "https://tweakers.net/"},
                    {"url": "https://www.reddit.com/"},
                ],
            },
        },
    }

    result = get_urls_from_dict(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
    ]
    assert result == expected


def test_get_urls_from_simple_bookmarks_dict():
    """Test that the function returns the URLs from a slightly simplified
    Chrome booksmarks structure"""
    info = {
        "roots": {
            "bookmark_bar": {
                "children": [
                    {"url": "https://tweakers.net/"},
                    {"url": "https://www.reddit.com/"},
                    {"url": "https://store.steampowered.com/"},
                ],
                "name": "Bookmarkbalk",
                "type": "folder",
            },
        },
        "version": 1,
    }

    result = get_urls_from_dict(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
        "https://store.steampowered.com/",
    ]
    assert result == expected


def test_count_urls_from_dict():
    """Test that the function counts the number of URLs in a Chrome
    booksmarks structure"""
    info = {
        "roots": {
            "bookmark_bar": {
                "children": [
                    {"url": "https://tweakers.net/"},
                    {"url": "https://www.reddit.com/"},
                    {"url": "https://store.steampowered.com/"},
                ],
                "name": "Bookmarkbalk",
                "type": "folder",
            },
        },
        "version": 1,
    }

    result = count_urls_from_dict(info)
    expected = 3
    assert result == expected


def test_get_urls_from_bookmarks_dict():
    """Test that the function counts the number of URLs in a full Chrome
    booksmarks structure"""
    info = {
        "checksum": "3d915f8847b6204002a07d3e0ca6e3ba",
        "roots": {
            "bookmark_bar": {
                "children": [
                    {
                        "id": "6",
                        "name": "Tweakers-Wij stellen technologie op de proef",
                        "type": "url",
                        "url": "https://tweakers.net/",
                    },
                    {
                        "id": "8",
                        "name": "reddit: the front page of the internet",
                        "type": "url",
                        "url": "https://www.reddit.com/",
                    },
                ],
                "id": "1",
                "name": "Bookmarkbalk",
                "type": "folder",
            },
            "other": {
                "children": [],
                "id": "2",
                "name": "Andere bookmarks",
                "type": "folder",
            },
            "synced": {
                "children": [],
                "id": "3",
                "name": "Mobiele bookmarks",
                "type": "folder",
            },
        },
        "version": 1,
    }

    result = get_urls_from_dict(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
    ]
    assert result == expected
