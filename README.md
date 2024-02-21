

<h2>About the project</h2>

<p>
## Inspiration
We wanted to do something with ai, and we decided to do something with image recognition.

## What it does
The user is able to draw a graph however they desire, and when they click the guess button we use clarifai to compare the graph to a dataset we generated, and then we show the user which function is most likely to be theirs.

## How we built it
We first spent a while researching a free image comparasion ai with an api compatible with python. We then built the frontend in python and then converted it to a webapp. Also using python, we generated a dataset of graphs with random offsets to mimic the offsets the user will most likely put. Clarifai then compares the graph to the dataset and gives us a list of which function the graph is most likely to be, and we present that to the user.

## Challenges we ran into
Our model was giving us completely wrong answers at first, and we would sometimes get no response at all. We also struggled to get the web app to communicate with clarifai, which ate most of our time.

## Accomplishments that we're proud of
Succesfully made a full stack app that utilizes ai and image comparison, while having no prior experience in that field before.

## What we learned
Learned more about Node.JS, how to use git commands, the process of pushing and pulling code, and broadened our understanding of AI. 

## What's next for Graph Guesser
Currently, the code is very hard coded to be only run on a local machine, so we plan to eventually make it so any user can download it and use it anywhere.

</p>

<h3>Build with:</h3>

» AI <br>
» ClarifAI <br>
» CSS3 <br>
» HTML5 <br>
» Python <br>
» PYQT5 <br>
» Node.JS

