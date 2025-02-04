# SHACL Shapes Generator

This script is designed to generate SHACL shapes from a given Excel file containing metadata definitions. 
It leverages SPARQL to query an endpoint for additional information and produces a SHACL file [RDA-AP_Podiumkunst-net-SHACL.ttl](../assets/RDA-AP_Podiumkunst-net-SHACL.ttl) as output.

## Prerequisites

- Python 3.8 or higher
- Install required dependencies using the `requirements.txt` file.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/shacl-generator.git
   cd shacl-generator
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script
   ``` bash
   python shacl_generator.py
   ```

4. Output will be saved as [RDA-AP_Podiumkunst-net-SHACL.ttl](../assets/RDA-AP_Podiumkunst-net-SHACL.ttl) in `assets` folder. 


## Shacl Generator
The input Excel file should have multiple sheets, each representing a different category of metadata (e.g., Werk, Expressie, Manifestatie). 

* Validation: Skips rows invalid `verplichting` values.

* SPARQL Query: Retrieves the `rdfs:label` for the property URI and converts it to camelCase for the shape name.

* Avoid Duplicates: Checks if the property shape is already processed using a unique_property_shapes set.

* Constraints:
   * Adds `sh:minCount` if `verplichting` is must.
   * Adds `sh:maxCount` if the max value is `1`.
   * Adds `sh:class` if a valid `bereik` mapping exists.
   * Severity: Sets `sh:Violation` for `must` and `sh:Warning` otherwise.
   * All node shapes are closed. We allow properties  `verplichting` to be empty or has values `must`, `should` and `could`. 
* Output: Returns the formatted SHACL property shape.
