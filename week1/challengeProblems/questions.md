Challenge 1: Compute 1000!
In one of the problems in the previous section, you were asked to write a function that computes the factorial of a number. However, that function is only good for relatively small numbers. Factorials have a tendency to grow extremely rapidly such even 20! is more than 2 billion billion!

Even the most powerful supercomputer in the world will not be able to compute 1000! the normal way. The number is enormous; it has close to 2500 digits!

Your first challenge is to figure out a clever way to compute this number anyway.

Hint: If you had to compute this by hand, it wouldn't be that difficult. You would probably need a few hours and a really, really long piece of paper. Can you write a program that mimics multiplication by hand?

Challenge 2: Create an xkcd comic book
xkcd is one of my favorite webcomics of all time. Created by Randall Munroe, it tends to cover topics related to programming, math, philosophy, and culture.

xkcd comics are available for free online. For this challenge, you have to write a script that downloads every xkcd comic strip ever created and converted into a PDF book (for personal consumption, of course).

This task will require the usage of Python packages like requests so feel free to Google and discover what you might need.

Challenge 3: Find the astronaut Scrappy Squirrels
Before Scrappy Project, our team worked on an NFT education project called Scrappy Squirrels. As part of this project, we had created over 14,000 squirrels generatively. You've already seen a lot of those squirrels in our logos and slides.

Each squirrel has a unique combination of expression, fur, background, and clothes. For this challenge, your task is to identify the IDs of all squirrels that wear an astronaut suit among the first 2000 squirrels.

Each squirrel has a JSON file associated with it. For instance, Scrappy Squirrel #1's JSON can be found at https://scrappyart.s3.ap-south-1.amazonaws.com/json/1. Similarly, Scrappy Squirrel #2000 can be found at https://scrappyart.s3.ap-south-1.amazonaws.com/json/5000.

If you visit this URL on a broswer, you should get output that looks something like this:

{"name": "Scrappy Squirrel #250", "description": "Scrappy Squirrels is a collection of 14,000 NFTs on the Ethereum blockchain. Scrappy Squirrels are meant for engineers, designers, and entrepreneurs pushing web3 forward.", "image": "https://scrappyart.s3.ap-south-1.amazonaws.com/images/00250.png", "attributes": [{"trait_type": "Background", "value": "Cyan"}, {"trait_type": "Body", "value": "Purple"}, {"trait_type": "Expressions", "value": "Winking"}, {"trait_type": "Clothes", "value": "Floral Print OverShirt"}]}
This is something called a JSON file. Notice how similar it is to a Python dictionary.
More importantly, it seems to have information on what clothes it is wearing.

You now need to figure out how to write a script that accesses these 2000 JSON files, parse it into a Python dictionary, and then determine if the squirrel is wearing an astronaut suit.

While you're at it, go ahead and claim a squirrel to be your study group's mascot!

