# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    guidesdoc/
        docs/
            index.md  # The documentation homepage.
            classes-function.md   # Show all classes and functions.
    myapp/
        templates/
            ...                   # contain all html files
        text/                     # contain all file text
            Test.md
        upload/                   # contain all file upload
            Test.md
            Test1.md
        __init__.py               # Set up flask and import library server
        app.db                    # File database
        forms.py                  # Use for storing a wtf forming implementation
        models.py                 # Design object models interacting database
        render.py                 # Interact with files by markdown
        routes.py                 # Controller
    .gitignore
    run.py                        # Run the website homepage
    Specification.md              # All use cases
