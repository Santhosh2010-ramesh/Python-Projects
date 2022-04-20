#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install qrcode')


# In[ ]:


from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode


# In[ ]:


image=Image.new('RGB',(1000,900),(255,255,255))
draw=ImageDraw.Draw(image)


# In[ ]:


font=ImageFont.truetype('arial.ttf',size=45)
os.system("ID CARD Generator")


# In[ ]:


d_date=datetime.datetime.now()
reg_format_date=d_date.strftime("%d-%m-%Y\t ID CARD Generator\t %I:%M:%S %p")
print(reg_format_date)


# In[ ]:


print('\n\nAll Fieldss are Mandatory')
print("Avoid any kind of spelling mistakes")
print("Write everything i uppercase letters")
(x,y)=(50,50)
message=input('\n Enter your company name: ')
company=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=80)
draw.text((x,y),message,fill=color,font=font)


# In[ ]:


# adding a unique id number. You can manually take it from the user
(x,y)=(600,75)
idno=random.randint(10000000,900000000)
message=str("ID"+str(idno))
color='rgb(0,0,0)'#black color
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)


# In[ ]:


(x,y)=(50,250)
message=input("Enter your Full Name: ")
name=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=45)
draw.text((x,y),message,fill=color,font=font)                        


# In[ ]:


(x,y)=(50,350)
message=input("Enter your Gender: ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font) 
(x,y)=(250,350)
message=input("Enter your Age: ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font) 
(x,y)=(50,450)
message=input("Enter your DOB: ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font) 


# In[ ]:


(x,y)=(50,450)
message=input("Enter your Blood group: ")
color='rgb(255,0,0)'
draw.text((x,y),message,fill=color,font=font) 


# In[ ]:


(x,y)=(50,450)
message=input("Enter your Mobile Number: ")
color='rgb(255,0,0)'
draw.text((x,y),message,fill=color,font=font) 


# In[ ]:


(x,y)=(50,750)
message=input("Enter your Address: ")
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)


# In[ ]:


image.save(str(name)+' .png')


# In[ ]:


image=qrcode.make(str(company)+str(idno))
img.save(str(idno)+'.bmp')


# In[ ]:


til=Image.open(name+'.png')
Iim=Image.open


# In[ ]:


img=qrcode.make(str(company)+str(idno))
img.save(str(idno)+'.bmp')


# In[ ]:


til=Image.open(name+'.png')
im=Image.open(str(idno)+'.bmp')
til.paste(im,(600,350))
til.save(name+'.png')


# In[ ]:


print(('\n\n\nYour ID Card successfully created in a PNG file'+name+'.png'))
eval(input('\n\nPress any key to close program...'))


# In[ ]:




