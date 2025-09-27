import pathlib
import re
import subprocess
import sys


def check_args(args):
    if len(args) < 2:
        raise Exception(
            "Expected at least two args with [copyright-file] [destination]"
        )
    if len(args) > 2:
        if len(args) % 2 != 0:
            raise Exception("Expected to receive values for the flags")
        if not args[2].startswith("-"):
            raise Exception("Unexpected flag placing")
        if len(args) > 4 and not args[4].startswith("-"):
            raise Exception("Unexpected flag placing")


def change_file_extension(files_to_change: list[str]):
    for file in files_to_change:
        if not len(file):
            continue

        new_file_name = pathlib.Path(file)
        while new_file_name.suffix:
            new_file_name = new_file_name.with_suffix("")

        new_file_name = f"{new_file_name}.{save_extension}"
        subprocess.run(["mv", file, new_file_name], capture_output=True, text=True)


def get_extension_comments(extension: str) -> {"start": str, "end": str}:
    COMMENT_BLOCKS = {
        ".py": {"start": '"""', "end": '"""'},
        ".cpp": {"start": "/*", "end": "*/"},
        ".h": {"start": "/*", "end": "*/"},
        ".js": {"start": "/*", "end": "*/"},
        ".java": {"start": "/*", "end": "*/"},
        ".md": {"start": "<!--", "end": "-->"},
        ".html": {"start": "<!--", "end": "-->"},
    }
    return COMMENT_BLOCKS.get(extension, {"start": "/*", "end": "*/"})


def get_extension_regex(extension: str):
    comment_schema = get_extension_comments(extension)
    return f"{comment_schema["start"]} BEGIN COPYRIGHT[\\s\\S]*?END COPYRIGHT {comment_schema["end"]}"


if __name__ == "__main__":
    args = sys.argv[1:]
    check_args(args)

    source, destination, search_extension, save_extension = None, None, None, None
    if len(args) == 2:
        source, destination = args
        # print(source, destination)
    else:
        source, destination = args[0], args[1]
        if "-c" in args:
            search_extension = args[args.index("-c") + 1]
            # print(search_extenstion)
        if "-u" in args:
            save_extension = args[args.index("-u") + 1]
        #     print(save_extenstion)
        # print(source, destination)

    # print(source, destination, search_extenstion, save_extenstion)

    copyright_content = subprocess.run(
        ["cat", source], capture_output=True, text=True
    ).stdout
    find_output = subprocess.run(
        [
            "find",
            destination,
            "-name",
            f"*.{search_extension if search_extension else "*"}",
            "-type",
            "f",
        ],
        capture_output=True,
        text=True,
    ).stdout
    files_to_check = find_output.split("\n")[:-1]

    copyright_text = f"""\"\"\" BEGIN COPYRIGHT
{copyright_content}
END COPYRIGHT \"\"\""""

    for file_path in files_to_check:
        regex = get_extension_regex(pathlib.Path(file_path).suffix)
        with open(file_path, "r") as file:
            file_content = file.read()
        copyright_blocks = re.split(regex, file_content)

        new_file_content = copyright_text.join(
            copyright_blocks
        )

        with open(file_path, "w") as file:
            file.write(new_file_content)

    if save_extension:
        change_file_extension(files_to_check)
