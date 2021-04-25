from .bookmarks.bookmarks_json import get_urls_from_json


def test_get_urls_from_simplified_bookmarks_json():
    """Test that the function returns the URLs from a simplified JSON Chrome
    bookmarks string"""
    info = """{
        "roots": {
            "bookmark_bar": {
                "children": [
                    {"url": "https://tweakers.net/"},
                    {"url": "https://www.reddit.com/"}
                ]
            }
        }
    }"""

    result = get_urls_from_json(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
    ]
    assert result == expected


def test_get_urls_from_bookmarks_json():
    """Test that the function returns the URLs from a full JSON Chrome
    bookmarks string"""
    info = """{
        "checksum": "3d915f8847b6204002a07d3e0ca6e3ba",
        "roots": {
            "bookmark_bar": {
                "children": [
                    {
                        "id": "6",
                        "name": "Tweakers-Wij stellen technologie op de proef",
                        "type": "url",
                        "url": "https://tweakers.net/"
                    },
                    {
                        "id": "8",
                        "name": "reddit: the front page of the internet",
                        "type": "url",
                        "url": "https://www.reddit.com/"
                    }
                ],
                "id": "1",
                "name": "Bookmarkbalk",
                "type": "folder"
            },
            "other": {
                "children": [],
                "id": "2",
                "name": "Andere bookmarks",
                "type": "folder"
            },
            "synced": {
                "children": [],
                "id": "3",
                "name": "Mobiele bookmarks",
                "type": "folder"
            }
        },
        "version": 1
    }"""

    result = get_urls_from_json(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
    ]
    assert result == expected
