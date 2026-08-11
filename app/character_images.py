"""Portraits for secondary/supporting characters of historical events.

Complements app.event_images.EVENT_IMAGES, which only covers the ONE
main portrait per event. Sourced from Wikimedia Commons the same way --
see Chronos_archives_photos_tableaux_portraits.xlsx and the event_images
module docstring for the same caveats (not all URLs individually opened
to confirm the file/licence). Keyed by event slug -> character name
(must match app.data.EVENTS[slug]["characters"][i]["name"] exactly).
Not every character has an entry: some are collective groups ("Gardes
Suisses") with no individual to portray, others had no reliable Commons
file found.
"""

CHARACTER_IMAGES = {
    'prise-de-la-bastille': {
        'Louis XVI': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_de_Louis_XVI,_Antoine_Fran%C3%A7ois_Callet,_1779.jpg',
            'credit': 'Antoine-François Callet, 1779',
            'licence': 'Domaine public',
        },
        'C. Desmoulins': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Camille_Desmoulins,_Mus%C3%A9e_Carnavalet.jpg',
            'credit': 'Musée Carnavalet',
            'licence': 'Domaine public',
        },
    },
    'prise-des-tuileries': {
        'Marie-Antoinette': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Marie-Antoinette_en_chemise_ou_en_gaulle_-_Vers_1783_-_Elisabeth_Louise_Vig%C3%A9e_Le_Brun.jpg',
            'credit': 'Élisabeth Vigée Le Brun, v.1783',
            'licence': 'Domaine public',
        },
    },
    'assassinat-cesar': {
        'Brutus': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Michelangelo_Brutus.jpg',
            'credit': 'Buste de Michel-Ange, musée du Bargello',
            'licence': 'Domaine public',
        },
        'Marc Antoine': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Marble_bust_of_Mark_Antony_(Vatican_Museums).jpg',
            'credit': 'Buste en marbre, Musées du Vatican',
            'licence': 'CC-BY-SA 4.0',
        },
    },
    'alunissage-apollo-11': {
        'Buzz Aldrin': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Buzz_Aldrin.jpg',
            'credit': 'Portrait officiel NASA, 1969',
            'licence': 'Domaine public',
        },
        'Michael Collins': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Michael_Collins_(S69-31742).jpg',
            'credit': 'Portrait officiel NASA, 1969',
            'licence': 'Domaine public',
        },
    },
    'chute-mur-berlin': {
        'Günter Schabowski': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/G%C3%BCnter_Schabowski_-_Mutter_Erde_fec.JPG',
            'credit': 'Photo Mutter Erde',
            'licence': 'CC-BY-SA 4.0',
        },
        'Helmut Kohl': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Helmut_Kohl_(1996).jpg',
            'credit': 'Photo Christian Lambiotte, 1996',
            'licence': 'Domaine public / CC (à vérifier)',
        },
    },
    'debarquement-normandie': {
        'Charles de Gaulle': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/General_Charles_de_Gaulle_in_1945.jpg',
            'credit': 'Photo officielle, 1945',
            'licence': 'Domaine public',
        },
        'Erwin Rommel': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv_Bild_146-1973-012-43,_Erwin_Rommel.jpg',
            'credit': 'Bundesarchiv, Bild 146-1973-012-43',
            'licence': 'CC-BY-SA 3.0 de',
        },
    },
    'armistice-1918': {
        'Georges Clemenceau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Georges_Clemenceau_(profil)_-_photo_Paul_Nadar.jpg',
            'credit': 'Photo Paul Nadar',
            'licence': 'Domaine public',
        },
    },
    'declaration-independance-americaine': {
        'Benjamin Franklin': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Benjamin_Franklin_by_Joseph_Duplessis_1778.jpg',
            'credit': 'Joseph Siffred Duplessis, Smithsonian',
            'licence': 'Domaine public',
        },
        'George Washington': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Gilbert_Stuart,_George_Washington_(Lansdowne_portrait,_1796).jpg',
            'credit': 'Gilbert Stuart, National Portrait Gallery',
            'licence': 'Domaine public',
        },
    },
    'arrivee-christophe-colomb': {
        'Isabelle Ire de Castille': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/IsabellaofCastile03.jpg',
            'credit': 'Musée du Prado',
            'licence': 'Domaine public',
        },
    },
    'nuit-du-4-aout': {
        'Vicomte de Noailles': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Louis-Marie_Vicomte_de_Noailles_Gilbert_Stuart_1798.jpeg',
            'credit': 'Gilbert Stuart, 1798, Met',
            'licence': 'Domaine public',
        },
    },
    'bataille-de-waterloo': {
        'Napoléon Ier': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Francois_Gerard_-_Napoleon_Ier_en_costume_du_Sacre.jpg',
            'credit': 'François Gérard, Fontainebleau',
            'licence': 'Domaine public',
        },
        'Maréchal Blücher': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Peter_Edward_Stroehling_-_Portr%C3%A4t_Gebhard_Leberecht_von_Bl%C3%BCcher.jpg',
            'credit': 'Peter Edward Stroehling',
            'licence': 'Domaine public',
        },
    },
    'sacre-napoleon': {
        'Joséphine de Beauharnais': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Josephine_de_Beauharnais-Gerard.jpg',
            'credit': 'François Gérard, Fontainebleau',
            'licence': 'Domaine public',
        },
        'Pape Pie VII': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Louis_david,_ritratto_di_pio_VII_chiaramonti,_1805.JPG',
            'credit': 'Jacques-Louis David, 1805, Louvre',
            'licence': 'Domaine public',
        },
    },
    'chute-de-constantinople': {
        'Constantin XI': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Constantine_Palaiologos.jpg',
            'credit': 'Portrait posthume, auteur inconnu',
            'licence': 'Domaine public',
        },
    },
    'eruption-vesuve': {
        'Pline le Jeune': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Pliny_the_Younger.jpg',
            'credit': "Gravure d'après un portrait ancien",
            'licence': 'Domaine public',
        },
    },
    'attaque-pearl-harbor': {
        'Franklin D. Roosevelt': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Franklin_Delano_Roosevelt,_Portrait_1933.jpg',
            'credit': 'Photo officielle, Elias Goldensky, 1933',
            'licence': 'Domaine public',
        },
    },
    'bombardement-hiroshima': {
        'Hirohito': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Emperor_Hirohito_1928.jpg',
            'credit': 'Portrait officiel du couronnement, 1928',
            'licence': 'Domaine public',
        },
    },
    'capitulation-allemande-1945': {
        'Dwight D. Eisenhower': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Dwight_D._Eisenhower,_official_photo_portrait,_May_29,_1959.jpg',
            'credit': 'Photo officielle Maison Blanche, 1959',
            'licence': 'Domaine public',
        },
        'Joseph Staline': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Joseph_Stalin,_1950.jpg',
            'credit': 'Photo officielle soviétique, 1950',
            'licence': 'Domaine public',
        },
    },
    'vol-de-gagarine': {
        'Sergueï Korolev': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Sergei_Korolev_portrait.jpg',
            'credit': 'Portrait photographique officiel',
            'licence': 'Domaine public',
        },
    },
    'discours-i-have-a-dream': {
        'John Lewis': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/John_Lewis_1964-04-16.jpg',
            'credit': 'US News & World Report, 1964',
            'licence': 'Domaine public',
        },
    },
    'revolution-doctobre': {
        'Alexandre Kerenski': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Alexander_Kerensky_1917.jpg',
            'credit': 'Photo, Library of Congress, 1917',
            'licence': 'Domaine public',
        },
    },
    'these-de-luther': {
        'Johann Tetzel': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Johann_tetzel.jpg',
            'credit': "Gravure d'époque",
            'licence': 'Domaine public (à vérifier)',
        },
    },
    'liberation-mandela': {
        'Frederik de Klerk': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Frederik_Willem_de_Klerk.jpg',
            'credit': 'World Economic Forum, Davos 1992',
            'licence': 'CC-BY-SA 2.0',
        },
    },
    'lancement-spoutnik': {
        'Nikita Khrouchtchev': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Nikita_Khrushchev_1960.jpg',
            'credit': 'Library of Congress, 1960',
            'licence': 'Domaine public',
        },
    },
    'chute-empire-romain-occident': {
        'Odoacre': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Coin_of_Odoacer_at_the_British_Museum.png',
            'credit': 'Monnaie antique, British Museum',
            'licence': 'Domaine public',
        },
    },
    'invention-machine-vapeur-watt': {
        'Matthew Boulton': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/William_Beechey_(1753-1839)_-_Matthew_Boulton_(1728%E2%80%931809)_-_2003.0007.44_-_Birmingham_Museums_Trust.jpg',
            'credit': 'William Beechey, Birmingham Museums Trust',
            'licence': 'Domaine public',
        },
    },
    'decouverte-tombe-toutankhamon': {
        'Lord Carnarvon': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Lord_Carnarvon_(4674086).jpg',
            'credit': 'National Media Museum (Flickr Commons)',
            'licence': 'Domaine public',
        },
        'Toutânkhamon': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Tutankhamun_Mask.JPG',
            'credit': 'Masque funéraire, Musée égyptien du Caire',
            'licence': 'CC BY-SA 2.5',
        },
    },
    'siege-de-bagdad-1258': {
        "Al-Musta'sim": {
            'url': "https://commons.wikimedia.org/wiki/Special:FilePath/The_Caliph,_al-Musta'%E1%B9%A3im,_brought_before_H%C5%ABl%C4%81g%C5%AB_Kh%C4%81n_(miniature)._Folio_89v_(British_Library,_Or_2780).jpg",
            'credit': 'Miniature, British Library Or.2780',
            'licence': 'Domaine public',
        },
    },
    'traite-de-nankin': {
        'Henry Pottinger': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Henry_Pottinger_(crop).jpg',
            'credit': "D'après Sir Francis Grant",
            'licence': 'Domaine public',
        },
    },
    'restauration-meiji': {
        'Tokugawa Yoshinobu': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/1867_Osaka_Yoshinobu_Tokugawa.jpg',
            'credit': 'Photographie, 1867',
            'licence': 'Domaine public',
        },
    },
    'independance-de-linde': {
        'Mahatma Gandhi': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mahatma-Gandhi,_studio,_1931.jpg',
            'credit': 'Photo studio, Londres 1931',
            'licence': 'Domaine public',
        },
    },
    'bataille-dadoua': {
        'Taytu Betoul': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Taitu_Betul_v_d.jpg',
            'credit': 'Photographie, coll. domaine public',
            'licence': 'Domaine public',
        },
    },
    'conference-de-berlin': {
        'Léopold II': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Leopold_II,_King_of_the_Belgians_by_Alexander_Bassano_(1889).jpg',
            'credit': 'Photo Alexander Bassano, 1889',
            'licence': 'Domaine public',
        },
    },
    'chute-de-tenochtitlan': {
        'Cuauhtémoc': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Cuahtemoc.jpg',
            'credit': 'Peinture, XIXe siècle',
            'licence': 'Domaine public',
        },
    },
    'capture-datahualpa': {
        'Francisco Pizarre': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Francisco_Pizarro.jpg',
            'credit': 'Amable-Paul Coutan, Musée de Versailles',
            'licence': 'Domaine public',
        },
    },
    'cook-a-botany-bay': {
        'Joseph Banks': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Joseph_Banks_1773_Reynolds.jpg',
            'credit': 'Joshua Reynolds, 1773',
            'licence': 'Domaine public',
        },
    },
    'prise-de-jerusalem-par-saladin': {
        'Guy de Lusignan': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Guido_di_Lusignano.jpg',
            'credit': 'François-Édouard Picot, Versailles',
            'licence': 'Domaine public',
        },
    },
    'prise-de-grenade': {
        'Boabdil': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Boabdil-el-Chico.jpg',
            'credit': "Alfred Dehodencq, Musée d'Orsay",
            'licence': 'Domaine public',
        },
    },
    'bataille-de-lepante': {
        'Ali Pacha': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ali_Pasha.jpg',
            'credit': 'Gravure/portrait ancien',
            'licence': 'Domaine public (à vérifier)',
        },
    },
    'bataille-de-panipat': {
        'Ibrahim Lodi': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ibrahim_Lodi_at_the_Battle_of_Panipat_(1526).jpg',
            'credit': 'Miniature moghole, 1526',
            'licence': 'Domaine public',
        },
    },
}


def character_image(slug, name):
    """Portrait for a named character of an event, or None."""
    return CHARACTER_IMAGES.get(slug, {}).get(name)
