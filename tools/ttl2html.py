import sys
from rdflib import Graph

def turtle_to_html(input_turtle, output_html):
    with open(input_turtle, "r", encoding="utf-8") as turtle_file:
        turtle_data = turtle_file.read()

    # Write the Turtle data to the output file as HTML
    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write("<pre>\n")
        html_file.write(turtle_data)
        html_file.write("\n</pre>")

if __name__ == "__main__":
    # Check if both input and output files are provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input.ttl output.html")
        sys.exit(1)

    # Get input and output file names from command-line arguments
    input_turtle = sys.argv[1]
    output_html = sys.argv[2]

    turtle_to_html(input_turtle, output_html)
