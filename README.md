# Menu Maker

![Coverage Badge](/assets/img/coverage.svg "Coverage Badge")

This project allows restaurant owners to register their restaurant and create a customized menu, allowing customers to easily view the restaurant's offerings from a desktop or mobile device.

Menu Maker is a project that showcases my understanding of best practices using Django and Git. In short, it is a simple CRUD app that showcases Django's utility as a web-first framework.

Menu Maker makes use of many of Django's primary features:

- Django's built-in ORM
    - This project uses SQLite for maximum portability and ease of setup
- Whenever possible, Class-Based Views (CBVs) are used, in order to take advantage of the features that are built into Django's CBVs (e.g. easy paging).
- Django's built-in test runner
    - To the best of my knowledge, all statements in the code have been properly tested (Coverage is currently at 94%).
    - Due to how Python's Coverage module detects code coverage, the number is a bit short of 100%. My goal is not to ensure that the badge says 100%, but to ensure that the codebase is sound.
    - All efforts have been made to ensure that the tests cover all expected circumstances.

This project also represents an effort to implement proper Git best practices, including:

- use of branches for separation of concerns (feature/test/main)
- small, incremental commits
- concise and accurate descriptions of each commit

<br>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="margin-left: auto; margin-right: auto; border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
