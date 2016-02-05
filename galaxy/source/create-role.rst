Create a Role

Requirements:
GitHub account
git installed (We’ll use the command-line version.)
ansible 2.0 or greater installed
cowsay installed (Optional. Install if you like cows.)

What you’ll learn: 
How to create and execute a basic Ansible role and some best practices to follow as you create your own roles.


For our example we’ll create the universal Hello World app in the form of a role called role-hello-world.
Create a GitHub Repository
Before we get into the details of creating a role, let’s first create a new GitHub repo for our role. If you’re unfamiliar with creating a repository on GitHub, see Create a Repo. Name the repo role-hello-world. Leave the ‘Initialize repository with a README’ option unchecked. Leave the .gitignore option empty (we’ll add our own). And if this is a public repo, choose a license.

Next, create a local copy of the new repository. Replace the URL in the following command with the URL for your repository:

$ git clone https://username@github.com/username/role-hello-world.git

The above creates a folder named ‘role-hello-world’ containing some git configuration items and a license file, if you added one. 

Create Role Scaffolding
Using the ansible-galaxy command that comes bundled with Ansible, we’ll execute the init command to add some initial scaffolding to our role-hello-world folder. We’ll also include the --force option, telling it to ignore the fact that role-hello-world already exists. From the same directory where you ran the command to create the local copy of the repository,run the following:

$ ansible-galaxy init role-hello-world --force

Ansible-galaxy added the following to our role-hello-world folder:

.. IMAGE HERE ..

Here’s a quick summary for each component of an Ansible role:


- .travis.yml -- When you are ready to test your role, this file can be used to start integration testing with Travis-CI.
- README.md -- Documentation that helps others use your role.
- defaults/main.yml -- Defaults for role variables.
- files -- Files needed by your role that cannot be represented in a template. 
- handlers/main.yml -- Define handlers that respond to task notification.
- meta/main.yml -- Add a list of any roles this role depends on, and provide metadata when sharing the role on Galaxy.
- tasks/main.yml -- The actual work the role will perform.
- templates -- jinja2 templates used by the role
- tests -- Files referenced in .travis.yml to perform a simple test against the role.
- var/main.yml -- Define additional variables with higher priority than defaults/main.yml.

For our purposes we’ll focus on the basics needed to get our role functioning.

Add Tasks
Let’s begin by adding a task to tasks/main.yml. This is the Ansible playbook containing the actual work or tasks the role will perform. Open tasks/main.yml and add the following:

- name: Say Hello
  debug: var=hello_world_message

In our task we’re using the debug module to display the contents of variable hello_world_message to stdout.

Define Variables
Now we need to set the value of the variable hello_world_message. We’ll do this in defaults/main.yml, where we list all the variables used in the role and provide each with a default value. Add the following line to defaults/main.yml:

hello_world_message: Hi!

Create a Playbook
To run our role we’ll need a playbook. In the parent folder to role-hello-world create a new file called hello.yml. This will be our playbook. Add the following lines to hello.yml:

- hosts: all
  connection: local
  roles:
    - role-hello-world



Create an Inventory File
We need to tell Ansible which hosts to run the playbook on, and we do this with an inventory file. An inventory file is simply a text file containing a list of hosts. Create a new file called inventory in the same folder as hello.yml. Add the following line to inventory, telling Ansible to run just on your computer:

localhost

Run the Playbook
We’re ready to run our role! To start the playbook we use the ansible-playbook command, and we specify our inventory file and which playbook to run. Type the following command from the same folder containing hello.yml:

$ ansible-playbook -i inventory hello.yml

Assuming you have cowsay installed, the output from running hello.yml will look like this:

::

    ______
    < PLAY >
     ------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

     ______________
    < TASK [setup] >
     --------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    ok: [localhost]
     _____________________________________
    < TASK [role-hello-world : Say Hello] >
     -------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    ok: [localhost] => {
        "hello_world_message": "Hi!"
    }
     ____________
    < PLAY RECAP >
     ------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    localhost                  : ok=2    changed=0    unreachable=0    failed=0


What Just Happened?

The above stdout provides a step-by-step guide to the execution of our playbook. Ansible started our play by running the setup task on our host, localhost. Each time a play starts Ansible performs a setup task on all hosts included in the play where it connects to each host and gathers some facts that may be needed by subsequent tasks in the play. In this case the setup task completed with an OK status for localhost.

Next ansible moved to the roles task in our play, as indicated by TASK[role-hello-world:Say Hello]. This tells us it’s running our role starting with the task we named Say Hello. This is followed by the results of the task executed on localhost, as indicated by OK: [localhost] => and the output from the debug module showing the default value we provided for the hello_world_message variable. Yay! It worked! 

And finally, the output provides a recap for the play letting us know what the outcome was for each host. In this case localhost finished with an OK status. We did not modify anything on localhost, so changed is 0. And as expected Ansible was able to communicate with localhost and none of our tasks failed.


How Do We Change the Message?

Our simple role displays the value of the hello_world_message variable. The default value is set to ‘Hi!’. What if we want it to be something else? We can provide a value in our playbook. Let’s make a change to hello.yml and see how it works. Open hello.yml and change the line in the roles list for role-hello-world to the following:

::

    roles:
      - { role: role-hello-world, hello_world_message: Hello Everybody! }

Instead of just providing the name of our role, we’re now providing the name of the role plus a value for hello_world_message.

Running our updated playbook produces the following output showing the new value assigned to hello_world_message:

::

    $ ansible-playbook -i inventory hello.yml
     ______
    < PLAY >
     ------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

     ______________
    < TASK [setup] >
     --------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    ok: [localhost]
     _____________________________________
    < TASK [role-hello-world : Say Hello] >
     -------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    ok: [localhost] => {
        "hello_world_message": "Hello Everybody!"
    }
     ____________
    < PLAY RECAP >
     ------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    localhost                  : ok=2    changed=0    unreachable=0    failed=0


In this way role variables can be thought of as parameters. If role-hello-world was a function in your favorite programming language, we just called that function with a parameter of ‘Hello Everybody!’ and changed the execution result. And that’s really the power of an Ansible role. A role allows us to turn a set of tasks into a reusable unit of work, just like an object or function in any programming language.
Best Practices

Our example role is pretty simple. But roles are pretty simple too. A role is nothing more than a set of tasks contained in tasks/main.yml that can be used over and over again. The tasks can be simple, like ours, or very complicated. And when done right, a role contains everything needed to execute the tasks, including: a default configuration, documentation, templates, files and handlers. 

To insure your future roles meet this standard, here are some guidelines to follow:

- Provide clear documentation in README.md. For this exercise we did not update README.md, but take a look at the template provided by ansible-galaxy. README.md is composed using markdown.
- A role can depend on other roles executing before it. Include any dependencies in meta/main.yml. Learn more about dependencies here FIXME*NEEDLINKTODOCS*FIXME
-  Prefix variable names with the role name, just like we did with hello_world_message.
- In defaults/main.yml provide a default value for each variable.
- Test your role, just as we did here.
- Provide any templates and files needed by the role, even if they are just samples, so that your role works out-of-the-box.

