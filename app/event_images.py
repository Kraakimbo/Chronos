"""Archive images (photo, tableau, portrait) for historical events.

Sourced from Wikimedia Commons (public domain / free license), one entry
per event slug (matches app.data.EVENTS). Each image type is optional --
not every event has a period photograph (photography did not exist before
~1839) or a well-documented painting. "credit" and "licence" should be
displayed next to the image per Commons attribution requirements.

NOTE: these URLs were compiled via web search and have not all been
individually opened to confirm the file still exists and the licence is
exactly as noted -- verify before relying on this in production. See
Chronos_archives_photos_tableaux_portraits.xlsx for the full research
notes, including entries still marked "introuvable".
"""

# Preferred image type for the event-detail page's cover banner: a scene
# (painting/engraving) reads best as a banner, then a period photo, and a
# portrait as the fallback -- every event has at least one of the three.
COVER_PRIORITY = ("tableau", "photo", "portrait")


def cover_image(slug):
    """Best available image for the event's cover banner, or None."""
    images = EVENT_IMAGES.get(slug, {})
    for image_type in COVER_PRIORITY:
        if image_type in images:
            return images[image_type]
    return None

EVENT_IMAGES = {
    'prise-de-la-bastille': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Anonyme_-_Prise_de_la_Bastille,_le_14_juillet_1789_(P707-1)_-_P707-1_-_Musée_Carnavalet.jpg',
            'subject': 'Prise de la Bastille (anonyme)',
            'credit': 'Musée Carnavalet',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_présumé_de_Bernard_Jourdan,_marquis_de_Launay_(1740-14_juillet_1789),_gouverneur_de_la_Bastille_01.jpg',
            'subject': 'Marquis de Launay (gouverneur de la Bastille)',
            'credit': 'Portrait anonyme',
            'licence': 'Domaine public',
        },
    },
    'prise-des-tuileries': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Jacques_Bertaux_-_Prise_du_palais_des_Tuileries_-_1793.jpg',
            'subject': 'Prise du palais des Tuileries, 10 août 1792',
            'credit': 'Jacques Bertaux, Musée national du Château de Versailles',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_de_Louis_XVI,_Antoine_François_Callet,_1779.jpg',
            'subject': 'Louis XVI',
            'credit': 'Antoine-François Callet',
            'licence': 'Domaine public',
        },
    },
    'assassinat-cesar': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Vincenzo_Camuccini_-_La_morte_di_Cesare.jpg',
            'subject': 'La Mort de César',
            'credit': 'Vincenzo Camuccini, Museo di Capodimonte',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bust_of_Julius_Caesar-Uffizi_Gallery.jpg',
            'subject': 'Buste de Jules César',
            'credit': 'Galerie des Offices',
            'licence': 'Domaine public',
        },
    },
    'alunissage-apollo-11': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Aldrin_Apollo_11_original.jpg',
            'subject': 'Buzz Aldrin sur la Lune',
            'credit': 'NASA (photo Neil Armstrong)',
            'licence': 'Domaine public (œuvre du gouvernement fédéral américain)',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Neil_Armstrong_pose.jpg',
            'subject': 'Neil Armstrong',
            'credit': 'NASA',
            'licence': 'Domaine public',
        },
    },
    'chute-mur-berlin': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Thefalloftheberlinwall1989.JPG',
            'subject': 'Chute du mur de Berlin, Porte de Brandebourg',
            'credit': 'Photo (1989)',
            'licence': 'CC (à vérifier sur la page fichier)',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/GorbachevMS.jpg',
            'subject': 'Mikhaïl Gorbatchev',
            'credit': 'Photo Lev L. Medvedev, 1991',
            'licence': 'CC-BY-SA 4.0',
        },
    },
    'debarquement-normandie': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Approaching_Omaha.jpg',
            'subject': 'Débarquement à Omaha Beach, 6 juin 1944',
            'credit': 'US Coast Guard / National Archives',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Dwight_D._Eisenhower,_official_photo_portrait,_May_29,_1959.jpg',
            'subject': 'Dwight D. Eisenhower',
            'credit': 'Photo officielle, 1959',
            'licence': 'Domaine public',
        },
    },
    'armistice-1918': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Armisticetrain.jpg',
            'subject': "Wagon de l'Armistice, Compiègne",
            'credit': "Photo d'époque, 1918",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/General_Ferdinand_Foch.jpg',
            'subject': 'Maréchal Ferdinand Foch',
            'credit': 'Photo',
            'licence': 'Domaine public',
        },
    },
    'declaration-independance-americaine': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Declaration_of_Independence_(1819),_by_John_Trumbull.jpg',
            'subject': "Déclaration d'Indépendance",
            'credit': 'John Trumbull, 1819, Rotonde du Capitole',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Thomas_Jefferson_by_Rembrandt_Peale,_1800.jpg',
            'subject': 'Thomas Jefferson',
            'credit': 'Rembrandt Peale, 1800',
            'licence': 'Domaine public',
        },
    },
    'arrivee-christophe-colomb': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/John_Vanderlyn_-_Columbus_Landing_at_Guanahani,_1492_-_WGA24269.jpg',
            'subject': 'Débarquement de Colomb à Guanahani',
            'credit': 'John Vanderlyn, Rotonde du Capitole',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ridolfo_del_Ghirlandaio_-_Ritratto_di_Cristoforo_Colombo_(1520).jpg',
            'subject': 'Christophe Colomb',
            'credit': 'Ridolfo del Ghirlandaio, 1520, Musée de la mer de Gênes',
            'licence': 'Domaine public',
        },
    },
    'nuit-du-4-aout': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Nuit_du_4_ao%C3%BBt_1789_abolition_of_the_privileges.jpg',
            'subject': 'Séance de la nuit du 4 août 1789',
            'credit': 'École française',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_de_Louis_XVI,_Antoine_Fran%C3%A7ois_Callet,_1779.jpg',
            'subject': 'Louis XVI',
            'credit': 'Antoine-François Callet, 1779',
            'licence': 'Domaine public',
        },
    },
    'bataille-de-waterloo': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Battle_of_Waterloo_(by_William_Sadler_II).jpg',
            'subject': 'Bataille de Waterloo',
            'credit': 'William Sadler II',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_the_Duke_of_Wellington_by_George_Hayter_1820.jpg',
            'subject': 'Duc de Wellington',
            'credit': 'George Hayter, 1820',
            'licence': 'Domaine public',
        },
    },
    'sacre-napoleon': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Le_Sacre_de_Napol%C3%A9on_-_Jacques-Louis_David_-_Mus%C3%A9e_du_Louvre_Peintures_INV_3699_%3B_MR_1437.jpg',
            'subject': 'Le Sacre de Napoléon',
            'credit': 'Jacques-Louis David, Musée du Louvre',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Painting_of_Napoleon_Bonaparte_by_Jacques-Louis_David,_1813.jpg',
            'subject': 'Napoléon Ier',
            'credit': 'Jacques-Louis David, 1813',
            'licence': 'Domaine public',
        },
    },
    'chute-de-constantinople': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Fall_of_Constantinople,.jpg',
            'subject': 'Chute de Constantinople 1453',
            'credit': 'Auteur non précisé (Commons)',
            'licence': 'Domaine public (à revérifier)',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Sultan_Mehmed_II_by_Gentile_Bellini_-_Fatih.jpg',
            'subject': 'Mehmed II le Conquérant',
            'credit': 'Gentile Bellini, 1480, National Gallery Londres',
            'licence': 'Domaine public',
        },
    },
    'signature-magna-carta': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Magna_Carta_(1215)_-_BL_Cotton_MS_Augustus_II_106.jpg',
            'subject': 'Document original de la Magna Carta (photo moderne)',
            'credit': 'British Library',
            'licence': 'Domaine public / CC (British Library)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/King_John_signing_the_Great_Charter_(Magna_Carta)_by_English_School.png',
            'subject': 'Signature de la Magna Carta par Jean sans Terre',
            'credit': 'École anglaise, ~1902',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/British_-_King_John_-_Google_Art_Project.jpg',
            'subject': 'Jean sans Terre',
            'credit': 'École britannique, Dulwich Picture Gallery',
            'licence': 'Domaine public',
        },
    },
    'eruption-vesuve': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Pompeii_Ruins_%26_Bronze_Statue_of_Daedalus_(48440549806).jpg',
            'subject': 'Ruines de Pompéi (photo moderne du site)',
            'credit': None,
            'licence': 'Domaine public / CC (à revérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Karl_Brullov_-_The_Last_Day_of_Pompeii_-_Google_Art_Project.jpg',
            'subject': 'Le dernier jour de Pompéi',
            'credit': 'Karl Brioullov, Musée russe',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Pliny_the_Elder.png',
            'subject': "Pline l'Ancien",
            'credit': 'Portrait posthume/imaginaire',
            'licence': 'Domaine public',
        },
    },
    'krach-de-1929': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Crowd_outside_nyse.jpg',
            'subject': 'Foule devant le NYSE, 29 oct. 1929',
            'credit': 'Photographe non identifié',
            'licence': 'Domaine public',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/19291030_Crash_of_%2729_-_New_York_Times.jpg',
            'subject': 'Une du New York Times, 30 oct. 1929',
            'credit': 'New York Times',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/President_Hoover_portrait.jpg',
            'subject': 'Herbert Hoover',
            'credit': 'Photographe officiel, 1928',
            'licence': 'Domaine public',
        },
    },
    'attaque-pearl-harbor': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/USS_Arizona_burning_Pearl_Harbor.jpg',
            'subject': 'USS Arizona en feu, 7 déc. 1941',
            'credit': 'US Navy',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Yamamoto_Isoroku.jpg',
            'subject': 'Amiral Isoroku Yamamoto',
            'credit': 'Photographe non identifié',
            'licence': 'Domaine public',
        },
    },
    'bombardement-hiroshima': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Atomic_cloud_over_Hiroshima.jpg',
            'subject': 'Champignon atomique, 6 août 1945',
            'credit': 'George R. Caron / US Army',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Harry_S_Truman,_bw_half-length_photo_portrait,_facing_front,_1945.jpg',
            'subject': 'Harry S. Truman',
            'credit': 'David Bell Edmonston, 1945',
            'licence': 'Domaine public',
        },
    },
    'capitulation-allemande-1945': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Field_Marshall_Keitel_signs_German_surrender_terms_in_Berlin_8_May_1945_-_Restoration.jpg',
            'subject': 'Wilhelm Keitel signant la capitulation à Berlin-Karlshorst',
            'credit': "Photo d'archive, restauration",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Wilhelm_Keitel.jpg',
            'subject': 'Wilhelm Keitel',
            'credit': "Photo d'identité militaire",
            'licence': 'Domaine public (présumé, à vérifier)',
        },
    },
    'vol-de-gagarine': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Yuri_Gagarin_(1961).jpg',
            'subject': 'Youri Gagarine, Helsinki, 3 juillet 1961',
            'credit': "Photo d'époque",
            'licence': 'Domaine public',
        },
        'tableau': {
            'url': "https://commons.wikimedia.org/wiki/Special:FilePath/The_Soviet_Union_1961_CPA_2562_stamp_(World's_First_Manned_Space_Flight._Rocket,_Gagarin_and_Kremlin).jpg",
            'subject': 'Timbre soviétique 1961',
            'credit': "Poste d'URSS (CPA 2562)",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Yuri-Gagarin-1961-Helsinki-crop.jpg',
            'subject': 'Youri Gagarine',
            'credit': 'Photo portrait, Helsinki 1961',
            'licence': 'Domaine public',
        },
    },
    'discours-i-have-a-dream': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Martin_Luther_King_Jr._addresses_a_crowd_from_the_steps_of_the_Lincoln_Memorial,_USMC-09611.jpg',
            'subject': 'MLK au Lincoln Memorial, 28 août 1963',
            'credit': 'Archives US Marine Corps',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Martin_Luther_King_Jr_NYWTS.jpg',
            'subject': 'Martin Luther King Jr.',
            'credit': 'New York World-Telegram & Sun collection, 1964',
            'licence': 'Domaine public',
        },
    },
    'revolution-doctobre': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/After_the_capture_of_the_Winter_Palace_26_October_1917.jpg',
            'subject': "Après la prise du Palais d'Hiver, 26 octobre 1917",
            'credit': "Photo d'archive",
            'licence': 'Domaine public',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ivan_Vladimirov_the-pogrom-of-the-winter-palace.jpg',
            'subject': '"The Pogrom of the Winter Palace", Ivan Vladimirov, 1917',
            'credit': 'Ivan Vladimirov',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Lenin_in_1920.jpg',
            'subject': 'Vladimir Lénine',
            'credit': 'Photo, 1920',
            'licence': 'Domaine public',
        },
    },
    'these-de-luther': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ferdinand_Pauwels_-_Luther_hammers_his_95_theses_to_the_door.jpg',
            'subject': 'Luther clouant ses 95 thèses',
            'credit': 'Ferdinand Pauwels',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Lucas_Cranach_-_Portrait_of_Martin_Luther_-_M.Ob.1757_-_National_Museum_in_Warsaw.jpg',
            'subject': 'Martin Luther',
            'credit': 'Lucas Cranach le Jeune, 1564',
            'licence': 'Domaine public',
        },
    },
    'liberation-mandela': {
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Nelson_Mandela_1994.jpg',
            'subject': 'Nelson Mandela',
            'credit': 'Photo, 1994',
            'licence': 'Domaine public / licence libre (à vérifier)',
        },
    },
    'lancement-spoutnik': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Sputnik_1.jpg',
            'subject': 'Spoutnik 1 (satellite / réplique)',
            'credit': "Photo d'archive",
            'licence': 'Domaine public',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/USSR_stamp_1957_CPA_2067.jpg',
            'subject': 'Timbre soviétique 1957',
            'credit': "Poste d'URSS (CPA 2067)",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Korolyov_(1934).jpg',
            'subject': 'Sergueï Korolev',
            'credit': 'Photo, 1934',
            'licence': 'Domaine public',
        },
    },
    'chute-empire-romain-occident': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Romulus_Augustulus_and_Odoacer.jpg',
            'subject': 'Romulus Augustule remettant la couronne à Odoacre',
            'credit': 'Illustration XIXe siècle',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Solidus_Romulus_Augustus-RIC_3406.jpg',
            'subject': 'Romulus Augustule (portrait numismatique)',
            'credit': 'Solidus, 475-476 apr. J.-C.',
            'licence': 'Domaine public',
        },
    },
    'invention-machine-vapeur-watt': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Watt_steam_pumping_engine.JPG',
            'subject': 'Machine à vapeur de Watt (artefact conservé, photo moderne)',
            'credit': "Photo moderne d'un exemplaire",
            'licence': 'CC/domaine public (à vérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/James_Eckford_Lauder_-_James_Watt_and_the_Steam_Engine-_the_Dawn_of_the_Nineteenth_Century_-_Google_Art_Project.jpg',
            'subject': 'James Watt concevant la machine à vapeur',
            'credit': 'James Eckford Lauder, 1855',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Beechey_James_Watt.jpg',
            'subject': 'James Watt',
            'credit': 'William Beechey',
            'licence': 'Domaine public',
        },
    },
    'decouverte-tombe-toutankhamon': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Tuts_Tomb_Opened.JPG',
            'subject': 'Ouverture de la tombe de Toutânkhamon, 1922',
            'credit': "Photo d'époque, fouilles Carter/Carnarvon",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Howard_Carter,_5-8-24_LOC_npcc.11276.jpg',
            'subject': 'Howard Carter',
            'credit': 'Library of Congress',
            'licence': 'Domaine public',
        },
    },
    'siege-de-bagdad-1258': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bagdad1258.jpg',
            'subject': 'Siège de Bagdad par les Mongols (1258)',
            'credit': 'Miniature persane, BnF Suppl. persan 1113',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Hulagu_Khan.jpg',
            'subject': 'Hulagu Khan',
            'credit': 'Miniature persane (Jami al-tawarikh)',
            'licence': 'Domaine public',
        },
    },
    'mort-de-barbe-noire': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Capture_of_the_Pirate_Blackbeard_1718_by_Jean_Leon_Gerome_Ferris.jpg',
            'subject': 'Capture/mort de Barbe Noire',
            'credit': 'Jean Leon Gerome Ferris',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Blackbeard_the_Pirate.jpg',
            'subject': 'Edward Teach dit Barbe Noire',
            'credit': 'Gravure, "A General History of the Pyrates" (1725)',
            'licence': 'Domaine public',
        },
    },
    'mort-de-gengis-khan': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mort_de_Djengiz_Kh%C3%A2n.jpeg',
            'subject': 'Mort de Gengis Khan',
            'credit': 'Miniature médiévale, "Maître Egerton"',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Genghis_Khan.jpg',
            'subject': 'Gengis Khan',
            'credit': 'Portrait posthume, album impérial Yuan',
            'licence': 'Domaine public',
        },
    },
    'traite-de-nankin': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Signing_of_the_Treaty_of_Nanking.jpg',
            'subject': 'Signature du traité de Nankin à bord du HMS Cornwallis',
            'credit': "D'après une peinture de John Platt",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/QiYing.jpg',
            'subject': 'Qiying',
            'credit': 'Portrait chinois XIXe s., auteur inconnu',
            'licence': 'Domaine public',
        },
    },
    'restauration-meiji': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Teenager_Meiji_Emperor_with_foreign_representatives_1868_1870.jpg',
            'subject': 'Empereur Meiji adolescent avec représentants étrangers, 1868-1870',
            'credit': "Photo d'époque",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Mutsuhito-Emperor-Meiji-1873.png',
            'subject': 'Empereur Meiji (Mutsuhito)',
            'credit': 'Photo officielle, Uchida Kuichi, 1873',
            'licence': 'Domaine public',
        },
    },
    'independance-de-linde': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Jawaharlal_Nehru_gives_his_%22tryst_with_destiny%22_speech_at_Parliament_House_in_New_Delhi_in_1947_(02).jpg',
            'subject': 'Nehru, discours "Tryst with Destiny", 15 août 1947',
            'credit': "Photo d'archive",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Pt_Jawaharlal_Nehru.jpg',
            'subject': 'Jawaharlal Nehru',
            'credit': 'Photo/portrait officiel',
            'licence': 'Domaine public',
        },
    },
    'bataille-dadoua': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ethiopian_painting,_Battle_of_Adwa,_1896.jpg',
            'subject': "Bataille d'Adoua, 1er mars 1896",
            'credit': 'Peinture éthiopienne anonyme',
            'licence': 'CC-BY-SA 4.0',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Emperor_Menelik_II.png',
            'subject': 'Ménélik II',
            'credit': "Photo d'époque",
            'licence': 'Domaine public',
        },
    },
    'conference-de-berlin': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Berlin_Conference,_1884%E2%80%9385.jpg',
            'subject': 'Ouverture de la conférence de Berlin, 1884-85',
            'credit': "Gravure de presse d'époque",
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bundesarchiv_Bild_183-R13234,_Otto_von_Bismarck.jpg',
            'subject': 'Otto von Bismarck',
            'credit': 'Bundesarchiv',
            'licence': 'CC-BY-SA 3.0 DE',
        },
    },
    'chute-de-tenochtitlan': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ruins_of_Tenochtitlan.JPG',
            'subject': 'Templo Mayor (site moderne)',
            'credit': 'Photo moderne des ruines du Templo Mayor, Mexico',
            'licence': 'CC-BY-SA (à vérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Conquista-de-M%C3%A9xico-por-Cort%C3%A9s-Tenochtitlan-Painting.png',
            'subject': 'Chute de Tenochtitlan',
            'credit': 'Juan et Miguel González, 1698',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Retrato_de_Hern%C3%A1n_Cort%C3%A9s.jpg',
            'subject': 'Hernán Cortés',
            'credit': 'Anonyme',
            'licence': 'Domaine public',
        },
    },
    'capture-datahualpa': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/El_cuarto_del_Rescate,_Cajamarca,_Peru.jpg',
            'subject': 'Cuarto del Rescate, Cajamarca (site moderne)',
            'credit': 'Photo moderne',
            'licence': 'CC-BY-SA (à vérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/La_Captura_de_Atahualpa_-_Juan_Lepiani_1920s.png',
            'subject': "Capture d'Atahualpa à Cajamarca",
            'credit': 'Juan Lepiani, années 1920, MALI',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Atahualpa_Inca_XIV.png',
            'subject': 'Atahualpa',
            'credit': 'Portrait XIXe s.',
            'licence': 'Domaine public',
        },
    },
    'cook-a-botany-bay': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Kurnell.JPG',
            'subject': 'Obélisque Captain Cook, Kurnell (site moderne)',
            'credit': 'Photo moderne du monument',
            'licence': 'CC-BY-SA (à vérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Landing_of_Lieutenant_James_Cook_at_Botany_Bay,_29_April_1770_(painting_by_E_Phillips_Fox).jpg',
            'subject': 'Débarquement de Cook à Botany Bay',
            'credit': 'E. Phillips Fox, 1902, NGV',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Captainjamescookportrait.jpg',
            'subject': 'Capitaine James Cook',
            'credit': 'Nathaniel Dance-Holland, c.1775',
            'licence': 'Domaine public',
        },
    },
    'fondation-de-sydney': {
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Founding_of_Australia._By_Capt._Arthur_Phillip_R.N._Sydney_Cove,_Jan._26th_1788.jpg',
            'subject': 'Fondation de la colonie de Sydney',
            'credit': 'Algernon Talmage, 1937',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Arthur_Phillip.jpg',
            'subject': 'Arthur Phillip',
            'credit': 'Francis Wheatley, 1786',
            'licence': 'Domaine public',
        },
    },
    'prise-de-jerusalem-par-saladin': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Jerusalem_Dome_of_the_rock_BW_1.JPG',
            'subject': 'Dôme du Rocher, Jérusalem (site moderne)',
            'credit': 'Berthold Werner',
            'licence': 'CC-BY-SA',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Jan_Lievens_Saladin_and_Guy_of_Lusignan.jpg',
            'subject': 'Saladin et Guy de Lusignan',
            'credit': 'Jan Lievens, c.1650',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Portrait_of_Saladin_(before_A.D._1185).jpg',
            'subject': 'Saladin',
            'credit': 'Portrait antérieur à 1185',
            'licence': 'Domaine public',
        },
    },
    'prise-de-grenade': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Granada._Alhambra._Exterior_de_la_mezquita,_norte_-_Garz%C3%B3n_fot%C3%B3grafo._LCCN2018646011.jpg',
            'subject': 'Alhambra de Grenade (photo ancienne du site)',
            'credit': 'Rafael Garzón, fin XIXe s., LOC',
            'licence': 'Domaine public',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/La_Rendici%C3%B3n_de_Granada_-_Pradilla.jpg',
            'subject': 'Reddition de Grenade',
            'credit': 'Francisco Pradilla Ortiz, 1882',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Ferdinand_of_Aragon,_Isabella_of_Castile.jpg',
            'subject': "Ferdinand II d'Aragon et Isabelle Ire de Castille",
            'credit': 'Portrait historique conjoint',
            'licence': 'Domaine public',
        },
    },
    'bataille-de-lepante': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Barcelona_Museu_Maritim_Galera_Real_01.jpg',
            'subject': 'Réplique de la Real (galère amirale)',
            'credit': 'Museu Marítim de Barcelone',
            'licence': 'CC-BY-SA (à vérifier)',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/The_Battle_of_Lepanto_by_Paolo_Veronese.jpeg',
            'subject': 'Bataille de Lépante',
            'credit': 'Paolo Veronese, 1571',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Jusepe_de_Ribera,_Equestrian_Portrait_of_Don_Juan_de_Austria,_1648,_NGA_38382.jpg',
            'subject': "Don Juan d'Autriche",
            'credit': 'Jusepe de Ribera, 1648',
            'licence': 'Domaine public',
        },
    },
    'bataille-de-panipat': {
        'photo': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Kabuli_Bagh_Mosque.JPG',
            'subject': 'Mosquée Kabuli Bagh, Panipat (site moderne)',
            'credit': 'Photo moderne, 2009',
            'licence': 'CC-BY-SA 3.0',
        },
        'tableau': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Battle_of_Panipat_(20_April_1526)._Baburnama_of_1598.jpg',
            'subject': 'Première bataille de Panipat',
            'credit': 'Illustration du Baburnama, 1598',
            'licence': 'Domaine public',
        },
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/Idealized_portrait_of_Babur_(1483-1530)_in_Persian_style,_painted_circa_1605-1615_in_India_(British_Museum_1921,1011,0.3).jpg',
            'subject': 'Babur',
            'credit': 'Peinture idéalisée, c.1605-1615',
            'licence': 'Domaine public',
        },
    },
    'independance-du-ghana': {
        'portrait': {
            'url': 'https://commons.wikimedia.org/wiki/Special:FilePath/A_portrait_of_Dr_Kwame_Nkrumah.jpg',
            'subject': 'Kwame Nkrumah',
            'credit': 'The National Archives (UK)',
            'licence': 'Domaine public (à vérifier)',
        },
    },
}
