import streamlit as st

st.title('''**10 Cool Beginner Python Tricks That Will Make Your Life Easier**''')
st.caption('''Simple but effective tips for every python lovers''')

from PIL import Image
image = Image.open('1_5IFgojJ4nU8f0YKTcjWDrg.jpeg')

st.image(image, caption='Photo by Miesha Maiden from Pexels')

st.write('''The compactness of Python can make a developer’s life a lot easier when 
writing lines and lines of code. But there are some lesser-known Python tricks that 
can surprise you with their amazing capabilities.

In today’s article, I will discuss 10 Python tips and tricks that will be really 
helpful for beginners to write more compact code. Knowing these tips and tricks 
will definitely save you some valuable time.''')

st.subheader('1. Walrus operator')
st.write('''The `Walrus` **or** `:=` operator is one of the latest additions to python 3.8. 
It is an assignment operator that lets you assign value to a variable within an expression 
like conditional statements, loops, etc.''')

st.write('''__|Example__''')
