#AUTHOR: ALLISON MURDOCK
#MCGILL ID: 261009978

#Assignment 3

def is_valid_image(image):
    """ (list<int>) -> bool
    Takes a nested list as an input and returns true if the nested
    list represents a valid PGM image matrix and False otherwise.
    The matrix will be valud if the list only contains integers
    between 0 and 255, and each row of the matrix is equal in length. 
    
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> is_valid_image([[0], [0, 0]])
    False
    >>> is_valid_image([["0x5", "200x2"], ["111x7"]])
    False
    """
    
    row_len = len(image[0]) #setting the row length equal to the length of the first row as a benchmark 
    for row in image:
        if len(row) != row_len:
            return False         #checks if row length is equal to 1st row to make sure all rows are equal. 
        
        row_len = len(row)
        
        for val in row:
            if type(val) != int or (val < 0 or val > 255): #two checks here: one if the value is anything other than an integer or if the integer value is within the range of 0-250, which is required to be a compression file
                return False
            
    return True



#HELPER FUNCTION USED TO COMPUTE THE LENGTH OF THE ROW FOR A COMPRESSED IMAGE (CUTS DOWN ON REPEDITIVE CODE) 
def compute_row_len(row):
    '''(list<str>)-> int
    Takes a list (a row of the matrix) and returns the total "B" value
    within the list as the list's length. Called only in the instance
    that the image matrix is compressed. 
    >>> compute_row_len(["0x24"])
    24
    '''
    row_len = 0
    for val in row:
        num_repetitions = val.split("x")[1] #this only works on strings so quotes are required we can use this as this function is specifically for compressed images
        
        if num_repetitions.isdecimal():
            num_repetitions = int(num_repetitions) #num_repetitions is the "B" value, aka the number of times "A" is repeated
        else:
            return -1
        
        row_len += num_repetitions
        
    return row_len

def is_valid_compressed_image(image):
    '''(list<int>)-> bool
    Takes a a nested list as input and returns True if the nested
    list represents a valid compressed PGM image matrix and False
    otherwise. To pass as True it must follow the proper compressed
    image format, which is a matrix composed of sublists of the form
    AxB, A being an integer between 0 and 255 and B being any postive
    integer (the amt that each pixel is compressed by). The sum of all
    B values per row must be the same.
    
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    >>> is_valid_compressed_image([[0], [0, 0]])
    False
    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True
    '''
    
    if type(image[0][0]) == str:
        row_len = compute_row_len(image[0]) #incorperating the helper function
    else:
        
        return False
    
    for row in image:
        if compute_row_len(row) != row_len: #checking the quantities (which translate to the row lengths) are constant. 
        
            return False
        
        row_len = compute_row_len(row)
        
        if row_len == -1:
          
            return False
        
        for val in row:
            val = val.split("x")
            
            if len(val) != 2 or not val[0].isdecimal() or not val[1].isdecimal(): #establishing that there must be two numbers in front and behind "x" and they both must be numbers
              
                return False
            
            a_val = val[0]
            b_val = val[1]
            
            a_val = int(a_val)
            
            if a_val < 0 or a_val > 255: #making sure it passes the whiteness condition 
               
                return False
            
    return True

#HELPER FUNCTION TO RAISE ASSERTION ERROR- RATHER THAN REPEATING CODE IN EACH FUNCTION
def valid_metadata(image_format, dimensions, white_limit, compressed = False):
    '''( str, str, str, bool)-> str
    Takes a string and asseses if it meets the format indicated for both regular and
    compressed images. If it doesnt meet the requirements, it is deemed an invalid
    matrix image and an assertion error is raised. Sets compressed to false to tell
    the computer that it is dealing with a regular image
    >>> valid_metadata("P2C","24 7", "265", compressed = True)
    AssertionError("Invalid white limit: " + 265)
    '''
    if compressed:
        if image_format != "P2C":
            raise AssertionError(image_format + " is not a valid image format.") #if compressed and image format isnt "P2C"
    else:
        if image_format != "P2":
            raise AssertionError(image_format + " is not a valid image format.")#if regular ("P2") and image format not regular
        
    if len(dimensions.split()) != 2 or not dimensions.split()[0].isdecimal() or not dimensions.split()[1].isdecimal(): #if the dimensions are more than two numbers or something other than numbers
        raise AssertionError("Invalid dimensions: " + dimensions)
    
    if len(white_limit.split()) != 1 or not white_limit.isdecimal() or int(white_limit) < 0 or int(white_limit) > 255: #if the white limit is less than 0 or greater than 255
        raise AssertionError("Invalid white limit: " + white_limit) 
            

def load_regular_image(image_filename):
    '''(str)-> list<list>
    Takes a filename (string) of a PGM image file as imput,
    and loads in the image contained in the file and returns
    it as an image matrix. If during or after loading, the
    resulting image matrix is found to not be in PGM format,
    then an AssertionError is raised.
    
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255,
    255, 255, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255,
    0],
    [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0],
    [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0,
    0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    f = open(image_filename, "r")
    file = f.read().strip().split("\n") #to read by row rather than as one long list
    f.close()
    
    image = []
    
    image_format = file[0].strip() #leaving just the image matrix, metadata is just to be read not necessarily displayed
    dimensions = file[1].strip()
    white_limit = file[2].strip()
    
    valid_metadata(image_format, dimensions, white_limit) #incorperating helper function 
    
    cols, rows = dimensions.split()
    cols = int(cols)
    rows = int(rows)
    
    for line in file[3:]:
        line = line.strip().split() #breaking down and building the matrix row by row
        
        row = []
        
        for val in line:
            if val.isdecimal():
                row.append(int(val)) #what builds the image
                
            else:
                raise AssertionError(val + " is not a valid pixel value.")
             
        if len(row) != cols:
            raise AssertionError("Invalid row length.") #if row is not matching the dimensions specified, return error
        
        image.append(row) #combining all the rows
    
    
    if is_valid_image(image):
        return image
    else:
        raise AssertionError("Error load_regular_image()")
        
def load_compressed_image(image_filename):
    '''(str)-> list<list>
    Takes a filename (string) of a compressed PGM file as input,
    and loads in the image contained in the file and returns it
    as a compressed image matrix. If, during or after loading the
    image matrix is not in compressed PGM format, then an AssertionError is raised.
    
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x1', '0x4'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '255x1', '0x4'], ['0x24']]
    '''
    f = open(image_filename, "r")
    file = f.read().strip().split("\n")  #to read by row rather than as one long list
    f.close()
    
    image = []
    
    image_format = file[0].strip() #leaving just the image matrix, metadata is just to be read not necessarily displayed
    dimensions = file[1].strip()
    white_limit = file[2].strip()
    
    valid_metadata(image_format, dimensions, white_limit, compressed = True)
    
    cols, rows = dimensions.split()
    cols = int(cols)
    rows = int(rows)
    
    
    
    for line in file[3:]: #reads the matrix rather than the metadata
        line = line.strip().split()
        
        row = []
        
        row_len = 0
        
        for val in line:
            val_split = val.split("x") #process is different for a compressed image as the the pixel value and the quantity is split by x and in a string
            
            if len(val_split) != 2:
                raise AssertionError("Invalid number of x")
            
            pixel_val, quantity = val_split
            
            if not pixel_val.isdecimal() or not quantity.isdecimal():
                raise AssertionError("Data is non-numerical")
            
            pixel_val = int(pixel_val)
            quantity = int(quantity)
            
            row_len += quantity #number of times the pixel value is repeated
            
            row.append(val) #builds the row
            
            
        if row_len != cols:
            raise AssertionError("Invalid row length.")
        
        image.append(row) #combines all rows
    
    
    if is_valid_compressed_image(image):
        return image
    else:
        raise AssertionError("Error load_compressed_image()")
        

def load_image(image_filename):
    '''(str)-> list<list>
    Takes a filename (string) of a file as input and checks the
    first line of the file. If it is 'P2', the loads in the file
    as a regular PGM image and reutrns the timage matrix. It its 'P2C',
    then loads in the file as a compressed PGM image and returns the compressed
    image matrix. If it is anything else, then an AssertionError with an
    appropritate error message will be raised.
    
    >>> load_image("comp.pgm.compressed")
    [['0x24'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x4', '0x1'],
    ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '187x1', '0x1', '255x1', '0x4'],
    ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1',
    '255x1', '0x4'],
    ['0x24']]
    '''
    f = open(image_filename, "r")
    
    file_type = f.read().strip().split("\n")[0].strip() #stripping each layer of the matrix image 
    
    f.close()
    
    if file_type == "P2":
        return load_regular_image(image_filename) #calling our previous functions rather than repeating code
    elif file_type == "P2C":
        return load_compressed_image(image_filename)
    
    
    raise AssertionError("Invalid file type: " + file_type)
        
    
def save_regular_image(image_matrix, image_filename):
    '''(list<list>, str)-> NoneType
    Takes a nested list and a filename (string) as input,
    and saves it in the PGM format to a file with the given
    filename. If the image matrix given is not a valid PGM
    image matrix, then an AssertionError will be raised. 
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255
    255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    >>> image = [[0]*10, [255]*10, [0]*10]
    >>> save_regular_image(image, "test.pgm")
    >>> image2 = load_image("test.pgm")
    >>> image == image2
    True
    '''
    if is_valid_image(image_matrix):
        output_file = open(image_filename, "w")
        
        #next lines below are for metadata
        output_file.write("P2\n")
        
        rows = len(image_matrix)
        cols = len(image_matrix[0])
        
        output_file.write(str(cols) + " " + str(rows) + "\n") #write column and row dimensions on a new line
        
        output_file.write("255\n")
        
        for row in image_matrix:
            
            output_row = ""
            
            for pixel_val in row:
                output_row += str(pixel_val) + " " #putting white spaces in between
                
                
            output_row = output_row.strip() + "\n" #creating a new line w/ each row
            
            output_file.write(output_row)
            
        
        output_file.close()
    else:
        raise AssertionError("Error saving to PGM format, invalid matrix provided.")

   
def save_compressed_image(image_matrix, image_filename):
    '''(list<list>, str) -> NoneType
    Takes a nested list and a filename (string) as input,
    and saves it in the compressed PGM format to a file with the given
    filename. If the image matrix given is not a valid compressed PGM
    image matrix, then an AssertionError will be raised.
    
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    >>> image = [["0x5", "200x2"], ["111x7"]]
    >>> save_compressed_image(image, "test.pgm")
    >>> image2 = load_compressed_image("test.pgm")
    >>> image == image2
    True
    '''
    if is_valid_compressed_image(image_matrix):
        output_file = open(image_filename, "w")
        
        #next lines below are for metadata
        output_file.write("P2C\n")
        
        rows = len(image_matrix)
        cols = compute_row_len(image_matrix[0]) #using the helper function again
        
        output_file.write(str(cols) + " " + str(rows) + "\n") 
        
        output_file.write("255\n")
        
        for row in image_matrix:
            
            output_row = ""
            
            for pixel_val in row:
                output_row += pixel_val + " "
                
            output_row = output_row.strip() +  "\n"
            
            output_file.write(output_row)
            
        #not much different here other then the way we determine the lenth of the row
        
        output_file.close()
    else:
        raise AssertionError("Error saving to PGM format, invalid matrix provided.")
            
def save_image(image_matrix, image_filename):
    '''(list<list>, str)-> NoneType
    Takes a nested list and a filename (string) as input,
    checks the type of elements in the matrix to determine
    whether they are compressed or regular and returns the
    according function. If they are anything else, then a
    AssertionError with an appropriate error message should
    be raised instead.
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    '''
    if type(image_matrix[0][0]) is int:
        save_regular_image(image_matrix, image_filename)
       
    elif type(image_matrix [0][0]) is str:
        save_compressed_image(image_matrix, image_filename)  

    else:
        raise AssertionError("Error saving to PGM format, invalid matrix provided.")
     

def invert(image):
    '''(list<list>)-> list<list>
    Takes a regular PGM image matrix as input, and returns the
    inverted image, and will not modify the input matrix. If the
    input matrix is not a vliad PGM image matrix, then an
    AssertionError is raised.
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    '''
    
    if not is_valid_image(image):
        raise AssertionError("Unable to invert, invalid image.")
    
    inverted_image = []
  
    for sublist in image:
        inverted_sublist = []
        for i in sublist:
            inverted_sublist.append(255 - i) #creating a deep copy so the input isnt modified
        inverted_image.append(inverted_sublist)
    
    return inverted_image
                       
def flip_horizontal(image):
    '''(list<list>)-> list<list>
    Takes a regular PGM image matrix as input, and returns the image
    matrix flipped horizontally, and wont modify the input matrix. If the input
    matrix is not a valid PGM image matrix,then a AssertionError will be raised.  
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    '''
    if not is_valid_image(image):
        raise AssertionError("Unable to flip, invalid image.")
    
    
    
    flipped_image = []
    
    for sublist in image:
        sublist = sublist[::-1] 
        flipped_image.append(sublist) #maintains the order of the sublists appear in, but flips the order of the values in each sublist
        
    return flipped_image

def flip_vertical(image):
    '''(list<list>)-> list<list>
    Takes a regular PGM image matrix as input, and returns the image
    matrix flipped vertically, and wont modify the input matrix. If the input
    matrix is not a valid PGM image matrix,then a AssertionError will be raised.
    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    '''
    
    if not is_valid_image(image):
        raise AssertionError("Unable to flip, invalid image.")
    
    return image[::-1] #flips the order of the sublists, maintains the order of the values within each sublist
            
def crop(image, x, y, rows, columns):
    '''(list<list>, int, int, int, int)-> list<list>
    Takes a regular PGM image matrix, two non-negative integers for the top left
    row and column, and two positive integers for the number of rows and columns
    (for the target rectagle) as input. Returns an image matrix corresponding to
    the pixels contained in the target rectangle, and will not modify the input
    list. If the input matrix is not a valid PGM matrix, then an AssertionError
    will be raised.
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 2, 2, 1)
    [[6], [10]]
    '''
    
    if not is_valid_image(image):
        raise AssertionError("Unable to crop, invalid image.")
    
    output = []
    
    for sub_row in image[x:x + rows]: #slicing (cropping) by row
        current_row = sub_row[y:y + columns] #slicing (cropping) by column
        output.append(current_row) #building up the cropped image
        
    return output 

def find_end_of_repetition(matrix_row, index, target_number):
    '''(list, int, int)-> int
    Takes a list of integers and two non-negative integers (an index and a
    target number) as input. Looks through the list starting after the given index, and returns the index of the last
    consecutive occurrence of the target number.
    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
        4
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
        6
    '''
    
    if not type(index) is int or not type(target_number) is int or index < 0 or target_number < 0:
        raise AssertionError("inputs must be non-negative.")
 
    for i in range(index, len(matrix_row)): #starting at the index, for the length of the matrix row
        if matrix_row[i] != target_number:
            return i-1

    return i #returns i if your target_number extends to the last number in the list
    
def compress(image):
    '''(list<list>)-> list<list>
    takes a (non-compressed) PGM image matrix as input. Compresses the matrix according
    to the compression algorithm described earlier in this PDF and returns the compressed matrix. If
    the input matrix is not a valid PGM image matrix, then a AssertionError with an appropriate
    error message should be raised instead.
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    '''
    if is_valid_image(image) == False:
        raise AssertionError("Error saving to PGM format, invalid matrix provided.")
    
    compressed_image = [] 
    
    for sublist in image: 
        i = 0
        
        row = [] 
        while i < len(sublist): # using a while loop over a for loop here as you dont necessarily need to examine and iterate through each value of the sublist 
            pixel_value = sublist[i]  
            ending_index = find_end_of_repetition(sublist, i, pixel_value)
            
            repetitions = ending_index - i + 1 #to determine how many times pixel_value is repeated 
            
            row.append(str(pixel_value) + "x" + str(repetitions))
            
            i = ending_index + 1
            
        compressed_image.append(row)
        
    return compressed_image

def decompress(image):
    '''(list<list>) -> list<list>
    takes a compressed PGM image matrix as input. Decompresses the
    matrix by undoing the compression algorithm described earlier
    in this PDF and returns the decompressed matrix. If the input matrix
    is not a valid PGM matrix, then an AssertionError is raised.
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> image = [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> compressed_image = compress(image)
    >>> image2 = decompress(compressed_image)
    >>> image == image2
    True
    '''
    if is_valid_compressed_image(image) == False:
        raise AssertionError("Error saving to PGM format, invalid matrix provided.")
  
    decompressed_image = []
    
    for sublist in image:
        row = []
        
        for elmt in sublist:
            pixel_value, repetitions = elmt.split("x")
            pixel_value = int(pixel_value)
            repetitions = int(repetitions)
            
            for i in range(repetitions):
                row.append(pixel_value) #appending by the repetition value
                
        decompressed_image.append(row)
    
    return decompressed_image
        
def process_command(command_string):
    '''(str)-> NoneType
    takes a string as input corresponding to a series of space-separated
    image processing commands, and executes each command in turn. Does not
    return anything. The command string can have any of the following commands
    which each correspond to one of the above functions: 'LOA'D', 'SAVE', 'INV',
    'FH', 'FV', 'CR', 'CP', 'DC'. Some commands will have an extra part after
    them to indicate further needed information. For example, a LOAD command will
    always have the form 'LOAD<x.pgm>' where ‘x.pgm’ will be a filename, and same
    for the SAVE command. A crop command will have the form 'CR<y,x,h,w>' where y
    and x are two non-negative integers and h and w are two positive integers, and
    y, x, h and w correspond to the four integer inputs needed for the crop command. 
    The command string will always begin with a LOAD command and end with a SAVE command. 
    If an unrecognized command is part of the command string, then an AssertionError is raised.          
    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.pgm")
    >>> image == image2
    True
    >>> process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
    >>> load_compressed_image("comp.pgm.compressed")
        #[['0x24'],['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'],
        #['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
        #'187x1', '0x1', '255x1', '0x2', '255x1', '0x1'],
        #['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
        #'187x1', '0x1', '255x4', '0x1'],
        #['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1',
        #'187x1', '0x1', '255x1', '0x4'],
        #['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1',
        #'255x1', '0x4'],
        #['0x24']]
    '''
    
    command_list = command_string.split() #splits them by the white space
    
    valid_commands = ['LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP', 'DC']
    
    for cmd in command_list:
        cmd = cmd.split("<") #isolates the filename within the brackets (<x.pgm>)
        
        if cmd[0] not in valid_commands: 
            raise AssertionError(cmd[0] + " is not a valid command!") #quick validity check before function is run
            
        if len(cmd) == 1:
            cmd = cmd[0] #reads the command at index 0
            
            #basic calls, no special conditions for these commands 
            if cmd == "INV":
                image = invert(image) 
            elif cmd == "FH":
                image = flip_horizontal(image)
            elif cmd == "FV":
                image = flip_vertical(image)
            elif cmd == "CP":
                image = compress(image)
            elif cmd == "DC":
                image = decompress(image)
            
        elif len(cmd) == 2:
            args = cmd[1][:-1]
            cmd = cmd[0] #returns the command at zero 
            
            #special condition functions
            if cmd == "LOAD":
                image = load_image(args)
            elif cmd == "SAVE":
                save_image(image, args)
            elif cmd == "CR":
                args = args.split(",") # so it takes each argument as an individual rather than one long string
                image = crop(image, int(args[0]), int(args[1]), int(args[2]),  int(args[3])) #accounting for arguments <y, x, h, w> and converts them into integers
                
                
              
        
        
        
        
        
        
        
        
        
        
    