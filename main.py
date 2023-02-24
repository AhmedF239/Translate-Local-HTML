import os
from google.cloud import translate_v2 as translate
from bs4 import BeautifulSoup


def translate_html_file(file_path, source_lang="en", target_lang="hi"):
    """Translates the text in an HTML file and saves the translated file."""
    # Load the HTML file
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Find all text elements in the HTML
    text_elements = soup.find_all(text=True)

    # Initialize the Google Translate client
    translate_client = translate.Client.from_service_account_json('google_translate_key.json')

    # Translate each text element
    for element in text_elements:
        if element.parent.name in ['style', 'script']:
            continue  # skip text inside style and script tags
        sentence = element.strip()
        if sentence:
            try:
                translated_text = translate_client.translate(sentence, source_language=source_lang, target_language=target_lang)["translatedText"]
            except Exception as e:
                print(f"An error occurred while translating: {e}")
                continue
            # Replace the original text with the translated text
            element.replace_with(translated_text)

    # Save the translated HTML file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def translate_html_directory(directory_path, source_lang="en", target_lang="hi"):
    """Translates all HTML files in a directory and its subdirectories."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                translate_html_file ( file_path , source_lang=source_lang , target_lang=target_lang )


if __name__ == "__main__":
    translate_html_directory("./Website", source_lang="en", target_lang="hi")
