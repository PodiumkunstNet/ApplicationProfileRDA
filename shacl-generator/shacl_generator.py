import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import re

# Load the Excel file
file_path = "../assets/RDA-AP_Podiumkunst-net.xlsx"
excel_data = pd.ExcelFile(file_path)

# Use a set to track unique properties
unique_properties = set()
unique_property_shapes = set()

# SPARQL endpoint 
sparql_endpoint = "https://api.podiumkunst.triply.cc/datasets/rda/rda/sparql"

# SHACL Prefixes
prefixes = """prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sh: <http://www.w3.org/ns/shacl#>
prefix rdae: <http://rdaregistry.info/Elements/e/>
prefix rdac: <http://rdaregistry.info/Elements/c/>
prefix rdam: <http://rdaregistry.info/Elements/m/>
prefix rdai: <http://rdaregistry.info/Elements/i/>
prefix rdaa: <http://rdaregistry.info/Elements/a/>
prefix rdap: <http://rdaregistry.info/Elements/p/>
prefix rdaw: <http://rdaregistry.info/Elements/w/>
prefix rdat: <http://www.w3.org/2001/XMLSchema#>
prefix shp: <https://podiumkunst.triply.cc/ApplicationProfileRDA/model/shp/>
"""

# Mapping for 4 annotated sheets
sheet_mapping = {
    "Werk": {"prefix": "Work_", "node_shape": "shp:Work", "target_class": "rdac:C10001"},
    "Expressie": {"prefix": "Expression_", "node_shape": "shp:Expression", "target_class": "rdac:C10006"},
    "Manifestatie (compleet)": {"prefix": "Manifestation_", "node_shape": "shp:Manifestation", "target_class": "rdac:C10007"},
    "Item": {"prefix": "Item_", "node_shape": "shp:Item", "target_class": "rdac:C10003"}
}

# Mapping for bereik to RDA classes
bereik_mapping = {
    "werk": "rdac:C10001",
    "persoon": "rdac:C10004",
    "nomen": "rdac:C10012",
    "actor": "rdac:C10002",
    "collectieve actor": "rdac:C10011",
    "corporatie": "rdac:C10005",
    "familie": "rdac:C10008",
    "expressie": "rdac:C10006",
    "item": "rdac:C10003",
    "manifestatie": "rdac:C10007",
    "tijdspanne": "rdac:C10010",
    "plaats": "rdac:C10009"
}

# Initialize SPARQL connection
sparql = SPARQLWrapper(sparql_endpoint)

def get_rdfs_label(property_uri):
    query = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix rdae: <http://rdaregistry.info/Elements/e/>
    prefix rdac: <http://rdaregistry.info/Elements/c/>
    prefix rdam: <http://rdaregistry.info/Elements/m/>
    prefix rdai: <http://rdaregistry.info/Elements/i/>
    prefix rdaa: <http://rdaregistry.info/Elements/a/>
    prefix rdap: <http://rdaregistry.info/Elements/p/>
    prefix rdaw: <http://rdaregistry.info/Elements/w/>
    SELECT ?label WHERE {{
        {property_uri} rdfs:label ?label .
        FILTER(lang(?label) = 'en')
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    # If label found, return it; otherwise, return the URI as a fallback
    if results["results"]["bindings"]:
        return results["results"]["bindings"][0]["label"]["value"]
    else:
        return property_uri 

def to_camel_case(label):
    # Convert label to camelCase
    label = re.sub(r'[^a-zA-Z0-9 ]', '', label)
    words = label.split()
    camel_case = words[0].lower() + ''.join(word.title() for word in words[1:])
    return camel_case

def create_property_shape(row, sheet_name):
    # Check if 'verplichting' and has a valid value or is empty
    if row['verplichting'] not in ['must', 'should', 'could'] and not pd.isna(row['verplichting']):
        return ""
    
    if not row['RDA Registry curie'].startswith('rda'):
        return ''
    
    # Get the RDA Registry curie (URI) and retrieve the rdfs:label via SPARQL
    property_uri = row['RDA Registry curie']
    label = get_rdfs_label(property_uri)
    
    # Convert label to camelCase
    camel_case_label = to_camel_case(label)
    
    # Generate shape name using the camelCase label
    shape_name = f"shp:{sheet_mapping[sheet_name]['prefix']}{camel_case_label}"

    # Check if the property shape has already been generated
    if shape_name in unique_property_shapes:
        return ""

    # Add the property shape to the set to mark it as processed
    unique_property_shapes.add(shape_name)

    # minCount only if 'verplichting' is "must"
    min_count = f"sh:minCount 1;" if row['verplichting'] == "must" else ""

    # maxCount only if 'max' is exactly 1
    max_count = f"sh:maxCount 1;" if row.get('max') == 1 else ""

    #sh:class 
    range = f"sh:class {bereik_mapping[row.get('bereik')]};" if row.get('bereik') in bereik_mapping  else ""

    severity = "sh:Violation" if row['verplichting'] == "must" else "sh:Warning"

    # Only return property shape if it has valid components
    if property_uri and severity:
        return f"""
{shape_name}
    a sh:PropertyShape;
    {min_count}
    {max_count}
    {range}
    sh:path {property_uri};
    sh:severity {severity}.
    """
    return ""

def create_node_shape(sheet_name, df):
    df.columns = df.columns.str.strip()

    # Generate property shapes, avoiding duplicates
    property_shapes = []
    for _, row in df.iterrows():
        if (row['verplichting'] in ['must', 'should', 'could'] or pd.isna(row['verplichting'])) and row['RDA Registry curie'].startswith('rda'):
            property_label = to_camel_case(get_rdfs_label(row['RDA Registry curie']))
            property_shape = f"shp:{sheet_mapping[sheet_name]['prefix']}{property_label}"

            if property_shape not in unique_properties:
                unique_properties.add(property_shape)
                property_shapes.append(f"        {property_shape}")

    # Format the property shapes: separate by comma, but end the last one with a semicolon
    if property_shapes:
        property_shapes_formatted = ",\n".join(property_shapes[:-1]) + (",\n" if len(property_shapes) > 1 else "") + property_shapes[-1] + ";"
    else:
        property_shapes_formatted = ""

    target_class = sheet_mapping[sheet_name]['target_class']

    return f"""
{sheet_mapping[sheet_name]['node_shape']}
    a sh:NodeShape;
    sh:closed true ;
	sh:ignoredProperties (rdf:type) ;
    sh:property
{property_shapes_formatted}
    sh:targetClass {target_class}.
"""

def generate_shacl():
    shacl_output = [prefixes]
    for sheet_name in excel_data.sheet_names:
        if sheet_name in sheet_mapping.keys():
            print(f"Processing {sheet_name}")
            df = excel_data.parse(sheet_name)
            node_shape = create_node_shape(sheet_name, df)
            property_shapes = "\n\n".join([create_property_shape(row, sheet_name) for _, row in df.iterrows()])
            # Remove empty property shapes to avoid blank lines
            property_shapes = "\n".join([shape for shape in property_shapes.splitlines() if shape.strip()])
            
            # Only add non-empty node shape or property shapes
            if node_shape.strip() or property_shapes.strip():  # Only add if not empty
                shacl_output.append(node_shape)
                shacl_output.append(property_shapes)
    
    return "\n".join(shacl_output)
    

# Generate SHACL content
shacl_content = generate_shacl()

# Save to file
with open("../assets/RDA-AP_Podiumkunst-net-SHACL.ttl", "w") as file:
    file.write(shacl_content)
