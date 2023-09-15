# YAML to Bootstrap cards

This utility reads structured data from YAML and puts them into a trivial Bootstrap template using the cards feature.

Run the utility by running this command:

```bash
python load_yaml.py filename columns_max
```

- substitute the _filename_ with the name of the YAML file (don't include the file extension)
- substitute the _columns_max_ with the maximum number of cards you want in one row

## YAML file structure

In the YAML file there is list. Each item represents one card. Each item in the list is a dictionary where the key represents the term in an html definiton list a the value represent the definition. There are two exceptions: value with the key `_name_` is displayed as a card header and `_image_` is an url poining on an image display above the card. See the `example.yaml` and `example.html` files.
