# Setting up the project (for Linux based CLI):

# In main project directory with venv file type:
source venv/bin/activate

# After that go on folder up to "images" directory with the whole project:
cd images
# and start project with Django command:
python3 manage.py runserver

# From now on project should be available at "localhost:8000/api/images" in Your web explorer.
# other links are specified in API .json format views (relative uri's)
# Then You can log in onto pre-created users:

name: glem
tier: Basic

name: oleg
tier: Premium

name: jozin
tier: Enterprise

name: jontek
tier: Incredible (custom-made)

# For all the users listed above there is one common password:
okmijn123

# For admin panel You need to use:
name: admin
pass: admin

####################################################
From Author:
Thank You very much for checking my not-so-perfect and unfinished project. Due to being self-taught
amateur with full-time professional job in quite other field I am proud that with just basic knowledge
about Django Rest Framework module and quite better fluence with Django/Flask I made app meeting most
of stated requirements. Spending about 1-2 hours on 5 afternoons and about 5-6 hours of weekend, gives
about 15 hours of work (more than 50% of that time was learning new things in DRF).
Here are some things, that should be done better, but lack of free time (and sometimes lack of the skills)
were blocking me:
- MUCH more tests,
- better cleanliness of the code,
- adding .gitignore (totally forgot about it :c) and using branching and better logic in commits,
- more Validators and Error Handling,
- adding special view with expiring link to Byte Image (using third-party module to generate expiring tokens)


I hope that it is not too much of a sacrifice for You to go through my code ant test provided app.
I am sorry for Your headache (;)), but hoping that You will appreciate my determination and fast-learning skills
I am patiently waiting for Your feedback.

Whether I made any impression at You or not, I am grateful for giving me a chance and counting on positive response.
Now it is time to REST and chill with World Cup matches :)
