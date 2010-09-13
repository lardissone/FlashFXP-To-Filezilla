## FlashFXP to Filezilla

This small piece of code converts FlashFXP databases to Filezilla.


### Usage

Export sites in FlashFXP using Site Manager.  
In **Site Manager** click on the folder/site you want to export, and then right-click and select **Export...**:
![Site Manager](http://cl.ly/f92d916b9d42600d3923/content/)

Save the file, and run this:

		python convert.py flashfxp-exported-file.ftp

And voila! A new `filezila.xml` file is created in the same directory with the database in Filezilla format.