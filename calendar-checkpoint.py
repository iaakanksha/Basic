{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import calendar\n",
    "text = calendar.calendar(2020)\n",
    "\n",
    "root = Tk()\n",
    "root.geometry('550x600')\n",
    "root.title('CALENDAR')\n",
    "label1 = Label(root,text='CALENDAR',bg='dark gray',font=('times',28,'bold'))\n",
    "label1.grid(row=1,column=1)\n",
    "root.config(background='white')\n",
    "l1=Label(root,text=text,font='consolas 10 bold')\n",
    "l1.grid(row=2,column=1,padx=20)\n",
    "root.mainloop()\n",
    "                                                         \n",
    "                                                            \n",
    "                                                             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
