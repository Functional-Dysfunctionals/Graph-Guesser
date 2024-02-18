import backend
import sys

def print_to_html(Alist):
    myfile = open('public/output.html', 'w')
    html_template = """
    <html>
    <head></head>
    <body>
        <p>{}</p>
    </body>
    </html>
    """

    title = "The type of equation is..."
    myfile.write(html_template.format(title))

    for newL in Alist:
        message = ', '.join(newL)
        myfile.write(html_template.format(message))

    myfile.close()

# Example data
# Alist = [
#     ['123', 'user1', 'New Compressed (zipped) Folder.zip', '05-24-17'],
#     ['123', 'user2', 'Iam.zip', '05-19-17'],
#     ['abcd', 'Letsee.zip', '05-22-17'],
#     ['Here', 'whichTwo.zip', '06-01-17']
# ]
    
Alist = [[backend.getTypes()]]

print_to_html(Alist)

print('sup')