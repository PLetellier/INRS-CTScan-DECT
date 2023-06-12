import open_images as op
import numpy as np
import dect
import matplotlib.pyplot as plt


#Open CT data
#70kV
folder = 'D:/Projets/Python/3DAnalysis/tests/dect/GL23-20A-IIa-Un_70KV_D45s'
type = 'dicom'
stack_70kv = op.open_stack(folder,type)

#140kV
folder = 'D:/Projets/Python/3DAnalysis/tests/dect/GL23-20A-IIa-Un_140KV_D45s'
type = 'dicom'
stack_140kv = op.open_stack(folder,type)

#DETC calculation
[zeff, rho] = dect.detc_calc(stack_70kv, stack_140kv)



#threshold_value = filters.threshold_otsu(stack)
#threshold_low = 32000
#threshold_high = 45000
#binary_stack = np.logical_and(stack > threshold_low, stack < threshold_high)


#plotting results
plt.subplot(1,3,1)
plt.imshow(stack_140kv[:,250,:])
plt.title("140 kV")

plt.subplot(1,3,2)
plt.imshow(zeff[100,:,:])
plt.title("Zeff")

plt.subplot(1,3,3)
plt.imshow(rho[100,:,:])
plt.title("Rho")

plt.show()



