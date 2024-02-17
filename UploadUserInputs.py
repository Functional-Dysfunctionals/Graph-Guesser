from clarifai.client.user import User
client = User(user_id="qj7itgikynyv", pat="f85f784cf89946078344980521f17f0d")

from clarifai.client.user import User
app = User(user_id="qj7itgikynyv").app(app_id="my-first-application-i7adqk")
input_obj = app.inputs()

from AddInputsToDataset import setToUserInput
import string
from random import choice
# from keyword gets the function from the file

# make a random id
def make_random():
    """
    Generates a random string of 5 characters using letters and digits.
    """
    return ''.join([choice(string.ascii_letters + string.digits) for _ in range(5)])

# #input upload from url
# input_obj.upload_from_url(input_id = 'demo2', image_url='https://source.unsplash.com/random/200x200?sig=2')


#input upload from filename 
current_id = make_random()
input_obj.upload_from_file(input_id = current_id, image_file='output_image.png')
# add input to user-inputs dataset
setToUserInput(current_id)

'''# add a tag to the images
input_generator = input_obj.list_inputs(page_no=1,per_page=10,input_type='image')
inputs_list = list(input_generator)'''


# need to change input_id everytime you run this script


