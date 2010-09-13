## FlashFXP to Filezilla

This small piece of code converts FlashFXP databases to Filezilla.


### Usage

Export sites in FlashFXP using Site Manager.  
In **Site Manager** click on the folder/site you want to export, and then right-click and select **Export...**:
![Site Manager](http://cl.ly/f92d916b9d42600d3923/content/)

Save the file as `flash.xml`, in the same folder than `convert.py` and run it:

		python convert.py

And voila! A new `filezila.xml` file is created with the database in Filezilla format.