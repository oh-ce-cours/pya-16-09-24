def chunks(lst, n):
    """Yield successive n-sized chunks from lst.
    From https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


tle_data = """     ISS (ZARYA)             
1 25544U 98067A   14273.50403866  .00012237  00000-0  21631-3 0  1790
2 25544  51.6467 297.5710 0002045 126.1182  27.2142 15.50748592907666
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
"""


lines = tle_data.split("\n")
lines = [l.strip() for l in lines if l]
