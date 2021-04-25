# chrome_bookmarks
Chrome bookmarks parsing

Schrijf drie functies:

- get_url_from_dict: geeft een URL terug uit een dictionary in Google Chrome bookmarks formaat
- get_urls_from_dict: geeft een lijst met URLs terug uit een dictionary in Google Chrome bookmarks formaat (gebruik hiervoor `get_url_from_dict`)
- count_urls_from_dict: geeft het aantal URLs terug uit een dictionary in Google Chrome bookmarks formaat (gebruik hiervoor `get_urls_from_dict`)

Schrijf bijkomend een functie `get_urls_from_json` die gegeven een JSON
string een lijst met URLs geeft.

Schrijf bijkomend een functie `get_urls_from_file` die gegeven een pad naar
een Chrome bookmarks bestand, een lijst met alle URLs in dat bestand geeft.

Je bookmarks bestand vind je in `.config/google-chrome/Default/Bookmarks`
op Unix systemen, op `AppData\Local\Google\Chrome\User Data\Default\Bookmarks` op Window systemen.

Zorg dat alle testen slagen.