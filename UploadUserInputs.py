from clarifai.client.user import User
client = User(user_id="qj7itgikynyv", pat="f85f784cf89946078344980521f17f0d")

from clarifai.client.user import User
app = User(user_id="qj7itgikynyv").app(app_id="my-first-application-i7adqk")
input_obj = app.inputs()



#input upload from url
input_obj.upload_from_url(input_id = 'demo2', image_url='https://source.unsplash.com/random/200x200?sig=2')

# #input upload from filename
# input_obj.upload_from_file(input_id = 'demo', video_file='demo.mp4')

# add a tag to the images
input_generator = input_obj.list_inputs(page_no=1,per_page=10,input_type='image')
inputs_list = list(input_generator)


# top part is good and working
# need to change input_id and image_url everytime you run this script


