# Research Artifacts Library

This project provides a library for generating research artifacts, such as diagrams and checklists, in a systematic and reproducible way. The goal is to create an open-source, user-friendly, and highly reproducible system for generating research artifacts suitable for academic publishing and future-proofing.

## Supported Artifacts

*   [PRISMA 2020 Flow Diagram](#prisma-2020-flow-diagram)
*   [CONSORT 2010 Flow Diagram](#consort-2010-flow-diagram)
*   [STROBE 2007 Flow Diagram](#strobe-2007-flow-diagram)
*   [CONSORT 2010 Checklist](#consort-2010-checklist)

## Getting Started

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

4.  Run the script to generate an artifact:
    ```bash
    python -m src.cli generate data/your_data.json -o your_artifact.png
    ```
    You can change the output format by changing the file extension in the output filename.

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

## Examples

### PRISMA 2020 Flow Diagram

![PRISMA Example](examples/images/prisma_example.png)

[Jupyter Notebook Example](examples/notebooks/prisma_example.ipynb)

### PRISMA 2020 Flow Diagram for Updated Reviews

![PRISMA 2020 Updated Example](examples/images/prisma_2020_updated_example.png)

[Jupyter Notebook Example](examples/notebooks/prisma_2020_updated_diagram_example.ipynb)

### CONSORT 2010 Flow Diagram

![CONSORT Example](examples/images/consort_example.png)

[Jupyter Notebook Example](examples/notebooks/consort_example.ipynb)

### CONSORT 2010 Flow Diagram for Cluster-Randomised Trials

![CONSORT Cluster Example](examples/images/consort_cluster_example.png)

[Jupyter Notebook Example](examples/notebooks/consort_cluster_diagram_example.ipynb)

### STROBE 2007 Flow Diagram

![STROBE Example](examples/images/strobe_example.png)

[Jupyter Notebook Example](examples/notebooks/strobe_example.ipynb)

### STROBE 2007 Flow Diagram for Cohort Studies

![STROBE Cohort Example](examples/images/strobe_cohort_example.png)

[Jupyter Notebook Example](examples/notebooks/strobe_cohort_diagram_example.ipynb)

### CONSORT 2010 Checklist

[Jupyter Notebook Example](examples/notebooks/consort_checklist_example.ipynb)

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
