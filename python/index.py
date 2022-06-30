# Write your python code here
# For a quick tutorial: https://github.com/pyscript/pyscript/blob/main/docs/tutorials/getting-started.md

# The <py-env></py-env> tag will be inside the <head> of the HTML. There you need to add any
# modules you are using in this python file (eg: pandas, numpy). You also need to include any
# files (exel, csv) used in this script. If not, the files won't be loaded and an error will be
# thrown on the page.

# The <py-script></py-script> tag is inside the body of the HTML. There you can write python as
# well. If you are using this file, make sure you include it in the tag. Pass it inside the "src"
# attribute. eg: <py-script src="./python/index.py">. For this template, the source is already
# include it. But be aware if you change the name of the python name you need to change it in the
# tag.

# To pass a variable to the HTML use pyscript.write('id-in-html-element', 'python-variable')
# e.g: if you have a <div id='number'></div> in you HTML.
# Pass python variable or code --> pyscript.write('number', python_variable)

