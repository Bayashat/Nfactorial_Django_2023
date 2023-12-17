# Exercise-1
"""
    $ python3 -m venv new_env
    $ source new_env/bin/activate
    $ pip list
    $ deactivate
"""

# Exercise-2
"""
    $ python3 -m venv --system-site-packages myenv
    $ pip list
    $ 
"""

# Exercise-3
"""
    $ pip install numpy/requests/soap
    $ pip list
    $ pip freeze > requirements.txt
"""

# Exercise-4
"""
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip list
    $ pip install -r requirements.txt
    $ pip list
"""

# Exercise-5 

with open("test.txt", 'w') as file:
    file.write("Hello There,\n It's me, Bayashat.")
    
    
# Exercise-6
    
with open("test.txt", "r") as file:
    for line in file:
        print(line)