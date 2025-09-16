import subprocess
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
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

    copyright_text = subprocess.run(
        ["cat", source], capture_output=True, text=True
    ).stdout
    files_to_check = subprocess.run(
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
    print(copyright_text)
    print(files_to_check)
