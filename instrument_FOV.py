def instrument_FOV(FOV_size):
    
    """

    Modify the file output of Instrument Footprint Editor
    provided by Aladin with a user FOV size.

        http://aladin.u-strasbg.fr/footprint_editor/#
    
    """


    from send_Aladin_image import send_Aladin_image
    
    import warnings
    
    # ignore all warnings from Astropy
    from astropy.utils.exceptions import AstropyWarning

    warnings.simplefilter('ignore', category=AstropyWarning)

    
    from astropy.io.votable import parse
    
    # download an Aladin Instrument Footprint file from GitHub
    # or making it from http://aladin.u-strasbg.fr/footprint_editor/#
    
    # Reading the Instrument Footprint file template
    votable = parse("footprint_GWsky2.vot")

    # get table in the file (FOV size)
    table = votable.get_first_table()

    
    # get the data in the array member variable:
    data = table.array

    # Convert FOV size degree to arcsecond

    FOV_size_arcsec = FOV_size*3600

    
    # user FOV size
    data[0] = - FOV_size_arcsec /  2.0,   FOV_size_arcsec / 2.0
    data[1] =   FOV_size_arcsec /  2.0,   FOV_size_arcsec / 2.0
    data[2] =   FOV_size_arcsec /  2.0, - FOV_size_arcsec / 2.0
    data[3] = - FOV_size_arcsec /  2.0, - FOV_size_arcsec / 2.0

    # outputting a VOTable file
    votable.to_xml('instrument_FOV.vot')
    
    # send to aladin the instrument_FOV.vot
    send_Aladin_image('instrument_FOV.vot')

    

     