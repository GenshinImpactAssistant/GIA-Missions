from util import *
import ast

def operation(
    *,
    path_in: Path,
) -> None:
    print("Validating mission file {}".format(path_in))

    with open(path_in, "rb") as f:
        source = f.read()
    
    # Parse the source code
    module = ast.parse(source)

    # Check if the source code contains a META variable
    meta_value = None
    for node in module.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and node.targets[0].id == 'META':
            meta_value = ast.literal_eval(node.value)
            break
    assert meta_value is not None, "META variable should be defined in the mission source code."
    
    # Check if META is a dict
    assert isinstance(meta_value, dict), "META variable should be a dict."
    
    # Check the type of the values
    string_keys = ['name', 'author', 'description', 'note']
    list_keys = ['tags']
    for key, value in meta_value.items():
        if isinstance(value, dict):
            for inside_value in value.values():
                if key in string_keys:
                    assert isinstance(inside_value, str), f"Values of key '{key}' should be a string."
                if key in list_keys:
                    assert isinstance(inside_value, list), f"Values of key '{key}' should be a list."
        else:
            if key in string_keys:
                assert isinstance(value, str), f"Values of key '{key}' should be a string."
            if key in list_keys:
                assert isinstance(value, list), f"Values of key '{key}' should be a list."
    
    # Check if the required keys are present
    required_keys = ['name', 'author']
    for key in required_keys:
        assert key in meta_value, f"Required key '{key}' is missing in META variable."
        value = meta_value[key]
        if isinstance(value, dict):
            assert len(value) > 0, f"Values of key '{key}' should not be empty."
            for inside_value in value.values():
                assert len(inside_value) > 0, f"Values of key '{key}' should not be empty."
        else:
            assert len(value) > 0, f"Values of key '{key}' should not be empty."
    
    # author should be a string (not a dict or list)
    assert isinstance(meta_value['author'], str), f"Values of key 'author' should be a string."

def main() -> None:
    opts = get_opts()
    for opt in opts.input:
        operation(
            path_in=Path(opt),
        )

if __name__ == "__main__":
    main()