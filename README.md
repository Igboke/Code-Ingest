# Code Ingest: Local Codebase Aggregator

## 🚀 Overview

Code Ingest is a simple, yet powerful Python command-line utility that recursively traverses your local directory structure, reads the contents of specified files, and consolidates them into a single, comprehensive text file. This tool is invaluable for tasks where providing a large context of your codebase is beneficial, such as:

- Feeding your entire project to AI tools for better debugging, refactoring, or documentation generation.
- Creating a portable snapshot of your codebase for review or archival.
- Generating a consolidated text representation for analysis or search.

Unlike tools that require syncing with remote repositories (like GitHub), Code Ingest operates entirely locally, ensuring your code remains private and under your control.  

## ✨ Features

- Local Traversal: Recursively navigates through directories from a specified source path.
- Content Aggregation: Merges the content of all relevant files into a single .txt output.
- Configurable Exclusions: Easily skip directories (e.g., .git, node_modules) and file extensions (e.g., .png, .pyc, .pdf).
- File Size Limiting: Automatically skips very large files to prevent performance issues and irrelevant content.
- Standalone Script: Requires no external pip installations, relying solely on Python's standard library.
- Clear Output: Formats the output file with clear delimiters, indicating the path of each included file.

## 💡 Why Code Ingest?

In an AI-driven development environment, providing comprehensive context to tools is paramount. While powerful IDEs and cloud services exist, many developers prefer to maintain their existing workflows and keep their code local.

Code Ingest was inspired by the need for a local equivalent to tools like `gitingest`, allowing you to prepare your codebase for AI analysis without uploading it to a version control system. It addresses the common challenge of providing a holistic view of your project to AI without compromising privacy or forcing changes to your preferred development setup.

## Prerequisites

- Python 3.8+
- Git

## 🛠️ Installation

Code Ingest is a single Python script and requires no special installation.

Clone the repository:

```bash
git clone https://github.com/Igboke/Code-Ingest.git
cd Code-Ingest
```

Or, simply download the code_ingest.py script to a directory.

## 🏃 Usage

Navigate to the directory where code_ingest.py is located

### Basic Usage

To process the current directory and save the output to output.txt:

```bash
python code_ingest.py
```

### Specifying Source Directory and Output File

You can provide a specific source directory and custom output filename:

```bash
python code_ingest.py --source /path/to/your/project --output my_project_dump.txt
# Or using shorthand:
python code_ingest.py -s /path/to/your/project -o my_project_dump.txt
```

### Excluding Directories and File Extensions

Customize which directories and file types to ignore. Separate multiple items with spaces.

```bash
# Exclude 'docs' and 'temp' directories, and '.log' and '.csv' files
python code_ingest.py -s . -e docs temp -x .log .csv
```

### Setting a Maximum File Size

Skip files larger than a specified size (in KB):

```bash
# Process files up to 2MB (2048 KB)
python code_ingest.py -s . -m 2048
```

### Viewing All Options

To see a list of all available arguments and their descriptions:

```bash
python code_ingest.py --help
```

## ⚙️ Configuration (Default Exclusions)

By default, Code Ingest intelligently skips common development-related directories and non-text file extensions to ensure your output is clean and relevant.

Default Excluded Directories (-e / --exclude-dirs):

- .git
- __pycache__
- .venv
- venv
- node_modules
- dist
- build
- .vscode
- .idea

Default Excluded Extensions (-x / --exclude-extensions):

- .pyc
- .bin, .exe
- .zip, .tar, .gz
- .jpg, .jpeg, .png, .gif, .bmp
- .mp4, .mov, .avi
- .pdf, .docx, .xlsx, .pptx
- .sqlite3, .db
- .DS_Store
- .log

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Get in Touch / Support

Have questions, found a bug, or want to suggest a new feature? I'd love to hear from you!

- __Email:__ [Igboke Daniel](mailto:danieligboke669@gmail.com)

- __GitHub Issues:__ Feel free to [open an issue](https://github.com/Igboke/Code-Ingest/issues) on this repository.
