"""Dimensionality module"""
# this is could to combinate with pos()
# since you can tell which function corresponds to some IME in a sociotype

# The dimensions are:
# 4D : Ex, Nr, St, Tm
# 3D : Ex, Nr, St
# 2D : Ex, Nr
# 1D : Ex
# These weren't added to function output (for interface simplicity)
def dim(function : int) -> str:
    """Calculate dimensionality of a function, given its position in Model A"""
    if function == 1 or function == 8:
        return "4D"
    if function == 2 or function == 7:
        return "3D"
    if function == 3 or function == 6:
        return "2D"
    if function == 4 or function == 5:
        return "1D"
