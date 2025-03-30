# fw-fanctrl

[![Static Badge](https://img.shields.io/badge/Linux%E2%80%AF%2F%E2%80%AFGlobal-FCC624?style=flat&logo=linux&logoColor=FFFFFF&label=Platform&link=https%3A%2F%2Fgithub.com%2FTamtamHero%2Ffw-fanctrl%2Ftree%2Fmain)](https://github.com/TamtamHero/fw-fanctrl/tree/main)
![Static Badge](https://img.shields.io/badge/no%20binary%20blobs-30363D?style=flat&logo=GitHub-Sponsors&logoColor=4dff61)

[![Static Badge](https://img.shields.io/badge/Python%203.12-FFDE57?style=flat&label=Requirement&link=https%3A%2F%2Fwww.python.org%2Fdownloads)](https://www.python.org/downloads)



### This is a GSoC Qualificaiton Task Version of [fw-fanctrl](https://github.com/TamtamHero/fw-fanctrl/tree/main) project.</br>
#### The GSoC project aims at: </br>
* Making the requirements changes in ectool so that the functionality is available as a library that can be called from different languages.
* Creating, specifically, the Python bindings.
* Integrating the work with fw-fanctrl.

#### As a result, the Qualification Task aims at:
* A proof of concept - creating a basic dummy library that returns a constant value to Python (for any of the functions), and integrate it into fw-fanctrl.

#### Steps towards resolving the task
* explore how python bindings really work.
* choose among python bindings available tools.
* knowing the pros & cons of the chosen tool.
* write the code for a dummy library.
* write a script for automating build & test processes.
* running the test script and ensures interface functionality.
* integrating the dummy library into fw-fanctrl project.

#### How to test the functionality
* ensure you are at the parent directory of the project
* if you want you can run the test script:</br> `$invoke all`
* simply run the basic fw-fanctrl command:</br> `$sudo PYTHONPATH=src python3 -m src.fw_fanctrl run `

#### Output in Pictures
![Screenshot from 2025-03-30 13-51-04](https://github.com/user-attachments/assets/eb58a324-4821-4103-aa9a-f2c025e72a84)
