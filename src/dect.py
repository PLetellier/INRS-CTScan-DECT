#Attenuation coefficient Bourque 2014
def rel_att_coeff(HU):
    return ( HU/1000+1 )

#Zeff Martini 2021
def z_eff_calc(mulow, muhigh):
    murel = mulow/muhigh
    a=31.6640
    b=-41.3636
    c=20.2761
    return ( a + b*murel + c*murel**2 )

#rho Martini 2021
def rho_calc(mu, zeff):
    rhow = 3.34*10**23
    d=0.0817
    e=0.0383
    f=0.0071
    return ( mu*rhow/(d + e*zeff + f*zeff**2) )

#main function to use in code
def detc_calc(HU_low, HU_high):
    mu_low = rel_att_coeff(HU_low)
    mu_high = rel_att_coeff(HU_high)
    zeff = z_eff_calc(mu_low, mu_high)
    rho = rho_calc(mu_low, zeff)
    return zeff, rho