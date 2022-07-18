# Training on Testing

As data scientists, we're used to splitting training and testing data, to evaluate the performance of our models.
Recently, I had the opportunity to put those two words together in quite a different way,
when I prepared and led an internal training session on an entirely different, 
but highly important, technique: **Unit Testing**.

## The importance of unit testing
Unit testing involves writing automated test code to verify the behaviour of small 'units' of code, such as a Python function,
against specific inputs and conditions. As a data scientist writing a lot of Python code in my daily work, the benefits are as follows:

* Finding bugs: perhaps the most obvious, by writing unit tests I uncover bugs in code, especially under test cases.
* Structuring: by aiming to write unit tests, I must first structure my code into small, testable units.
* Avoiding regression: a suite of unit tests provides assurance that code changes have not broken existing working code;
  furthermore a colleague can refactor my code with a degree of confidence that functionality has been preserved.
* Test-driven development: by considering and writing unit tests before embarking on the code itself, I clarify and document
  my expectations the code's functionality in advance, helping to keep my thinking clear and focussed.


## Running the session
At Bays Consulting, we have the privilege of a weekly Learning & Development hour, 
when normal project work pauses for an opportunity to hone our skills.
We alternate each week between an independent, self-guided study slot,
and a group learning session where one member of the company will present a topic of interest to the rest of the team.

When my turn came round, and I had chosen the subject of unit testing, I was keen to make the experience
as hands-on and practical as possible for the participants, while keeping in mind the range of per-existing skills on the team.

Unit testing lends itself to an exercise in pair programming I have seen referred to as Adversarial Test Driven Development.
At a high level, developers take it in turns to write a minimal unit test to describe some intended functionality, 
or highlight an edge case.
Their partner then should make a minimal update to the main code that gets the tests to pass.
When applied in its most pure form, especially in a training context,
that update could be pedantically minimal, for example simply writing a function
to return a constant value to match the unit test's expectation, regardless of the inputs. 
This should ensure that the set of unit tests becomes as complete as possible, to overcome such trivialities,
while forcing an explicit and conscious articulation of requirements.

I was keen to give this exercise a go, so after a few slides of introduction, outlining the benefits of unit testing described above,
I split participants into pairs and set them to work pair programming.

### Technical set up
When planning the session, I was aware that I should prepare for a full range of technical and non-technical staff 
from the company to join, including colleagues who do not code on a daily basis,
and so it was critical to keep the complexity of technical requirements to a minimum.

I therefore chose to use *Visual Studio Code* as the Integrated Development Environment for the exercise,
as not only does it already have strong adoption within the company, but also for its collaboration features.

I installed the [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) extension, 
and so was able to invite a pair of participants into a pre-prepared workspace,
including all required Python packages, testing extensions, and example code 
(see [bays_training](bays_training) and [tests](tests)). 
I could then leave the pair to it, while keeping an eye on their progress and jumping in with prompts if required.

The beauty of this approach was that those without any development tools installed could join the collaboration
entirely within the browser, while those who were regular VS Code users could install the extension and join that way.

To take pressure of my own laptop, I created a workspace for the exercise on an EC2 instance (virtual machine)
in the Amazon Web Services cloud. I could thus dedicate a couple of CPU cores to each pair while only paying a dollar or so
for the hour-long exercise. I accessed the workspace using 
the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension.

Once the workspace was set up exactly how I wanted it, I used Git to initialise a repository for the workspace,
committing the code files and also VS Code's configuration. I could then very quickly make a copy of the workspace
for each pair, simply by running the `git clone` command.

### Pairing up
To maximise chances of success, I asked participants to RSVP and then worked out the pairings in advance. 
In doing so, I balanced two in some ways contradictory aims. 

On the one hand, it was important that each pair had at least one participant with Python experience, so that some
headway could be made. On the other hand, a pair with matched skill levels might be more effective and engaged at the
'ping-pong' nature of the Adversarial TDD.

Finally, one complication arose that I had not anticipated: an odd number of participants!

## Reflections
In principle, I believe it worked well to run this as a hands-on exercise.
Not only did it seem to capture the attention of the participants, but it allowed knowledge to be shared within the pairs
without any additional input from me.

Although the remote workspaces successfully allowed all participants to get into the coding environment, 
there were a few technical hiccups.

Firstly, for some reason the Test Explorer (beaker icon) was not available in the Live Share,
which was disappointing as this provides a clear and satisfying way to run a suite of unit tests and validate that they pass.
We were able to work around by running `pytest` in the VS Code Terminal.

Secondly, some team members found the real time collaboration to be flaky, with file contents not properly syncing.
Curiously, this seemed to be worse when joining via the VS Code application instead of the browser. 
We were generally able to work around by terminating the Live Share session and restarting all VS Code windows;
in other words "turning it off and on again"!

Thirdly, a learning point for me. Once we had broken into pairs, I encouraged each pair to communicate directly via
a Teams call if they were working remotely. I then had to message them if I wanted to break in and see how they were getting on.
In retrospect, it would have been more slick to use pre-arranged Teams break out rooms.

## Conclusion
I very much enjoyed preparing and delivering the training, and I hope my colleagues enjoyed too.
The true measure of success will be an increase in uptake and breadth of unit testing in our day to day work, 
which I shall be looking out for eagerly.
