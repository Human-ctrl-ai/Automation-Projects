import re
import pyperclip
import pdfplumber 

def phone_number_extractor(text):
    pattern = re.compile(r''' (?<![\w+]) (?: \+1 [\s\-\.]? (?:\(\d{3}\)|\d{3}) [\s\-\.]? \d{3} [\s\-\.]? \d{4} (?:\s?(?:ext\.?|x)\s?\d{1,5})? | \+91 [\s\-]? [6-9]\d{4} [\s\-]? \d{5} | \+34 [\s\-]? [6789]\d{2} (?:[\s\-]?\d{2}){3} | \+44 [\s\-]? (?:\(\d{2,4}\)|\d{2,4}) [\s\-]? \d{3,4} [\s\-]? \d{3,4} | \+82 [\s\-]? 10 [\s\-]? \d{4} [\s\-]? \d{4} | \+55 [\s\-]? (?:\(\d{2}\)|\d{2}) [\s\-]? 9\d{4} [\s\-]? \d{4} | \+46 [\s\-]? 7\d [\s\-]? \d{3} [\s\-]? \d{2} [\s\-]? \d{2} | \+971 [\s\-]? 5\d [\s\-]? \d{3} [\s\-]? \d{4} | \+33 [\s\-]? [67] (?:[\s\-]?\d{2}){4} | \+81 [\s\-]? \d{2} [\s\-]? \d{4} [\s\-]? \d{4} ) (?![\w-]) ''', re.VERBOSE)

    # Find all phone numbers
    matches = pattern.findall(text)

    # Print results
    for number in set(matches):
        print("Phone number :", number)
    print()
    
    return 0

def email_extractor(text):
    email_pattern = re.compile(r''' (?<![\w\.-]) [a-zA-Z0-9._%+-]+ @ [a-zA-Z0-9.-]+ \.[a-zA-Z]{2,} (?![\w.-]) ''', re.VERBOSE)

    # Find all phone numbers
    matches = email_pattern.findall(text)

    # Print results
    for email in set(matches):
        print("Email ID :", email)
    print()
    
    return 0

def clipboard_matcher(text):          
    # Read clipboard content(s)
    clipboard_text = pyperclip.paste()
    
    # Normalize whitespace(s)
    text = text.strip()
    clipboard_text = clipboard_text.strip()
    
    # Compare and Execute
    if clipboard_text not in text: print("Clipboard content NOT found in file.")
    else:
        print("Clipboard Text :", clipboard_text)
    print()
    
    return 0

def insta_handle_extractor(text):
    handle_pattern = re.compile(
        r'(?<!\w)@[A-Za-z0-9](?:[A-Za-z0-9._]{0,28}[A-Za-z0-9_])?'
    )

    # Find all phone numbers
    matches = handle_pattern.findall(text)

    # Print results
    for handle in set(matches):
        print("Insta Handle :", handle)
    print() 
    
    return 0

def linkedin_profile_extractor(text):
    profile_link_pattern = re.compile(
        r'https?:\/\/(?:www\.)?linkedin\.com\/(?:in|company|school)\/[A-Za-z0-9-_%]+\/?',
    re.IGNORECASE
)

    # Find all phone numbers
    matches = profile_link_pattern.findall(text)

    # Print results
    for link in set(matches):
        print("LinkedIN profile :", link)
    print()
    
    return 0

def github_profile_extractor(text):
    profile_link_pattern = re.compile(
    r'https?:\/\/(?:www\.)?github\.com\/(?!.*--)[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',
    re.IGNORECASE
)

    # Find all phone numbers
    matches = profile_link_pattern.findall(text)

    # Print results
    for link in set(matches):
        print("GitHUB profile :", link)
    print()
    
    return 0

def github_repo_extractor(text):
    profile_repo_pattern = re.compile(r'https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/)?')

    # Find all phone numbers
    matches = profile_repo_pattern.findall(text)

    # Print results
    for repo in set(matches):
        print("GitHUB REPO :", repo)
    print()
    
    return 0

def export_chat_extractor(text):
    chat_pattern = re.compile(r'^(\d{2}/\d{2}/\d{2}),\s(\d{2}:\d{2})\s-\s([^:]+):\s([\s\S]*?)(?=^\d{2}/\d{2}/\d{2},\s\d{2}:\d{2}\s-\s|\Z)', re.MULTILINE)
        
    matches = chat_pattern.findall(text)

    print('Exported Text : \n')
    for date, time, sender, message in matches:
        print("DATE:", date)
        print("TIME:", time)
        print("SENDER:", sender)
        print("MESSAGE:", message[:80])
        print("-" * 40)
    
    return 0

# main 
f = input("Enter file name : ")
text = ""

if f.endswith(".txt"):
    with open(f, 'r', encoding="utf-8") as file:
        text = file.read()
        phone_number_extractor(text)
        email_extractor(text)
        clipboard_matcher(text)
        insta_handle_extractor(text)
        linkedin_profile_extractor(text)
        github_profile_extractor(text)
        github_repo_extractor(text)
        export_chat_extractor(text)
        
elif f.endswith(".pdf"):
    with pdfplumber.open(f) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
                
    phone_number_extractor(text)
    email_extractor(text)
    clipboard_matcher(text)
    insta_handle_extractor(text)
    linkedin_profile_extractor(text)
    github_profile_extractor(text)
    github_repo_extractor(text)
    export_chat_extractor(text)
    
else:
    print("Unsupported file format :(")

   
        





