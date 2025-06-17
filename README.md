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

