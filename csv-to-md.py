import csv

def csv_to_markdown(csv_file, md_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("CSV file is empty.")
        return

    # Create Markdown header
    header = rows[0]
    md_table = ['| ' + ' | '.join(header) + ' |']
    md_table.append('|' + '|'.join([' --- ' for _ in header]) + '|')

    # Add table rows
    for row in rows[1:]:
        md_table.append('| ' + ' | '.join(row) + ' |')

    # Write to Markdown file
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_table))

    print(f"Markdown table saved to {md_file}")

# Example usage
csv_to_markdown('service-names-port-numbers.csv', 'output.md')
