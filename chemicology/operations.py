'''
Operations
----------
All methods, formulae, operations
'''

from database import element

class Empirical_foumula():
    '''Gives small whole number ratio between the atoms of different elements present in a compound'''

    def __init__(self, e_C_per, e_H_per, e_O_per):
        self.e_C_per = float(e_C_per)
        self.e_H_per = float(e_H_per)
        self.e_O_per = float(e_O_per)

    def gram_atoms(self):
        '''Finds gram atoms of C,H,O by percentage.'''

        self.e_C_n = self.e_C_per / element("carbon", "atomic_mass")
        self.e_H_n = self.e_H_per / element("hydrogen", "atomic_mass")
        self.e_O_n = self.e_O_per / element("oxygen", "atomic_mass")
        self.e_Total_n = [self.e_C_n, self.e_H_n, self.e_O_n]
        return self.e_Total_n
    
    def atomic_ratio(self):
        '''Finds atomic ratio between C,H,O by gram atoms.'''

        self.e_t_nm = min(self.e_Total_n)
        self.e_C_r = self.e_C_n / self.e_t_nm
        self.e_H_r = self.e_H_n / self.e_t_nm
        self.e_O_r = self.e_O_n / self.e_t_nm
        
        self.e_Total_r = [round(self.e_C_r, 2), round(self.e_H_r, 2), round(self.e_O_r, 2)]
        return self.e_Total_r
    
    def show_method(self):
        '''Gives Ful method of Empirical Formula'''

        e_C_ga = "No. of grams of Carbon = " + str(self.e_C_per) + "g / " + str(element("carbon", "atomic_mass")) + "gmol-1 = " + str(round(self.e_C_n, 2)) + "gram atoms"
        e_H_ga = "No. of grams of Hydrogen = " + str(self.e_H_per) + "g / " + str(element("hydrogen", "atomic_mass")) + "gmol-1 = " + str(round(self.e_H_n, 2)) + "gram atoms"
        e_O_ga = "No. of grams of Oxygen = " + str(self.e_O_per) + "g / " + str(element("oxygen", "atomic_mass")) + "gmol-1 = " + str(round(self.e_O_n, 2)) + "gram atoms"

        e_Total_ar = str(round(self.e_C_n, 2)) + " / " + str(round(self.e_t_nm, 2)) + " : " + str(round(self.e_H_n, 2)) + " / " + str(round(self.e_t_nm, 2)) + " : " + str(round(self.e_O_n, 2)) + " / " + str(round(self.e_t_nm, 2))
        e_Total_ara = str(round(self.e_C_r, 2)) + " : " + str(round(self.e_H_r, 2)) + " : " + str(round(self.e_O_r, 2))
        
        method_msg = e_C_ga + "\n" + e_H_ga + "\n" + e_O_ga + "\n\n" + e_Total_ar + "\n" + e_Total_ara
        return method_msg