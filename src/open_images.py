import os
import pydicom
import numpy as np
from PIL import Image

def open_dicom_stack(folder_path):
    dicom_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.dcm')], key=len)
    slices = []
    
    for file in dicom_files:
        file_path = os.path.join(folder_path, file)
        ds = pydicom.dcmread(file_path)
        slices.append(ds.pixel_array)
    
    stack = np.stack(slices, axis=0)
    return stack

# Example usage
#dicom_folder = 'D:/Projets/Python/3DAnalysis/tests/dicomStack'
#dicom_stack = open_dicom_stack(dicom_folder)
#print(dicom_stack.shape)


def open_tiff_stack(folder_path):
    tiff_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.tif')])
    slices = []
    
    for file in tiff_files:
        file_path = os.path.join(folder_path, file)
        ds = Image.open(file_path)
        slices.append(ds)
    
    stack = np.stack(slices, axis=0)
    return stack

#tiff_folder = 'D:/Projets/Python/3DAnalysis/tests/tiffStack'
#tiff_stack = open_tiff_stack(tiff_folder)
#print(tiff_stack.shape)

#def open_stack(folder_path,type):
#    match type:
#        case dicom:
#            open_dicom_stack(folder_path)
#        case tiff:
#            open_tiff_stack(folder_path)
            

def open_stack(folder_path,type):
    if type == 'dicom':
        stack = open_dicom_stack(folder_path)
    elif type == 'tiff':
        stack = open_tiff_stack(folder_path)
    return stack
        
        