from typing import Any


def is_valid_grid(
    width: int | None, height: int | None, config_data: dict[str, Any]
) -> bool:
    if width is None or height is None:
        print("Error: WIDTH and HEIGHT must be defined in config.txt")
        return False

    if width <= 1 or height <= 1:
        print("Error: height or width must be greater than 1")
        return False

    if width < 8 or height < 6:
        print("Error: The maze size does not allow the 42 pattern")
        config_data["42"] = False
    else:
        config_data["42"] = True

    for key in ["entry", "exit"]:
        if key in config_data:
            x, y = config_data[key]
            if not (0 <= x < width and 0 <= y < height):
                print(
                    f"Error: {
                        key.upper()} {
                        x,
                        y} is out of maze boundaries.")
                return False
    return True


def assign_key_value(key: str, value: str,
                     config_data: dict[str, Any]) -> bool:
    try:
        match key:
            case "WIDTH":
                config_data["width"] = int(value)
            case "HEIGHT":
                config_data["height"] = int(value)
            case "ENTRY" | "EXIT":
                parts = value.split(",")
                if len(parts) != 2:
                    print(
                        f"Error: {key} "
                        "must contain exactly two coordinates (x,y)."
                    )
                    return False
                coords = tuple(int(n) for n in parts)
                config_data[key.lower()] = coords
            case "OUTPUT_FILE":
                if value != "maze.txt":
                    print("The OUTPUT_FILE must be 'maze.txt'.")
                    return False
                config_data["output_file"] = value
            case "PERFECT":
                if value.lower() not in ["true", "false"]:
                    print("The PERFECT value must be 'true' or 'false'.")
                    return False
                config_data["perfect"] = value.lower() == "true"
            case _:
                print(f"Error: Unknown key '{key}' found in config.txt.")
                return False
    except ValueError as e:
        print(f"Error: {e}")

    return True


def is_all_keys_required(config_data: dict[str, Any]) -> bool:
    required_keys = [
        "width",
        "height",
        "entry",
        "exit",
        "perfect",
        "output_file"]
    for req in required_keys:
        if req not in config_data:
            print(f"Error: Missing required configuration key: {req.upper()}")
            return False
    return True


def parsing_config_data(file_name: str) -> dict[str, Any] | None:
    """Parses the configuration file and returns a dictionary of settings."""
    if file_name != "config.txt":
        print("Invalid filename. Expected 'config.txt'.")
        return None

    config_data: dict[str, Any] = {}
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    print("Invalid format. Missing '=' in line: " + line)
                    return None
                if " " in line:
                    print(f"Format Error: Spaces are not allowed in '{line}'")
                    return None
                (key, _, value) = line.partition("=")
                if not assign_key_value(key, value, config_data):
                    return None

    except FileNotFoundError:
        print(
            f"Error: The file '{file_name}' "
            "was not found in the current directory."
        )
        return None
    except PermissionError:
        print(f"Error: You do not have permission to read '{file_name}'.")
        return None

    if not is_all_keys_required(config_data):
        return None

    width = config_data.get("width")
    height = config_data.get("height")

    if not is_valid_grid(width, height, config_data):
        return None

    return config_data
