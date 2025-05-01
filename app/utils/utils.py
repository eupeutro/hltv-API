import re
from typing import Optional , Union

def trim(text: Union[list, str]) -> str:

    if isinstance(text, list):
        text = "".join(text)
    
    return text.strip().replace("\xa0", "")

def extract_from_url(hltv_url: Optional[str], element: str) -> Optional[str]:
   if not hltv_url:
     return None
   regex = (
        r"(?:https?://(?:www\.)?hltv\.org)?"
        r"/player/(?P<id>\d+)"
        r"(?:/(?P<nickname>[\w\-]+))?"
    )
   match = re.match(regex,hltv_url)
   return match.groupdict().get(element) if match else None

def extract_nickname_from_name(full_name: str) -> Optional[str]:
    match = re.search(r"'([^']+)'", full_name)
    return match.group(1) if match else None