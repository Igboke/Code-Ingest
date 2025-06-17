import argparse
import os


def parse_arguments():
    """Parses command-line arguments for source directory, output file, and exclusions."""
    parser = argparse.ArgumentParser(
        description="Recursively copies content of files in a directory structure to a single text file."
    )
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        default=".",  # Default to current directory
        help="The source directory to traverse. Defaults to the current directory.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.txt",  # Default output filename
        help="The name of the output text file. Defaults to 'output.txt'.",
    )
    parser.add_argument(
        "-e",
        "--exclude-dirs",
        nargs="*",  # Allows zero or more arguments
        default=[
            ".git",
            "__pycache__",
            ".venv",
            "node_modules",
            "dist",
            "build",
            ".vscode",
            ".idea",
            "venv",
        ],  # Common exclusions
        help="List of directory names to exclude from traversal (e.g., .git __pycache__). Defaults to common development directories.",
    )
    parser.add_argument(
        "-x",
        "--exclude-extensions",
        nargs="*",
        default=[
            ".pyc",
            ".bin",
            ".exe",
            ".zip",
            ".tar",
            ".gz",
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".mp4",
            ".mov",
            ".avi",
            ".pdf",
            ".docx",
            ".xlsx",
            ".pptx",
            ".sqlite3",
            ".db",
            ".DS_Store",
            ".log",
        ],  # Common binary/non-text extensions
        help="List of file extensions to exclude from content aggregation (e.g., .pyc .log). Defaults to common binary/media/document extensions.",
    )
    parser.add_argument(
        "-m",
        "--max-file-size-kb",
        type=int,
        default=1024,  # 1MB default
        help="Maximum file size in KB to include. Files larger than this will be skipped. Defaults to 1024KB (1MB).",
    )
    args = parser.parse_args()
    return args


def read_file_content(file_path: str) -> str | None:
    """
    Reads the content of a file, attempting different encodings if necessary.
    Returns content string or None if unreadable.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    except UnicodeDecodeError:
        # Fallback to a more lenient encoding, or ignore errors
        try:
            with open(file_path, "r", encoding="latin-1") as f:  # Common fallback
                content = f.read()
                return content
        except Exception as e:
            # If latin-1 also fails, try with errors='ignore' as a last resort
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    print(
                        f"  Warning: Read {file_path} with UTF-8 errors ignored. Content might be corrupted."
                    )
                    return content
            except Exception as e:
                print(f"  Error reading {file_path}: {e}. Skipping.")
                return None
    except Exception as e:
        print(f"  Error reading {file_path}: {e}. Skipping.")
        return None


def traverse_and_collect_files(
    source_dir: str,
    exclude_dirs: list[str],
    exclude_extensions: list[str],
    max_file_size_bytes: int,
) -> list[str]:
    """
    Traverses the directory, applies filters, and collects paths of files to process.
    """
    collected_files = []
    print(f"Starting traversal from: {os.path.abspath(source_dir)}")

    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Pruning directories: Modify dirnames in place to prevent os.walk from entering them.
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # Check if file should be excluded by extension
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in [ext.lower() for ext in exclude_extensions]:
                # print(f"  Skipping (extension): {file_path}")
                continue

            # Check file size
            try:
                file_size = os.path.getsize(file_path)
                if file_size > max_file_size_bytes:
                    print(
                        f"  Skipping (size > {max_file_size_bytes/1024:.2f}KB): {file_path}"
                    )
                    continue
            except OSError as e:
                print(f"  Error checking file size for {file_path}: {e}. Skipping.")
                continue  # Skip if we can't even get size

            # If it passes all checks, add to our list
            collected_files.append(file_path)
    return collected_files


def write_to_output_file(
    output_file_path: str, collected_files: list[str], source_dir: str
) -> None:
    """
    Writes the content of collected files to the specified output file.
    """
    # Ensure parent directories exist for the output file
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")
        except OSError as e:
            print(f"Error creating output directory {output_dir}: {e}. Aborting write.")
            return

    total_files_processed = 0
    total_content_size_bytes = 0

    print(f"Writing content to: {os.path.abspath(output_file_path)}")
    try:
        # Use 'w' mode to ensure a fresh file each run
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            for file_path in collected_files:
                relative_path = os.path.relpath(
                    file_path, start=source_dir
                )  # Path relative to source_dir
                content = read_file_content(file_path)

                if content is not None:
                    # Add a clear separator and file path
                    outfile.write(f"\n\n--- FILE: {relative_path} ---\n\n")
                    outfile.write(content)
                    total_files_processed += 1
                    total_content_size_bytes += len(
                        content.encode("utf-8")
                    )  # Calculate size in bytes
                else:
                    print(f"  Skipped (unreadable content): {relative_path}")

        print(f"\n--- Aggregation Complete ---")
        print(f"Total files processed: {total_files_processed}")
        print(
            f"Total aggregated content size: {total_content_size_bytes / (1024*1024):.2f} MB"
        )
        print(f"Output saved to: {os.path.abspath(output_file_path)}")

    except IOError as e:
        print(f"Error writing to output file {output_file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during writing: {e}")


if __name__ == "__main__":
    args = parse_arguments()

    source_dir = os.path.abspath(args.source)
    output_file_path = args.output
    exclude_dirs = args.exclude_dirs
    exclude_extensions = args.exclude_extensions
    max_file_size_bytes = args.max_file_size_kb * 1024  # Convert KB to bytes

    # Validate source directory
    if not os.path.isdir(source_dir):
        print(
            f"Error: Source directory '{source_dir}' does not exist or is not a directory."
        )
        exit(1)  # Exit with an error code

    print(f"\n--- Configuration ---")
    print(f"Source: {source_dir}")
    print(f"Output: {output_file_path}")
    print(f"Exclude Dirs: {exclude_dirs}")
    print(f"Exclude Extensions: {exclude_extensions}")
    print(f"Max File Size: {args.max_file_size_kb} KB")
    print(f"---------------------\n")

    files_to_process = traverse_and_collect_files(
        source_dir, exclude_dirs, exclude_extensions, max_file_size_bytes
    )
    write_to_output_file(output_file_path, files_to_process, source_dir)
