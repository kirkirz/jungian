"""Dimensionality module"""

# this combinates neatly with pos()
# since you can tell which function corresponds to some IME in a sociotype


# The dimensions are:
# 4D : Ex, Nr, St, Tm
# 3D : Ex, Nr, St
# 2D : Ex, Nr
# 1D : Ex
# These weren't added to function output (for interface simplicity)
def dim(function: int) -> str:
    """Calculate dimensionality of a function, given its position in Model A"""
    if function in (1, 8):
        return "4D"
    if function in (2, 7):
        return "3D"
    if function in (3, 6):
        return "2D"
    if function in (4, 5):
        return "1D"
    raise ValueError(f"Invalid position: {function}. Must be 1-8.")
