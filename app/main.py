def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:

    return {"errors": [{"line": item["line_number"],
                        "column": item["column_number"],
                        "message": item["text"], "name": item["code"],
                        "source": "flake8"}
                       for item in errors], "path": file_path,
            "status": "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [{"line": error["line_number"],
                         "column": error["column_number"],
                         "message": error["text"], "name": error["code"],
                         "source": "flake8"}
                        for error in errors], "path": path,
             "status": "failed" if errors else "passed"}
            for path, errors in linter_report.items()]
