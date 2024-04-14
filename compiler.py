import argparse
import re
def compile(file_path):
    # Read the content of the .gxml file
    with open(file_path, 'r') as file:
        gui_code = file.read()

    # Define regex patterns to match various tags
    div_pattern = r'<div>(.*?)</div>'
    scroll_pattern = r'<scroll>(.*?)</scroll>'
    list_pattern = r'<list>(.*?)</list>'
    data_pattern = r'<data>(.*?)</data>'
    style_pattern = r'<style>(.*?)</style>'
    script_pattern = r'<script>(.*?)</script>'
    plain_pattern = r'<plain>(.*?)</plain>'
    bold_pattern = r'<bold>(.*?)</bold>'
    image_pattern = r'<image\s+src="([^"]+)"\s*>'

    # Replace various tags with their corresponding HTML elements
    html_code = re.sub(div_pattern, r'<div>\1</div>', gui_code)
    html_code = re.sub(scroll_pattern, r'<scroll>\1</scroll>', html_code)
    html_code = re.sub(list_pattern, r'<list>\1</list>', html_code)
    html_code = re.sub(data_pattern, r'<data>\1</data>', html_code)
    html_code = re.sub(style_pattern, r'<style>\1</style>', html_code)
    html_code = re.sub(script_pattern, r'<script>\1</script>', html_code)
    html_code = re.sub(plain_pattern, r'<p>\1</p>', html_code)
    html_code = re.sub(bold_pattern, r'<strong>\1</strong>', html_code)
    html_code = re.sub(image_pattern, r'<img src="\1">', html_code)
    
    return html_code

def main():
    parser = argparse.ArgumentParser(description='Compile Project GUI (.gxml) files to HTML.')
    parser.add_argument('file_path', metavar='FILE', type=str, help='Path to the .gxml file')
    args = parser.parse_args()

    file_path = args.file_path
    html_code = compile(file_path)
    print(html_code)

if __name__ == "__main__":
    main()
