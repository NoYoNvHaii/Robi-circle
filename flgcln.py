o
    P��b�  �                   @   sj  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeed e
 ��Zee	d e d e
 d �Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d d lmZmZmZmZ d dlZd dlmZ d dlZd dlZd dlmZ d!Zed" Z e� Z!d#e!d$< d%e!d&< ee!d'< ej"e e!d(�Z#e#�� d) d*k�r4eed+ e	 e#�� d, d-  d � e#�� d, d. Z$g Z%d/Z&ej"e&e!d(�Z'e�r�e$D ]Z(eed0 e	 d1 e e(d2  � e%�)e(d2 � �qDz4e%D ]/Z*ed3 e* Z ej"e e!d(�Z#e#�� d) d4k�r�ee	d5 e e* e	 d6 � �qbeed7 � �qbW n
   eed8 � Y eee	d9 e
 d: e	 d; ��Z+e �d� dS )<�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZJoNyZword� r   �	flgcln.py�	logoprint   s
   
�r   z[>] Enter Api Key: z

	[!]z, If You Wonna To Clear Following List Type Yz4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz 
)r
   )�init�Fore�Back�Stylez5https://circle.robi.com.bd/mylife/appapi/appcall.php?zop=getFollowingInfoList�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-key)�headersZrdescZOKz[>] Total Following:�data�totalZ	followingz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=Your Circle  Following List Is Cleaning By Using MoJiiB....!! &retry=falsez
[>]z CIRCLE ID	:	�nicknamezop=stopFren&nickname=zRequest acceptedu   
[√] You have left zH's  circle & will not be receiving his/her status update CSHOUT anymore.u   
[×] Something Went Wrongu   [×] Error!z	 

	Pressz Enterz To Exit),�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�input�x�bool�getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   �baseZurlr   ZpostZresp�yZflgNicksZurlxZresp5�user�appendr   Zxnr   r   r   r   �<module>   s�   




	$  � 