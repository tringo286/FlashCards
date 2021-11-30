import markdown

class Render():

    """
    This class Renders files into html text
    
    Attributes:
    ----------
    file: Takes a file and uses markdown to render a .md file into html
    

    Function:
    ---------
    render(): opens the .md file and converts it to html
    """


    def render(file):
        file = file
        with open(file , 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
        return html
