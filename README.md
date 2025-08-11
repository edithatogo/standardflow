# Research Artifacts Library

This project provides a library for generating research artifacts, such as diagrams and checklists, in a systematic and reproducible way. The goal is to create an open-source, user-friendly, and highly reproducible system for generating research artifacts suitable for academic publishing and future-proofing.

## Supported Artifacts

*   [PRISMA 2020 Flow Diagram](#prisma-2020-flow-diagram)
*   [PRISMA 2020 Flow Diagram for Updated Reviews](#prisma-2020-flow-diagram-for-updated-reviews)
*   [CONSORT 2010 Flow Diagram](#consort-2010-flow-diagram)
*   [CONSORT 2010 Flow Diagram for Cluster-Randomised Trials](#consort-2010-flow-diagram-for-cluster-randomised-trials)
*   [STROBE 2007 Flow Diagram](#strobe-2007-flow-diagram)
*   [STROBE 2007 Flow Diagram for Cohort Studies](#strobe-2007-flow-diagram-for-cohort-studies)
*   [CONSORT 2010 Checklist](#consort-2010-checklist)
*   [STROBE 2007 Checklist for Cohort Studies](#strobe-2007-checklist-for-cohort-studies)
*   [STROBE 2007 Checklist for Case-Control Studies](#strobe-2007-checklist-for-case-control-studies)
*   [STROBE 2007 Checklist for Cross-Sectional Studies](#strobe-2007-checklist-for-cross-sectional-studies)

## Getting Started

### With Docker

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/research-artifacts-library.git
    ```
2.  Build and run the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```
3.  Open your web browser and navigate to `http://localhost:5000`.

### Without Docker

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/research-artifacts-library.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    You will also need to install Graphviz and ImageMagick. On Debian-based systems, you can do this with:
    ```bash
    sudo apt-get update && sudo apt-get install -y graphviz imagemagick
    ```

3.  Create a JSON file with your data. See the `data` directory for examples.

For more details on using the command-line interface, see the [CLI Usage](#cli-usage) section.

## CLI Usage

The command-line interface provides a powerful way to interact with this library.

### `generate`

The `generate` command is used to create a diagram or checklist from a JSON data file.

**Usage:**
```bash
python -m src.cli generate [OPTIONS] INPUT
```

**Arguments:**
*   `INPUT`: The path to the JSON data file.

**Options:**
*   `-o, --output TEXT`: The output file name. The format is inferred from the extension.
*   `-s, --style PATH`: Path to a JSON file with styling information.
*   `--set TEXT`: Set a key-value pair in the data, e.g., `--set randomized=999`. Can be used multiple times.
*   `--interactive`: Run in interactive mode to be prompted for data.

**Example:**
```bash
python -m src.cli generate examples/data/consort_data.json -o consort.png --set randomized=999
```

### `validate`

The `validate` command is used to validate a JSON data file against the appropriate schema.

**Usage:**
```bash
python -m src.cli validate INPUT
```

**Arguments:**
*   `INPUT`: The path to the JSON data file to validate.

### `list`

The `list` command lists the available diagram and checklist types.

**Usage:**
```bash
python -m src.cli list
```

### `schemas`

The `schemas` command lists available schemas or prints a specific schema.

**Usage:**
```bash
# List all schemas
python -m src.cli schemas

# Print a specific schema
python -m src.cli schemas CONSORT
```

## Styling

You can customize the appearance of the diagrams by adding a `style` object to your JSON data file. The `style` object can contain the following properties:

*   `box_color`: The background color of the boxes.
*   `font_color`: The color of the text in the boxes.
*   `font_name`: The name of the font to use for the text.
*   `font_size`: The size of the font to use for the text.
*   `arrow_color`: The color of the arrows.

Here is an example of a JSON file with styling information:

```json
{
    "diagram_type": "PRISMA",
    "records_identified": 1000,
    "records_after_duplicates_removed": 800,
    "records_screened": 800,
    "records_excluded": 200,
    "full_text_articles_assessed": 600,
    "full_text_articles_excluded": 300,
    "studies_included": 300,
    "style": {
        "box_color": "lightblue",
        "font_color": "darkblue",
        "font_name": "Arial",
        "font_size": "12",
        "arrow_color": "darkblue"
    }
}
```

This will produce the following diagram:

![Styled PRISMA Example](examples/images/styled_prisma.png)

## Output Formats

This library supports generating diagrams in the following formats:

*   **PNG:** A raster image format.
*   **SVG:** A vector image format, suitable for high-quality publications and web use.
*   **PDF:** A portable document format, useful for sharing and printing.
*   **Typst:** A modern typesetting system. This will generate a `.typ` file that includes an SVG of the diagram.

You can specify the output format by using the appropriate file extension in the output filename when using the CLI. For example:

```bash
# Generate a PNG
python -m src.cli generate data/your_data.json -o your_artifact.png

# Generate an SVG
python -m src.cli generate data/your_data.json -o your_artifact.svg

# Generate a PDF
python -m src.cli generate data/your_data.json -o your_artifact.pdf

# Generate a Typst file
python -m src.cli generate data/your_data.json -o your_artifact.typ
```

## Examples

### PRISMA 2020 Flow Diagram

![PRISMA Example](examples/images/prisma_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/prisma_example.ipynb)

### PRISMA 2020 Flow Diagram for Updated Reviews

![PRISMA 2020 Updated Example](examples/images/prisma_2020_updated_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/prisma_2020_updated_diagram_example.ipynb)

### CONSORT 2010 Flow Diagram

![CONSORT Example](examples/images/consort_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/consort_example.ipynb)

### CONSORT 2010 Flow Diagram for Cluster-Randomised Trials

![CONSORT Cluster Example](examples/images/consort_cluster_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/consort_cluster_diagram_example.ipynb)

### STROBE 2007 Flow Diagram

![STROBE Example](examples/images/strobe_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/strobe_example.ipynb)

### STROBE 2007 Flow Diagram for Cohort Studies

![STROBE Cohort Example](examples/images/strobe_cohort_diagram_example.png)

[Jupyter Notebook Example](examples/notebooks/strobe_cohort_diagram_example.ipynb)

### CONSORT 2010 Checklist

[Jupyter Notebook Example](examples/notebooks/consort_checklist_example.ipynb)

### STROBE 2007 Checklist for Cohort Studies

[Jupyter Notebook Example](examples/notebooks/strobe_cohort_checklist_example.ipynb)

### STROBE 2007 Checklist for Case-Control Studies

[Jupyter Notebook Example](examples/notebooks/strobe_case_control_checklist_example.ipynb)

### STROBE 2007 Checklist for Cross-Sectional Studies

[Jupyter Notebook Example](examples/notebooks/strobe_cross_sectional_checklist_example.ipynb)

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
