# echtiapp

### Installing required packages

Before development, proper packages need to be installed on the system. The packages can be installed in venv : 
1. Move to the root folder of the app and activate a virtual environment:
```bash
source .venv/bin/activate
```

2. Install kivy and kivymd
```bash
pip install "kivy[full]"
pip install kivymd
```

3. Install Buildozer - a tool used to build mobile applications, automating the entire build process. Additionally, you need to install other system packages 
```bash
pip3 install --upgrade buildozer
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --upgrade Cython==0.29.33 virtualenv
```

4. At the end of ~/.bashrc file, add
```bash
export PATH=$PATH:~/.local/bin/
```

5. Create main.py and main.kv files with simple application example

6. Run the following command to create an app specification file - buildozer.spec
```bash
buildozer init
```

7. As an initial configuration, modify the following lines in buildozer.spec file
```bash
[app]

# (str) Title of your application
title = EchtiApp

# (str) Package name
package.name = echtiapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.example

...

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

...
```
8. Activate Developer Mode on your mobile phone
    a. On a Samsung mobile phone go to Settings -> About phone -> Software information\
    b. Tap 7 times on Build number pane. Developer mode will be activated\
    c. Go to Settings -> Developer options\
    d. Activate the mode with setting it to ON\
    e. Activate USB debugging\
    f. Connect your phone to the computer via a USB cable

9 Run the following command to build, install and run the app on the phone (First run can take some time)
```bash
buildozer android debug deploy run
```
or, for detailed logs

```bash
buildozer android debug deploy run logcat
```


### References
1. [Kivy installation doc](https://kivy.org/doc/stable/gettingstarted/installation.html#using-pip)
2. [KivyMD installation doc](https://kivymd.readthedocs.io/en/1.1.1/getting-started/)
3. [Installing Buildozer](https://buildozer.readthedocs.io/en/latest/installation.html)