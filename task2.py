def get_cats_info(path: str) -> list[dict[str, str]]:
    cats: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

    except (FileNotFoundError, OSError, ValueError):
        return []

    return cats
