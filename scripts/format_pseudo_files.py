"""
https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters
add in global settings of vscode
  copy the file format_pseudo_files.py to your root of workspace folder
  updated vscode settings with below register
  "customLocalFormatters.formatters": [
    {
      "command": "python format_pseudo_files.py",
      "languages": ["pseudo"]
    }
  ]
  usage: VSCode's formatter features lets you quickly format code through the Format Document command (shift+alt+f) or automatically on save with the editor.formatOnSave option.
"""
import sys


class var:
    open_loop_count = 0


def format_line(contents):
    open_loop_keywords = ["IF", "CASE", "FOR",
                          "WHILE", "ELSE", "ELSIF", "WHEN"]
    close_loop_keyword = ["ENDIF", "ENDCASE",
                          "ENDFOR", "ENDWHILE", "ELSE", "ELSIF", "WHEN"]
    alignement = "    "

    if len(contents.strip()) > 0:
        line_text = contents.strip()
        line_words = line_text.split(" ")
        # print line_words[0]
        if (line_words[0] in close_loop_keyword) and (var.open_loop_count > 0):
            var.open_loop_count = var.open_loop_count - 1

        space_str = "{}".format(alignement * var.open_loop_count)

        if (line_words[0] in open_loop_keywords):
            var.open_loop_count = var.open_loop_count + 1

        contents = "{}{}".format(space_str, contents.strip())
        print(contents)
        # editor.replaceLine(lineNumber, contents)


def main(argv):

    for line in sys.stdin:
        format_line(line)
        # print(line.strip())


if __name__ == "__main__":
    main(sys.argv[1:])
