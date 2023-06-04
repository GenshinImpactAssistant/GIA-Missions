Work flow:

- 'missions' in the .json file should not be modified manually.
  - It can only be modified by workflow.
  - See "check_index_modifications.py"
- Validate the py file in the missions folder.
  - META variable should be defined.
  - META variable should contain 'name' field.
  - META variable should contain 'author' field.
    - 'author' field should be a string like 'author1, author2' (Check manually)
    - Previous author should be kept. (Check manually)
  - Check the data type of each field in META variable.
  - See "validate_mission_file.py"
- Generate the json file.
  - Generate multi language json files.
  - If the mission is created first time, 'create-time' field will be added.
  - If the mission is updated, 'update-time' field will be updated.
  - The timezone is UTC for time fields.
  - Update other fields according to the META in py file.
  - See"generate_index.py"