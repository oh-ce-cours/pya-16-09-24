import multiprocessing
import time


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
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
ISS DEB [TOOLBAG]       
1 33442U 98067BL  09215.54829407  .13008691  12713-4  15349-3 0  3986
2 33442 051.6268 036.9885 0007699 292.6234 072.1768 16.49476607 40751
"""


def parsing_triplet(triplet: list) -> dict:
    time.sleep(10)
    res = {}
    name, ligne1, ligne2 = triplet
    if ligne1[0] != "1":
        raise Exception("c'est pas bon ligne 1")
    if ligne2[0] != "2":
        raise Exception("c'est pas bon ligne 2")
    res["name"] = name
    elements_ligne_1 = ligne1.split()
    elements_ligne_2 = ligne2.split()

    labels_ligne_1 = [
        "champ11",
        "champ12",
        "champ13",
        "champ14",
        "champ15",
        "champ16",
        "champ17",
        "champ18",
        "champ19",
    ]

    if len(elements_ligne_1) != 9:
        raise Exception(
            f"pas le bon nombre d'éléments dans la ligne 1 on en a {len(elements_ligne_1)}, attendu 9"
        )

    dico_ligne_1 = {
        label: value for label, value in zip(labels_ligne_1, elements_ligne_1)
    }
    labels_ligne_2 = [
        "champ21",
        "champ22",
        "champ23",
        "champ24",
        "champ25",
        "champ26",
        "champ27",
        "champ28",
        "champ29",
    ]
    dico_ligne_2 = {
        label: value for label, value in zip(labels_ligne_2, elements_ligne_2)
    }

    # dico_ligne_1 = {}
    # dico_ligne_1["champ11"] = ligne1[0].strip()
    # dico_ligne_1["champ12"] = ligne1[2:7].strip()
    res.update(dico_ligne_1)
    res.update(dico_ligne_2)
    return res


lines = tle_data.split("\n")
lines = [l.strip() for l in lines if l]
items = list(chunks(lines, 3))


if __name__ == "__main__":
    print(f"Il y a {len(items)} items à parser")
    with multiprocessing.Pool(15) as p:
        print(p.map(parsing_triplet, items))
