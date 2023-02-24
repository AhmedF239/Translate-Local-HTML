# Translate-Local-HTML
Translated multiple local HTML files in different subdirectories then replaced the original text in the original files while maintaining the formatting and style

The code uses the Beautiful Soup library to parse HTML files and extract all text elements from the HTML. It then uses the Google Cloud Translation API to translate each text element from a specified source language to a specified target language.

The translated text is then inserted back into the HTML in place of the original text. The translated HTML files are then saved in the same directory as the original files.

The code defines two functions: translate_html_file() and translate_html_directory().

The translate_html_file() function takes a file path to an HTML file, and optionally a source and target language. It loads the HTML file using BeautifulSoup, finds all the text elements, translates them using the Google Cloud Translation API, and replaces the original text with the translated text. Finally, it saves the translated HTML file.

The translate_html_directory() function takes a directory path, and optionally a source and target language. It calls the translate_html_file() function on every HTML file in the specified directory and its subdirectories.

The main code block calls translate_html_directory() on a specified directory, using the default source and target languages if none are provided.

You can assess a live version of the translated website through https://classcentral-in-hindi.web.app
