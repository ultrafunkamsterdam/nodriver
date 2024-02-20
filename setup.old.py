__ascii_art = ("""
##################################################################################################

          888b    888              8888888b.             d8b
          8888b   888              888  "Y88b            Y8P
          88888b  888              888    888
          888Y88b 888    .d88b.    888    888   888d888  888   888  888   .d88b.   888d888
          888 Y88b888   d88""88b   888    888   888P"    888   888  888  d8P  Y8b  888P"
          888  Y88888   888  888   888    888   888      888   Y88  88P  88888888  888
          888   Y8888   Y88..88P   888  .d88P   888      888    Y8bd8P   Y8b.      888
          888    Y888    "Y88P"    8888888P"    888      888     Y88P     "Y8888   888

               BY ULTRAFUNKAMSTERDAM (https://github.com/ultrafunkamsterdam)


##################################################################################################
""")


import codecs
import os


from setuptools import setup, find_packages


dirname = os.path.abspath(os.path.dirname(__file__))

with codecs.open(
    os.path.join(dirname, "version"),
    mode="r",
    encoding="utf-8",
) as fp:
    version = fp.read().strip()

description = (
    __ascii_art +
    """
    * Official successor of Undetected Chromedriver
    * Can be made to work for for all chromium based browsers.
    * Dropped selenium and chromedriver binary requirements.
    * fully asynchronous == bizarre performance gains, and more granular control
    
    Part of undetected-chromedriver, or merely the successor of it, this library is a full rewrite, providing a
    fast framework for web automation, webscraping, bots and any other creative ideas which are normally 
    hindered by annoying anti bot systems like Captcha / CloudFlare / Imperva / hCaptcha and other 
    big corp "ai" money machines using your input to make even more $$ (http://tinyurl.com/bigcorp-ai-inputs)
    
    The webdriver/selenium requirement is dropped entirely, since this library communicates directly to the browser.
    Being fully asynchronous, this adds massive performance improvements and more detailed control possibilities.
    
    As usual ( like undetected chromedriver) all config details and best practices are built-in, which means 
    up and running with just a line of code.
    
    This makes it simple to use for quick prototyping, and perfect for interactive interpreter use (eg: IPython).
    

    WARNING:
       - results may vary due to many factors. No guarantees are given whatsoever.
       - Running from bad IP or datacenter may still cause captcha's and/or other problems.
       - With great power comes ... etc etc etc
         no but SERIOUS: for your own benefit, make sure "they" have no reason for upscaling anti-bot measurements.
         there might be one day it would not be feasible anymore to work up against big corp, and provide upgrades 
         and free libraries. 
        
    """)



setup(
    name="nodriver",
    version=version,
    packages=["nodriver", "nodriver.core", "nodriver.cdp"],
    install_requires=[
        "mss",
        "websockets>=11",
    ],
    package_data={"nodriver": ["example/*"]},
    url="https://github.com/ultrafunkamsterdam/undetected-chromedriver",
    license="GPL-3.0",
    author="UltrafunkAmsterdam",
    author_email="info@blackhat-security.nl",
    description=description,
    long_description=open(os.path.join(dirname, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
