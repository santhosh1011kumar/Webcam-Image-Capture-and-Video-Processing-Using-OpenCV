#!/usr/bin/env python
# coding: utf-8

# # Ex. No: 02  
# # Image Acquisition using Web Camera  
# 
# **Name:** ____________    **Reg. No:** ____________
# 

# ## Dr.MANIKANDAN S P Saveetha Engineering College
# - drmanikandansp@gmail.com 
# - CNN using Custom Images 
# - 19AI413-Digital Image Processing Techincs 
# 
# - EVEN SEM ( Slot: 4Q1-2 & 4N5-2)

# i) Write the frame as JPG file

# In[5]:


import cv2
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time


# In[6]:


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cv2.imwrite("captured_frame.jpg", frame)
cap.release()


# In[7]:


captured_image = cv2.imread('captured_frame.jpg')


# In[8]:


plt.imshow(captured_image[:,:,::-1])
plt.title('Captured Frame')
plt.axis('off')
plt.show()


# ii) Display the video

# In[12]:


cap = cv2.VideoCapture(0)

for i in range(50):
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(frame_rgb)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)

cap.release()


# iii) Display the video by resizing the window

# In[10]:


cap = cv2.VideoCapture(0)

for i in range(50):
    ret, frame = cap.read()
    if not ret:
        break
    resized_frame = cv2.resize(frame, (100, 150))  # Resize to 320x240
    frame_rgb = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(frame_rgb)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)

cap.release()


#  iv) Rotate and display the video

# In[11]:


cap = cv2.VideoCapture(0)

for i in range(50):
    ret, frame = cap.read()
    if not ret:
        break
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame_rgb = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(frame_rgb)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)

cap.release()


# In[ ]:




