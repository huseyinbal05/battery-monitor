from setuptools import setup

APP = ['src/app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': "Battery Monitor",
        'CFBundleDisplayName': "Battery Monitor",
        'CFBundleGetInfoString': "Battery Monitor App",
        'CFBundleIdentifier': "com.huseyinbal.battery-monitor",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
    },
    'packages': ['rumps', 'psutil'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
