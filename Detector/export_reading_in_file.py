
#this file is for export readings: free lots , occupied lots to Readings files
#************************************First Location Exports******************************************
def export_reading_in_file(array):
    if(len(array)):

        text_file = open("Reading_And_Assets/reading.txt", "w")
        text_file.write(', '.join([str(i) for i in array]))#seperator
        text_file.close()

def export_reading_in_file2(array):
    if(len(array)):

        text_file = open("Reading_And_Assets/reading2.txt", "w")
        text_file.write(', '.join([str(i) for i in array]))#seperator
        text_file.close()

#************************************Second Location Exports******************************************

def export_reading_in_file_occupied(array):
    if(len(array)):

        text_file = open("Reading_And_Assets/reading_occ.txt", "w")
        text_file.write(', '.join([str(i) for i in array]))#seperator
        text_file.close()


def export_reading_in_file_occupied2(array):
    if (len(array)):
        text_file = open("Reading_And_Assets/reading2_occ.txt", "w")
        text_file.write(', '.join([str(i) for i in array]))#seperator
        text_file.close()