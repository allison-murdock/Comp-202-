1. I was unsure with the save_regular,save_compressed, and save_image function docstrings to indicate that it returns nothing (NoneType) 
or to say it returns a string as in some circumstances an AssertionError can be raised. 

2. For valid_metadata, in the last argument, you can set compressed = False or True depending on the image you are dealing with (ie if it 
reads P2 then you put compressed as false and vice versa w P2c)

Nothing else to report :)