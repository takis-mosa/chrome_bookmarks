from io import StringIO

from .bookmarks.bookmarks_file import get_urls_from_file


def test_get_urls_from_bookmarks_file():
    """Test that a list of URLs is returned from a Chrome bookmarks file"""
    info = StringIO(
        """{
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
    )

    result = get_urls_from_file(info)
    expected = [
        "https://tweakers.net/",
        "https://www.reddit.com/",
    ]
    assert result == expected
