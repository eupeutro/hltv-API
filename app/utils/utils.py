import re
from typing import Optional , Union

def trim(text: Union[list, str]) -> str:
    """
    Trims the input text by removing extra spaces and special characters like non-breaking spaces.

    Args:
        text (Union[list, str]): The text to be trimmed. It can be a list or a string.

    Returns:
        str: The trimmed text.
    """

    if isinstance(text, list):
        text = "".join(text)
    
    return text.strip().replace("\xa0", "")

import re
from typing import Optional

def extract_from_url(hltv_url: Optional[str], element: str) -> Optional[str]:
    """
    Extracts specific elements (like player ID or nickname) from a given HLTV URL using regex.

    Args:
        hltv_url (Optional[str]): The HLTV profile URL to extract information from.
        element (str): The element to extract from the URL (e.g., "id", "nickname").

    Returns:
        Optional[str]: The extracted value, or None if the element cannot be found.
    """
    if not hltv_url:
        return None
    
   
    regex = (
        r"(?:https?://(?:www\.)?hltv\.org)?" 
        r"/player/(?P<id>\d+)"
        r"(?:/(?P<nickname>[\w\-]+))?"
    )
    
    
    match = re.match(regex, hltv_url)
    

    return match.groupdict().get(element) if match else None


def extract_nickname_from_name(full_name: str) -> Optional[str]:
    """
    Extracts the nickname from a player's full name enclosed in single quotes.

    Args:
        full_name (str): The full name of the player.

    Returns:
        Optional[str]: The extracted nickname, or None if not found.
    """
    match = re.search(r"'([^']+)'", full_name)
    return match.group(1) if match else None


def extract_country_name_from_flag_url(flag_url: str) -> Optional[str]:
    """
    Extracts the country name based on the flag URL from HLTV.

    Args:
        flag_url (str): The URL of the flag image.

    Returns:
        Optional[str]: The country name associated with the flag, or None if not found.
    """
    country_names = {"AE":"United Arab Emirates","AF":"Afghanistan","AL":"Albania","AM":"Armenia","AO":"Angola","AR":"Argentina","AS":"American Samoa","AT":"Austria","AU":"Australia","AW":"Aruba","AX":"Åland Islands","AZ":"Azerbaijan","BA":"Bosnia and Herzegovina","BB":"Barbados","BD":"Bangladesh","BE":"Belgium","BF":"Burkina Faso","BG":"Bulgaria","BH":"Bahrain","BI":"Burundi","BJ":"Benin","BM":"Bermuda","BN":"Brunei","BO":"Bolivia","BR":"Brazil","BS":"Bahamas","BT":"Bhutan","BW":"Botswana","BY":"Belarus","BZ":"Belize","CA":"Canada","CD":"Democratic Republic of the Congo","CF":"Central African Republic","CG":"Congo","CH":"Switzerland","CI":"Ivory Coast","CL":"Chile","CM":"Cameroon","CN":"China","CO":"Colombia","CR":"Costa Rica","CU":"Cuba","CV":"Cape Verde","CY":"Cyprus","CZ":"Czech Republic","DE":"Germany","DK":"Denmark","DO":"Dominican Republic","DZ":"Algeria","EC":"Ecuador","EE":"Estonia","EG":"Egypt","ES":"Spain","ET":"Ethiopia","FI":"Finland","FJ":"Fiji","FR":"France","GA":"Gabon","GB":"United Kingdom","GE":"Georgia","GH":"Ghana","GL":"Greenland","GM":"Gambia","GN":"Guinea","GR":"Greece","GT":"Guatemala","GU":"Guam","GW":"Guinea-Bissau","GY":"Guyana","HK":"Hong Kong","HN":"Honduras","HR":"Croatia","HT":"Haiti","HU":"Hungary","ID":"Indonesia","IE":"Ireland","IL":"Israel","IN":"India","IQ":"Iraq","IR":"Iran","IS":"Iceland","IT":"Italy","JM":"Jamaica","JO":"Jordan","JP":"Japan","KE":"Kenya","KG":"Kyrgyzstan","KH":"Cambodia","KR":"South Korea","KW":"Kuwait","KZ":"Kazakhstan","LA":"Laos","LB":"Lebanon","LK":"Sri Lanka","LR":"Liberia","LS":"Lesotho","LT":"Lithuania","LU":"Luxembourg","LV":"Latvia","LY":"Libya","MA":"Morocco","MC":"Monaco","MD":"Moldova","ME":"Montenegro","MG":"Madagascar","MK":"North Macedonia","ML":"Mali","MM":"Myanmar","MN":"Mongolia","MO":"Macau","MR":"Mauritania","MT":"Malta","MU":"Mauritius","MV":"Maldives","MW":"Malawi","MX":"Mexico","MY":"Malaysia","MZ":"Mozambique","NA":"Namibia","NE":"Niger","NG":"Nigeria","NI":"Nicaragua","NL":"Netherlands","NO":"Norway","NP":"Nepal","NZ":"New Zealand","OM":"Oman","PA":"Panama","PE":"Peru","PG":"Papua New Guinea","PH":"Philippines","PK":"Pakistan","PL":"Poland","PT":"Portugal","PY":"Paraguay","QA":"Qatar","RO":"Romania","RS":"Serbia","RU":"Russia","RW":"Rwanda","SA":"Saudi Arabia","SE":"Sweden","SG":"Singapore","SI":"Slovenia","SK":"Slovakia","SN":"Senegal","SO":"Somalia","SY":"Syria","TH":"Thailand","TJ":"Tajikistan","TL":"East Timor","TN":"Tunisia","TR":"Turkey","TT":"Trinidad and Tobago","TW":"Taiwan","TZ":"Tanzania","UA":"Ukraine","UG":"Uganda","US":"United States","UY":"Uruguay","UZ":"Uzbekistan","VE":"Venezuela","VN":"Vietnam","YE":"Yemen","ZA":"South Africa","ZM":"Zambia","ZW":"Zimbabwe"}
    match = re.search(r'/([A-Z]{2})\.gif$',flag_url)

    if match:
        country_code = match.group(1)
        return country_names.get(country_code, country_code)
    return None

def extract_age (age_str: str) -> Optional[int]:
    """
    Extracts the numeric age from a string in the format 'XX years'.

    Args:
        age_str (str): The age string in the format 'XX years' (e.g., '28 years').

    Returns:
        Optional[int]: The extracted age as an integer, or None if the extraction fails.
    """
    if age_str: 
        match=re.match(r"(\d+)\s+years", age_str)
        if match:
            return int(match.group(1))

    return None