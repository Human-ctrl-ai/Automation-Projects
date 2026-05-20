import re
import pyperclip

def phone_number_extractor(f):
    pattern = re.compile(r''' (?<![\w+]) (?: \+1 [\s\-\.]? (?:\(\d{3}\)|\d{3}) [\s\-\.]? \d{3} [\s\-\.]? \d{4} (?:\s?(?:ext\.?|x)\s?\d{1,5})? | \+91 [\s\-]? [6-9]\d{4} [\s\-]? \d{5} | \+34 [\s\-]? [6789]\d{2} (?:[\s\-]?\d{2}){3} | \+44 [\s\-]? (?:\(\d{2,4}\)|\d{2,4}) [\s\-]? \d{3,4} [\s\-]? \d{3,4} | \+82 [\s\-]? 10 [\s\-]? \d{4} [\s\-]? \d{4} | \+55 [\s\-]? (?:\(\d{2}\)|\d{2}) [\s\-]? 9\d{4} [\s\-]? \d{4} | \+46 [\s\-]? 7\d [\s\-]? \d{3} [\s\-]? \d{2} [\s\-]? \d{2} | \+971 [\s\-]? 5\d [\s\-]? \d{3} [\s\-]? \d{4} | \+33 [\s\-]? [67] (?:[\s\-]?\d{2}){4} | \+81 [\s\-]? \d{2} [\s\-]? \d{4} [\s\-]? \d{4} ) (?![\w-]) ''', re.VERBOSE)

    # Read text from file
    with open(f, 'r', encoding="utf-8") as file:
        text = file.read()

    # Find all phone numbers
    matches = pattern.findall(text)

    # Print results
    for number in matches:
        print("Phone number:", number)
        
    return 0

def email_extractor(f):
    email_pattern = re.compile(r''' (?<![\w\.-]) [a-zA-Z0-9._%+-]+ @ [a-zA-Z0-9.-]+ \.[a-zA-Z]{2,} (?![\w.-]) ''', re.VERBOSE)

    # Read text from file
    with open(f, 'r', encoding="utf-8") as file:
        text = file.read()

    # Find all phone numbers
    matches = email_pattern.findall(text)

    # Print results
    for name in matches:
        print("Email ID:", name)
        
    return 0

def clipboard_matcher(f):
    # Read file content(s)
    with open(f, 'r', encoding="utf-8") as file:
        file_text = file.read()
        
    # Read clipboard content(s)
    clipboard_text = pyperclip.paste()
    
    # Normalize whitespace(s)
    file_text = file_text.strip()
    clipboard_text = clipboard_text.strip()
    
    # Compare and Execute
    if clipboard_text not in file_text: print("Clipboard content NOT found in file.")
    else:
        print("Clipboard Text:", clipboard_text)
    return 0

# main 
f = 'test.txt'
phone_number_extractor(f)
email_extractor(f)
clipboard_matcher(f)

