# Face Time-lapse Tool
### Introduction
Over the past couple of years, I have taken a picture of myself almost every day, which will be
compiled into a long-term time-lapse of my face. Before creating this tool, I would manually rename 
each image file for ordering purposes and align my face to a template in Photoshop, so I can create
the time-lapse. However, with more than a thousand files, this would require a lot of effort
and time. 

### Description
The Face Time-lapse Tool assists in easing this process by automatically indexing each image file
by their 'date-taken' property. Most importantly, the tool will also go through each image and
automatically make the necessary image transformations to be easily compiled into a time-lapse.


#### Libraries Used
+ dlib - finding facial features
+ cv2 - image transformations
+ pyqt5 - GUI


#### References
[1] https://www.pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/ <br>
[2] https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/ <br>
