def extract_markdown_definitions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    definitions = []
    for line in lines:
        # Strip leading and trailing whitespace
        stripped_line = line.strip()
        # Check if the line starts with '>'
        if stripped_line.startswith('>'):
            if len(stripped_line) == 1:
                continue
            definitions.append(stripped_line[1:].strip())  # Remove '>' and leading whitespace
            #definitions.append('\n')  

    return definitions

def main():
    # Replace 'your_file.md' with the path to your Markdown file
    file_path = r'season-01\06 The One With the Butt\index.md'
    definitions = extract_markdown_definitions(file_path)
    
    # Write the extracted definitions to Vocabulary.txt
    count = 0
    with open('Vocabulary.txt', 'w', encoding='utf-8') as output_file:
        for definition in definitions:
            count += 1
            output_file.write(str(count) + '. ' + definition + '\n\n')

    print("success")

if __name__ == "__main__":
    main()