# Equator Network Resource Library

This project aims to re-create, systematize, and expand upon the resources available on the [Equator Network website](https://www.equator-network.org/), with a focus on diagrams (e.g., PRISMA) and checklists. The ultimate goal is to create an open-source, user-friendly, and highly reproducible system for generating research artifacts suitable for academic publishing and future-proofing.

## Phase 1: Core Diagram Generation (Python First)

This is the initial phase of the project, focusing on generating PRISMA diagrams using Python.

### Current Features

*   Generate PRISMA 2020 flow diagrams from a JSON input file.
*   Supported output formats: PNG, SVG, PDF, TIFF, and EPS.
*   A Python script (`src/prisma.py`) to generate diagrams from the command line.
*   A Jupyter notebook (`notebooks/PRISMA_Diagram_Generator.ipynb`) for interactive diagram generation.
*   A comprehensive test suite to ensure the reliability of the diagram generation.

### Getting Started

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/equator-network-resources.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    You will also need to install Graphviz and ImageMagick. On Debian-based systems, you can do this with:
    ```bash
    sudo apt-get update && sudo apt-get install -y graphviz imagemagick
    ```

3.  Create a JSON file with your PRISMA data (e.g., `data/my_prisma_data.json`):
    ```json
    {
        "records_identified": 1000,
        "records_after_duplicates_removed": 800,
        "records_screened": 800,
        "records_excluded": 200,
        "full_text_articles_assessed": 600,
        "full_text_articles_excluded": 300,
        "studies_included": 300
    }
    ```

4.  Run the script to generate a diagram:
    ```bash
    python src/prisma.py data/my_prisma_data.json -o my_prisma_diagram.png
    ```
    You can change the output format by changing the file extension in the output filename.

5.  Explore the Jupyter notebook in the `notebooks` directory for an interactive example.

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
