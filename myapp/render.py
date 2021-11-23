import markdown

class Render():
    
    def render(file):
        file = file
        with open(file , 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
        return html