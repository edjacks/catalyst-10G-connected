Help on module get10Gconnected:

NAME
    get10Gconnected - Retrieve information on any TenGig Ethernet interfaces.

FILE
    /cygdrive/z/edjacks/files/<removed>/2016/20160816__search-for-3850-2-nm-10g/get10Gconnected.py

DESCRIPTION
    Log into a seed switch, find any CDP neighbors, and subsequently
    list all connected TenGigabit Ethernet interfaces that are found
    on those neighboring switches.
    
    This was used to look for any Cisco C3850 switches that had any
    NM-2-10G modules that included both 2x 1G and 2x 10G ports in
    use.
    
    20160817 - edjacks@cisco.com

FUNCTIONS
    jumphost_login(user, password)
        Log into the jump host
    
    main()
        Main function.
        
        1) Get credentials from user
        2) Log into jump host
        3) Log into seed switch
        4) Find CDP neighbors
        5) Log into each CDP neighbor
        6) Generate list of connected 10G interfaces on neighbor
        7) Save data to neighbor specific file

DATA
    seed_switch = 'switch.<removed>.com'


