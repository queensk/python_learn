import re

from numpy import mat
students = """
•	Nebiyu Aklilu - Yelbeneh Abayneh Assefa 
•	Roland Sankara - Makube Ouma 
•	Uyoyou Uwuseba - Promise Okere 
•	Israel Adewumi - Moses Erhinyodavwe 
•	Kevin Mwole - Francis Gitau 
•	Favour Pondei - Oladipupo Kukoyi 
•	Monagane Morapedi - Ole Morapedi 
•	Jubilee Oghenerukome - Dammy Babarinde 
•	Nemera Bellachew - Bonsh Shafik 
•	Onuche Abah - Naheem Adebisi 
•	McRich Ehimigbai - Eraga Abu 
•	Oluwaferanmi Idowu - Emmanuel Ekundayo Agbaje Agbaje 
•	Eric Asamoah-Boateng - Emmanuel Gyateng 
•	Vivian Opondo - Joshua Muwanguzi 
•	Mishak Nwakpa - Beza Mersha 
•	innocent thomas - Robleh Xasan 
•	Abel Gebreyohannis - Kennedy Tabitha 
•	Paul Asukwo - Victor Nice 
•	Abreham Mirgeza - Keeno Matthee 
•	Tebogo Masete - Miracle Agbo 
•	Monwa Sithaba - Elizabeth Taiwo 
•	Cent Kanayo Nwebia - Olusegun Alawode 
•	Nahom Getenet - Makafui Kwawu kofi 
•	Christian Nebo - Jentrix WAMEYA 
•	John Iluyemi - George George 
•	Inyang Johnson Inyang - Alem Zerfu 
•	Ajibola Deborah - Bereket Adamsseged 
•	Seid Hamid Muhammed - Kebede Desta 
•	Frank Akuchie - Bisrat Ashagre 
•	ITUMELENG Mokwena - Keitumetse Mokwena 
•	Benson Macharia - Scolar Njuguna 
•	Saad ABDULLAHI - Solomon Ezeatum 
•	Abel Wubshet - Mikias kegnlyew 
•	Leonard Oriobor - Oluwaseyanu Onasanya 
•	Seyi Oke - Dagn Marilign 
•	Kam ALIDOU - Bolton Kogada 
•	netsimj Meja - Yemsrach Sinu 
•	Mariana Amadi - Richard Asuwe 
•	Umar Ahmad - Isaac Oluwagbemi 
•	Chimezie Onwudiwe - Monica Ejikang 
•	BLESSING PAUL - Pelumi Olalekan 
•	getachew Berhe - Fraol Beyene 
•	Cal Gizaw - Kofi Yesuko Kofi 
•	Caroline WAMBUI - Blessed Nyabereka 
•	OLAJIDE ADEBAMIPE - Abiodun abiodun 
•	Vector Temi - Abiud Nyamache 
•	Naol Mamo - Ikenna Oguejiofor 
•	Chioke Tochukwu Tochukwu - Frank OMUJI 
•	Mubarak Olajuwon - Rukaya Haruna 
•	Josh Mordi - Ifenna Onwuagana 
•	Odii Odii - Doris Okodugha 
•	Osayamwen Iwinosa - Odiase Odiase 
•	Ahmed Hassan - Mark Arinda 
•	Kingsley Ibrahim - Jeremy John John 
•	Mhiret Bekalu - Eual Girma 
•	Samuel Osunsakin - francisco kaunda 
•	EMMANUELGOSPEL Gospel 
•	Brian Odhiambo - Claire Njeri 
•	Amiolemhen Anita - Brian Munene 
•	Abebe Birhanu - Simon Michael 
•	Mariam Tomori - Ama Bentil 
•	Habeeb SULEIMAN - Aristide YAO 
•	Geoffrey Geoffrey - Mohamed Hussein 
•	Adeyemi Ige - Peter Adewole 
•	Mercy Okon - Ekeh Miracle Ihechi-Tabitha 
•	Kingsley Oweku - Adebayo Stephen 
•	Brian Bassey - Abdulbasit Akingbade 
•	Omoso Clinton Omoso - Okumu Hillary 
•	Henok Endeshaw - Edwin Enchill 
•	Michael Tubi - Sheyi Gaji 
•	Chima Nnachi - Jasper Oghenerukevwe 
•	Leonnie Okojie - William Kelechi 
•	Joshua Bolorunduro - Ifeanyi Ani 
•	Edwin Gichuhi - Dein Aaron 
•	Bukola Adegboyega - Alfred Koomson 
•	EGWU Ogbonnia - Tolu Oladosu 
•	Maureen Maurice - Gountane KANTCHO 
•	Victor Marcus-otu - Alvin Mwandoe 
•	Segun Olawale - Damilola Kuteyi 
•	Bekalu Tilahun - Rebecca Christiana Folarin Folarin 
•	Ugochukwu Nnaji - Osayuwamen Uwadiae 
•	Cameron Gramanie - Deji Dankuwo 
•	David Olatoye - Jonathan Ihejirika 
•	Mark Obi - Emmanuel Myles 
•	Tiffany Kariuki - Yosief Kidane 
•	Fisayo Adeniji - Rasheed Olayanju 
•	Victor ONYEWUCHI - Aniekan Thompson 
•	Daniel Onikola - Alexander Akerele 
•	sharon wanjiru - Daniel Agu 
•	Claudio Kimani - lumori simon 
•	isaac Tolesa - Lebogang Mokoena 
•	Farida Adamu-Ibrahim - #King Obinna 
•	Vongai Gaviro - Balogun Adedotun 
•	David Ugbabe - Victory Psalms NWORIE 
•	Babatunde Osifodunrin - Taiwo Shodamola 
•	Shadrach Akong - Abdulbadiu Sule 
•	Frankline Kiptoo - Sery Sesery 
•	Frank Idowu - Maximuele Okot 
•	Ayanfisco Ojo - vwairhe Okolosi 
•	JOY Chepchirchir - Chino Chinedu 
•	Leantan Yemane - Kawthar Babatunde 
•	OJUOLA OJUOLA - Zion Moses 
•	Ukoette Akpan - Mercy Kimaiyo 
•	Yusuf Adebayo - Mintesinot Habtegiorgis 
•	Dan Kioko - Meshack Musembei 
•	TEDDY BEYENE - Ezeh Chimezie 
•	Andino Joe - Edna Nkatha Kijogi 
•	Yoseph Kifle - Hibreselam Dejene 
•	Charles Igweonu - Fiifi Asare-Kumi Asare-Kumi 
•	Stephen Ataga - Taofeek Bello Bello 
•	Ife Owolabi - JANE Ngugi 
•	Ughasi Peter - Bakare Muideen Adeleke Adeleke 
•	Solomon UMOH - Godstime Barida 
•	Isaac Abraham - Hora Terefe 
•	Annie Wachana - Peter Odira 
•	Josephine Chialuka - Michael Sarkodie 
•	Simon Wanjira - Mohamed Ayman 
•	ALLAN NYAGI - Elias NGUMBA 
•	Thomas Conteh - Victor Nnoju 
•	Ernest Gichuhi - BENSON KAMAU 
•	Moyinoluwa Abass - Alfred Apenteng 
•	Iyanu Abolarin - COSTEDIAN 
•	David ONwuli - Koxy G Eyaadah 
•	Munge Kariuki - Ahmad Abdulazeez 
•	Sharon Olatunji - Josephine Uwuilekhue 
•	Nnaemeka Okoli - Emmanuel Joe Ochigbo 
•	Goodness Jolayemi - YOHANNES Ketema 
•	Blessed wonder Okotie - ADINDU OGECHUKWU 
•	Justice Chukwudi - Chinagorom Njoku 
•	Lerato Ncwadi - Tshegofatso Tswai 
•	Emmanuel Asante - Benie Chika 
•	Nicholas Muyimbwa - Motaz Hassan 
•	Ruth Matheri - Sakim Njoroge 
•	Kero Filicha - chidinma Egbu 
•	Opeyemi Akanbi - onyeme Ozioma 
•	Paul Saferio - Joseph Ndegwa 
•	Niitembu Augustinus - Franklin Igah 
•	Nathan Kirimi - Mintesinot kasa weldesenbet Mintesinot 
•	Mohammed Hamdoun - Kate Ouma 
•	Dominion DOMINION - Zubaidat Salaudeen 
•	Jire Shittu - Geoffrey Ongoro 
•	Muhindo Gift - Martin Njeri 
•	Isabella UMEH - Mureti Gitije 
•	Aman Gebretsadik - Tsegaab Sawo 
•	ADEWOLE Oluwanifemi - Yusuf Adeoye 
•	Ogunwoye Johnson - Gbolahan KOLAWOLE 
•	Mostafa Neamatalla - Tobi Amoniyan 
•	Ali ABDALLA - Austin Naulikha 
•	Becca Peters - Papa ahmadou fall fall 
•	Diamond Joseph - Oluwafemi Ogundare 
•	Israel Dereje Tekle - Bereket Tadesse 
•	Offiong Peter - Bienvenu GBETI 
•	Arnold Afayedor - Joseph Dessouassi 
•	Phillip Kyule - Kate Navisino 
•	Adeleke Adeola - Muslymarh Olaniyi 
•	Cheikh DIALLO - JBoy Oluwatosin 
•	Brandon Mothupi - Mojalefa Sikisi 
•	Allan Ngwae - Calvin Mwangi 
•	Eme NAYO - Oliver Ugwi 
•	Fnan Tedros - Esrom Abrha 
•	Dara Oluwadaramola - Princess Dada 
•	Gathoni Kiiru - Khadija Osman 
•	Dave Hailu - birra haile 
•	Eugene Oyier - Rogena Antony Owande Rogena 
•	ODERA ODERA - Cisca Chidobe 
•	Sosthenes Nyakeri - Otuekong Paul 
•	Tolani david - Mayi Nambalirwa 
•	SETA Donati - Nnamdi Alozie 
•	Sayid Abdi - Farhan Mohamud 
•	Barock Ololo - Simon Nguthu 
•	Mundia Gitonga - Maureen Korir 
•	Onanefe Idjerhe - Olumide Adebanjo 
•	Cornelius Cornelius - Mohammed Tawfiq Iddrisu 
•	Aishat Shaibu Nene - Kieran Mwangi 
•	Robel Adane - Robel_Adugna Robi 
•	Kipyegon Rotich Rotich - Diana Kyalo 
•	Chima Emenike - Nichodemus Abia 
•	Abraham Fatoki - Ermiyas Fisha 
•	Dejene Mulugeta - Salem Olaoye 
•	Oluwatobi Kayode - Lois Onyeanuforo 
•	EMwende Wanza - Saleh IBRAHIM 
•	Mustapha Sadiku - OMONDI Masika 
•	Everest Obot - Ayock Daniel 
•	Bukunmi Ojo-David - PD Doshi 
•	Faizol Kehinde - CAROLYNE MACHARIA 
•	Abby Wamaina - Princewill EMEKA 
•	Idowu Agboola - Ajgesh Ajiboye 
•	Joshua Shaola - Ogundeko Adebukola 
•	Elsa Desta - Jonah Apagu 
•	Debbie Olofin - Paul Okoli 
•	Maureen Oguche - Deborah Thomas 
•	Glory Ebube - Kelly Allan Mungai 
•	Romuald valere Ndigui ntamack - Billy Armel Essaga Anaba 
•	Benjamin George Obbo Obbo - Yiga BUDALAH 
•	Collins Nasong'o - Lema Lemayian 
•	George Junior Adomako - Horsfall Horsfall 
•	Martins Adegboyega - Damola Bamigboye 
•	mightGuy Onyejeme - Goodness Mbakara 
•	Samuel Theophilus - Ella Abang 
•	Esosa Omoigui - Emmanuel Ekete 
•	Nuel Eigbadon - Oluwafunbi Adeneye 
•	Olivia Wairimu - ColdQuiver Mwaura 
•	Jedidiah Ezana - Daniel Micah 
•	John KIPNGENO - STEPHEN DAVID DAVID 
•	Rasheed ADEJARE - Adullam Udo 
•	Anthony Wairiah - PETER MUTINDA 
•	John Akande - FIDELIS KANU 
•	opata ebubechukwu - Joyce John 
•	Julius Ossai - SHILLAH Psoboi 
•	Haleluya Amde - Dawit Alemayehu 
•	Kehinde joy Odumesi - Aniebiet Afia 
•	Theophilus Uwanogho - Rihana A Ali 
•	lilian okereke - Prosper Asema 
•	Temi Bowoto - Jeff Bwalya 
•	MOHAMED Ahmed - ABDOU-AKIM GBADAMASSI GBADAMASSI 
•	Charles Adure - Rume Dolor 
•	Janet Bitutu - Martins James 
•	David Nkwabi Hezron - AHMED ABDIWELI 
•	Alex Maina - Dibora Geremew Bezabeh 
•	Osaro OJO - Abdulrahman Gaya 
•	Emmanuel Lawal - Tamrat Feleke 
•	JO Birhanu - Opetunde Ibitoye 
•	Kodjo Justin Frederic AMAGLO-AFFATCHAWO - Tamunoibim Jaja 
•	Isaac Isaac - Innocent Oichoe 
•	Florida Korir Korir - Juliet Wangoi 
•	Kemi Osatohanmwen - Emmanuella Okonkwo 
•	Ebby Jerop - Collins Chumba 
•	Bradley Kibwana - Koki Koki 
•	Gift Mabasa - Seun Ajayi 
•	Ernest Thompson - Girum Getachew 
•	Chinedu Opara - Uju Sophia 
•	Rob Agai - Mise Wanjira 
•	CHUKWUEMEKA Dan-Chuku - Omotolani Okerinde 
•	Abraham Oladayiye - Mamadou Kane 
•	Joe Smith Joseph - Paul Adansi 
•	Temesgen Kelemework - Vincent Mabeka 
•	Chiiamaka Umoh - Kwanele Mthethwa 
•	Eunice Akinwande - Eman Tekle 
•	yoseph Tefera - Agoa Andrew 
•	Ilyas Osman 
•	Salami Adaviruku - Abdulrasheed Abdulrazaq 
•	Dagi Elias - Kirubel Getaneh 
•	ODUNAYO OGUNLEYE - Alfie265 Menyere 
•	Olaoluwa Isogun - Chris Nwaekpe 
•	Muiz Oyebowale - Patrick Ogadi 
•	Ayub Ibrahim - Diana Syombua 
•	Damola Oke - Eneojo Victor 
•	Lidya Assale - Yunus_abdul . 
•	Cyrus Mbatia - Katlego Dipitso 
•	Abdulrahman Al-awal - Rilwan Temitope 
•	Marcelino Nnatu - Ephraim ATTITSOGBE 
•	muli WAMBUA - Michael Wanjiru 
•	Chidiebere Uhegbu - Atalel Wubie 
•	Luke Olawale - Bitrus Dauda 
•	Benjamin Amui - Jeremy Ntuk Ntuk 
•	Lawrence Oragwa - Joshua mochama 
•	Faith Okosun - Adewemimo Adewale 
•	James Okwoche - Thando Siluma 
•	Mary Nyameke - Frank Emmanuel 
•	Jason Ukpong - Muhammad Ali 
•	Stephen Oluwasanmi - Irene Muthoni Mwaniki Muthoni 
•	Edu Njuguna - Muhammad Muhammad 
•	Gerhardt Datsomor - Ojugba Victory 
•	Lucille Lindeque - Selamawit Worku 
•	Rophi Chukwu - Brandon Mwanzia 
•	saad outchakoucht - Hamza Annane 
•	Hans Tognon - Ezemdi Benson 
•	Robby Milambo - Sibusiso Shinga 
•	Kgotso Matjato - Ejiofor Obieze 
•	Adekunle Olaitan - Joseph Wanjiru 
•	Christabel Juma - Kal Tollosa 
•	Tinsae Kebede - Beresa Abebe 
•	Prince Friday - Michael Ukpong 
•	Saviour Eking - Davis Tumuhaise 
•	Omojola Ilerioluwa - Oluwarotimi Adewumi 
•	Maryann Ezeogu - Ikechukwu Nwamah 
•	Gbenga Michael - Vongani Phakula 
•	Idriss Ibrahim Ibrahim - Jemila Ali 
•	Daniel Onyeachonam - Olanrewaju Lawal 
•	Bereket Alebachew - Solomon Okpako 
•	Jamiu Jamiu - Frankline Oyolo 
•	Yekeen Abdmuizz Abdmuizz - Debo Tijani 
•	Dagim Ourgie - Zeki Behailu 
•	Paschal Etuonovbe - amh Mohamed 
•	Enock Kipsang - Precious Idubor 
•	samuel mbogo - Wendimu Sitotaw 
•	Emmanuel Nnazor - Eddie OKON 
•	GHISLAIN ETOUNDI MVOGO - ezekiel dombissi 
•	Rashid Ali - Priscah Orori 
•	Linus Conrad Muhirwe - Edwin Agana 
•	Alene kahaliw - Ehikioya Oriaifo 
•	Castro David Castro - Oluwadara Oluwafemi 
•	Dagmawi Takele - zeresenay Yaregal 
•	Abdulrahman Yahaya - AMEER Usman 
•	Dampalou KANTCHO - Andre Pillay 
•	Amanda Arnandlall - Emeka CHIEMEKA 
•	Margret njumbi - Mary Mukami 
•	Prince Letsyo - Orison Ansre 
•	Mohamad Ebrahim - Clinton Adeoti 
•	Joy Omari - Shedrick Mboya 
•	Edem Ukoh - Mercy Nyong 
•	Daniel Okene - Samson Akinola 
•	Favour Olumese - Okorie Stanley Maduabuchi Okorie 
•	Natnael Wodajo - YommyBoy Madamori 
•	Michael Macharia 
•	Dagogo Orifama 
•	Victor Chinyereugo - Steve Obialor 
•	Stephen Kamanu - Favour Victor-Nuwomi 
•	WAKAM Hermann Vanel - Ornelle Penchia Mediesse 
•	James .O. - Gbenga Olaseni 
•	Ihuoma Ogbuji - Yirga Beyene 
•	Vivien Okubo - Kelechi Nnadozie 
•	Dawit Yibas - Elijah Murimi 
•	kelly Banda - Kingvictor Umeobiorah 
•	Aduragbemi Oduntan - ayobami Obadare 
•	Toheeb Oyeyemi - Kvngxthar Nwabuisiaku 
•	Abel kifle Woldesilassie - Bezahun Bekele 
•	Stephanie Aniche - Karugaba Blaire 
•	Jonathan Enyidede - Okezie Emmanuel 
•	Nadia Sanoussi - Charity Nkereuwem-Sunday 
•	ell MWANGI - Ruth Muthoni 
•	KIBET LANGAT - Sodiq Makinde 
•	Keyern Mwihandi - Peris Mwangi 
•	Charles Ogbobe - Oluwafemi Babalola 
•	Nelson Okoro - Vivian Okeke 
•	Favour Alozie - Jozef Ike 
•	Nectar Maina - Wisdom Onimisi 
•	Andrew Nwaogu - Abenezer Lemma 
•	Nzoputachi Emmanuel Samuel Samuel - Eliud Wanja 
•	Birhanu Miso 
•	Seid Muhammed Seid - Selehadin Selehadin 
•	David Okai - Abdulquadir Raheem 
•	Kenny Okeowo - Chima Durumetu 
•	Zerabruk Arega - Tougue Aristide Ate 
•	Bismark Abban - Kathy Egyepong 
•	dema Amano - Misrak Desalegn 
•	Onose Oko-Ose - Humphrey Okunwe 
•	Jesse Amenaghawon - Progress Lefsifi 
•	eBen Oyedokun - Ridwan Abdulkareem 
•	Philip Ukanwoke - David Okolie 
•	Harrison Omorogbe - Nenkkyoung WIKE 
•	nebiyou bekele - Epherem Ayele 
•	Neo Mathekga - Onome Okupa-Eboh 
•	Francis Chukwuoma - Taofeek Adisa 
•	Qozeem Ibrahim - Amina Omar 
•	Alfred Mwangi - Viola Ngige 
•	Magu Mwangi - Osi Enekhaze 
•	Ruth Victoire - KOUASSI STEPHANE 
•	Joe Ogaro - Victor Kaimoi 
•	Michael Onyeweke - AGBAGHER JAPHET 
•	Olanrewaju Oyekanmi - Oluwafunto Falua 
•	Pluto Ofejiro - Segun Iyanda 
•	Oviedo Shekina - Joy Omohwovo 
•	Sunusi Usman - Ken Otieno 
•	Godfred Frimpong - Esther Emmanuel 
•	Hilary Uwuseba-Godstime - Emmanuel Alabi 
•	Sherif Awofiranye - caleb Lewechi 
•	Adama Cherif - chanford Hermann chanford 
•	Ayanda Dladla - Ayub Odhiambo 
•	DENNIS Odibo - Omaka Kalu 
•	Alemi Asiki - Norbert Onyanga 
•	carson Carson - Faruq Taiwo 
•	Patricia Kithao - ESTHER Nduati 
•	Chris Omondi Omondi - Paul Kaiba 
•	DinoTech Amhande - Deborah Bamigboye 
•	Kiisi Felix - Nonso Iwedinobi 
•	Sandra Umunakwe - Unekwu Shaibu 
•	Solomon Aboagye - Abdulrazaq Ibrahim 
•	Gad Evans - Jesse Momanyi 
•	Kaifa Toure - Ajah Emmanuel Ajah 
•	Ngetich LEONARD - Chepsain Bett 
•	Vincent Nwafor - Joshua ABOTSIDIA 
•	IbukunOluwa Onabajo 
•	Tshepo Baloi - Tosin Kanmodi 
•	Torin Ajanaku - Jimoh Musyoka 
•	Theophilus Ayano - Abdulazeez Gaji 
•	Eloka Michel - Apexx Apelogun 
•	Tomide Adeyanju - Adam Bilal 
•	Asante Opoku-Asante - Jonas Mireku Amoquandoh 
•	Melak Mekibib - Gurumoh Gurumoh 
•	Kitts Makokha - kipngeno koech Brian 
•	Gerald Rotich - Frank Kuloba 
•	Tife Ogundele - Cindy Misoi 
•	Skyline Edhebru - Ufuoma Ovoke 
•	Mazi intel Ugwu - victor chidi 
•	Fortunate_June 2022🇿🇦 Ratau - Kalkidan Melese 
•	Oluwatosin Ajayi - Tosin Mojeed 
•	Aliyu sani - Alhassan Mumin 
•	Boluwatife Oladejo - Samuel Oluwatoyin 
•	Michael Omondi Otieno - Joseph Olabode 
•	Akomolafe victor Segun - Million Abebe Gete Gete 
•	Kwadwo Duah - Oreoluwani Omoyeni 
•	Ahmed Nesru - Shalyne Onyancha 
•	Oswald Ojo - Nech Anadi 
•	ANTEHUNEGN AYENE - Gifty Ikechukwu 
•	Eric Mutisse - Winny nyamohanga 
•	Barry Barry - Tsietsi Ramosedi 
•	Favour Osumah - Peter Augustine 
•	Boman George - Kobby Boateng 
•	Victor Tahiru - Emmanuel Akpaninyang 
•	HIRAM Njoroge Njoroge - Prosper Kazi 
•	John njogu - Dennis Gitonga 
•	Olawale Busayo - BALQEES LASISI 
•	Olaniyan Omotosho - Israel Oteniola 
•	Emmanuel Nwankwo - CHUBBY Uzoechi 
•	Reuben Kiringu - Martin Oyugi 
•	Linus Nwokedike - Gibril Sesay Sesay 
•	Dhikrullah Jagun - ibraahim Warsame 
•	Overcomer Salo - Mardiyyah Adepeju 
•	Negaye Muraga - Mikiyas Eshetu 
•	Olayinka Eyebiokin - Yitbarek Oushacho 
•	Utibe-ima Udokang - Joshua Oladeji 
•	sumeya Kedir - Hassan Mahamat Djidda 
•	Dennis Njogu - Ukasha Musa 
•	Natnael Zenebe - Samuel Mamo 
•	Ugochukwu Benedict - Stephen Gideon 
•	Steve Gitu - Dennis Fofie 
•	Cynthia Ofoche - Wilson Icheku 
•	Divine Peter - Millicent Magadi 
•	Cox Musyoki Musyoki - Djidula kevin Dadzie DADZIE 
•	Austine Nyiam - Mbongo Kemia 
•	ERIC Maingi - Austin OUMA 
•	Kiage Kiage - Peter Ateka 
•	Nathan Kebede - Mahmoud Abd Elkader 
•	Verem Israel - Gabriel Mwangi 
•	Olufemi Akola 
•	Odinakachukwu Anthony - Ann Legbosi 
•	Igwegbe Igwegbe - Bamidele Adeiza 
•	lizzie Ngotho - ELOHOR Eriobo 
•	Kwanele Ndhlovu - Chukwuma Emordi 
•	Wachira Mwangi - Donald Kiplagat 
•	RAPHAEL Ude - Israel Nwangwu 
•	Philips David - Kasim Jajere 
•	Mpho mahlangu - Youssef KERROUM 
•	Salim Sarumi - Josiah Elias 
•	Mohamed Abdiaziiz - Aliyare Warsame 
•	James Okeiyi - Emmanuel Olorunmolu 
•	ALVIN KUNG'U - Jimmy Kagochi 
•	Ogundimine Yetunde - ABUCHI DIDIGWU 
•	Esther Nwadigo - Victor Chukwudi 
•	joel kariuki - Clare Mosoba 
•	Brandon Makhubo - Ikechukwu Godwin 
•	Yod Tesfaye - Olusola Dairo 
•	Daniel Yadeta - Adeniyi Oluwajana 
•	Adebayo Jubreel - Oluwakorede Oladetohun 
•	Jhohn Afolami - Chidera Chukwuma 
•	Samuel Mariwa - Bongwe Obaga 
•	BALOGUN Balogun - Kevin Letlabika 
•	Hayat Elias - Martins Sule 
•	Ben Bundi - Asteraye Lemma 
•	Israel Jaja - Richard Asamoah 
•	Vitalis Osuchukwu - Edil Gebrewold 
•	Godwin Akpan - Agmuasie Belay 
•	Janet Kehinde - David ogunsanwodavid123@gmail.com 
•	Abdulkadir Usman - GERALD Gerald 
•	Victor Ruoya - oscar Nderitu 
•	Natinael Gebriye - Getachew Yazie 
•	Collins Ofeimu - Imani Akajameh 
•	Tevin Aduma - Nelson Orogwu 
•	Ngozi Ohagwa - Emmanuel Akpan 
•	Christian Egyir - Valentine Adjei 
•	Irene Osifo - Udale Ibrahim 
•	Philip Ng'ang'a - Aniekutmfon Ekere 
•	Sally Mulingwa - Mousa Sabit 
•	Haruna Danladi Maina DANLADI - Bislon Zulu 
•	Lawal Thuwaybah - Adedayo Aruwajoye 
•	Abenezer Anito - Betselot Uloro 
•	Obatoyo Alexander - Gorret Nabatanzi 
•	Tawanda Banditi - Lavine Shikanga 
•	Samuel Mwendwa - Maxwell Obuoro 
•	Immaculate Nyaga - Wasswa Julius 
•	Emmanuel Fasogba - Taiwo Adeyemi 
•	Joseph Oladoye - Oyeniyi Emmanuel 
•	Uchechukwu Iroadiogu - Adeyemo Adeyemo 
•	Amanze Glory - Nkechi Adihuba 
•	Ahlam Abdulkhalek - Kevin Mwongera 
•	Talent Aleck Gaviro Gaviro - Abdullah Munirudeen 
•	Lawal Lawal - Oluwajuwon Oladiti 
•	Mory momo - Assalet KOUA 
•	Austin Igboke - Uchechi Nmecha 
•	Masturoh Adegbola - Eddie Okon 
•	Jafaru Umar Faruk - emJoeTech Onwukwe 
•	Marie Damwanza - James Kariuki Kigathi 
•	Paul Alabi - Osuman Shehu Basiru 
•	Shehu Halimah Sadiya Halimah Sadiya - Abel Teame 
•	Ian Kitembe - Patricia Rukud'de 
•	Salome Nyambura Kamau Kamau - Adane alemu 
•	Brian Ibik - Chijioke Emele 
•	Daniel Oluwatosin - Ella Jessica Chinenye 
•	Imen Khemira - Toka ElWetedy 
•	Rebcca Asaye - Chane Eshetu 
•	Abdulshakoor Omeiza - Toyyib Ishaq 
•	Hikmah Olanipekun - Francis Oguaju 
•	Deb Omoniyi - Steve Obasi 
•	Leul sileshi - Amanuel Esayas Abdi 
•	Abdulazeez Ogunnubi - Nigus Amare 
•	Henry Otieno - Boniface Dakey 
•	Ridhwan Bakare - Emmanuel Osiyoku 
•	Osman Kamara - Christiano Enyia 
•	Olubunmi Ogunjemiyo - Michael Erukusin 
•	Samadou OURO-AGOROUKO - Victor Victorien 
•	Tolulope Omotoso - Munashe Matipano 
•	Akinbowale Akinyemi - Natnael Getnet 
•	mugambi Ndwiga - Emmyglobal Emmanuel 
•	Kamogelo Thulari - Cepha Mwangi 
•	Collins Ojougboh - Ikennah Stanley 
•	Netsanet Mekonnen - Selam Jada 
•	Patrick Peter - olawale Olayigbade 
•	Adegbenga Ogundeko - Malvin Sibanda 
•	Olasubomi Adetunji - Afolabi Adetunji 
•	Justin Protais BEKONO OTTOU - Shadrack Kiprono 
•	Mayamiko Msonkho - Kelechi Emejuo 
•	Kendi Nceene - Richard Ouko 
•	Abdulazeez Adegbite - Victor Ehimigbai 
•	Opeyemi Ogunsanya - Dennis Abraham 
•	Kara Alexander - Dixon Ibezim 
•	ORIRE Orire - Mohammed Mohammed 
•	Martins Awojide - Daniel Ifebueme 
•	Kaleb solomon - Nnamdi Ndunero 
•	Ifieniya Clement - Wondosen Seminew 
•	Abdulkareem Bello - Daerego Braide 
•	OLUSOLA AYODELE - Henok Yimer 
•	Saviour Gawugah - Renkre Dauda 
•	Adeoye Ajarat Abisola Ajarat - Tobi Oyekanmi 
•	Yasin Alhadi - Ejeje Akami Oden 
•	Bernard Owoo - Benard Gomashie 
•	MARIAM KAMAU - Khadijat Usman 
•	FITSUM Asrat - Utibe Udoh 
•	Prince Edeh - Divine Nnodim 
•	Ifeanyi Okolo - Sarah Enobabor 
•	Tevin Matema - Cuteface udoekong 
•	Pamah Onoriode - Oluwaferanmi Olatunji 
•	Wondmalem Desta - Raphael Kazembe 
•	Gephun Omondi - Estifanos Karato 
•	Geofrey Simiyu - Trefania Vhareta 
•	SAMUEL Abiola - Favour Nwobodo-Charles 
•	Carol Wanjiku - Seid Nurie 
•	Nsamije Ekpe - Abdullateef Tajudeen 
•	Antonia Wakaba - Thomas Njoroge 
•	John Billy - Oh G Ogidi 
•	Gold Ochim - MORRISON Ibim 
•	Wanja Nganga - Emmanuel Ayemere 
•	Georges MBOCK MBOCK - Princess Okonta 
•	Lerumo Nkofo - Blessing IKPONMWOSA 
•	Osborn Asamoah Kwasi - OBENG MICHEAL DUODU 
•	Muhammad Abdullahi - MARTIN Dotsey 
•	Lewis KETCHEMEN NKWEMI - AHMED Abd Alsattar 
•	Oluwafunsho ANIFOWOSHE - Whyte Bryte Aregbesola 
•	Koya Adekoya - Omotosho Omotosho 
•	Hale Endale - Godwin Johnson 
•	Tingo Ngara - Blessing Zuze 
•	Humble ONYENMA - Ebenezer Kiheo 
•	Beza Lindlöf - Daniel Kuria 
•	Rahab Mary - Michael Nduati 
•	Olamide Mujeeb Olagunju Olagunju - Biruk Tessema 
•	Andrew Obando - Anne Kiama 
•	lydia uzoma - Collins Oghenevirieze 
•	Rick Adebayo - Samuel Adeyemi 
•	Opeyemi Oriolowo - Guyfleury MANIRAKIZA 
•	Wilfred Wilfred - Ademola Adebowale 
•	Moshood Odutola 
•	Godwin Ezembi - Matsheole Majoro 
•	Abraham Okpala - Caleb Anietie 
•	Akinloye Rukayat Olorunwa Olorunwa - Dagim Zewdie 
•	Evans Karega - AbdulBasit Dawud 
•	Idah Jerop - George Agwet 
•	Mukuka Kondowe - Sarah Ossai 
•	Oluwakayode Oloyede - Kosisochukwu Okey-Nwankwo 
•	Ibrahim Olusegun - Ibrahim Alimi 
•	TMH Hailu - Kofi Oghenebrume 
•	Joy Ikebude - C Iloka 
•	Nana Kauffmann - Kidus Ataklti Brihane Brihane 
•	Christian Maximilian - Calvin Sharara 
•	George Rapemo - Abdul Mumin Fuseini 
•	Amsale Tsige - Yosef Alemu 
•	Hadiza Rabiu - Michael Adesina 
•	Chiamaka Anawanti - Slim Balogun 
•	David Bassey - Tolulope Babatunde 
•	Javan Muriungi - Kelly Muriungi 
•	Steve Kariuki - FIDEL Nguono 
•	Chinwe Chukwuogor - Emmanuel Ugoh 
•	Emmanuel Nwafor - Favour Ogidi 
•	Casey Mwangi - Fiona Wekulo 
•	muhammed Kanyi - Gabriella Peji 
•	Adewole SHOBANKE - Quadry Oladejo 
•	Buomkuoth Makuach - Haruna Mohammed 
•	Ilesanmi Aderibigbe - Adeyemi Salawu 
•	Sharon Wanjiku - James Oluwabukola 
•	Brian WAITHAKA - Gabriella Ngene 
•	Marvis Enubiaka - Ivan Ivan 
•	Victor Muiruri - Mohamed Mahamud 
•	Ashu Zeleke - Akhona Mtongana 
•	Tochi Onyenakorom - Joy Hanson 
•	Kingsley Ozor - Simba Mahlaulo 
•	Michael Okojie - Mukhtar Oladayo 
•	sylvester Sipitey - Habibah Jibril 
•	Emezi Uchechi David Emezi - Raphael Nnabuenyi 
•	Akinyemi Seyi Emmanuel Emmanuel - Emmanuel Emmanuel 
•	Bisrat Dressie - Ruth Moges 
•	Judy Chepkorir - Beryl Mark 
•	Vivian Ochieng - Antony Opano 
•	Captain obinna nwandu Nwandu - Ebenezer Ogheneverwhe 
•	Chika Mark - Divine Clem 
•	Mmabore Molaba - Edwin Odinga 
•	Ololade Adebanjo - Kwesi Danquah 
•	Samuel Muchoki - Natnael Kebede 
•	Fridah Odhiambo - JORRIS Nyange 
•	Oluwatobi Adelabu - Stefan Emmanuel 
•	Mensah Kodjo AVOMENOU - Abel PAKPALI 
•	John Okoye - Chidiebere Agbo 
•	Damian OLATUNJI - Chuka Oraekwuotu 
•	Imran Abdulmalik - Amity Ekoyi 
•	Gibson Afriyie - Olugbenga Odhiambo 
•	FELIX TOO - Lionel Gicheru 
•	Andrew Ezeani - Joshua Daramola 
•	WINNIE NAMIRIMU 
•	Boris Nkepguep - Emmanuel Ayodele 
•	Okechukwu Nwaorgu - Terry Onyango 
•	Emmanuel Adebiyi - Damilola Olofin 
•	Sophie Shalom Jeptoo - Queens Kisivuli 
•	Jessica Jones - Mekdem Kassye Yosph 
•	Waseem Ahmad Ebrahim - Estif Tassew 
•	Dennis nyawira - Alberto Oisebe 
•	Ibrahim Suleiman - Mignot Tadesse 
•	Akinremi Olajumoke Akinremi - Damilola Gbanja 
•	Elizabeth Anne Awino Onyango - Ayienda Brian 
•	Elvis Marfo - Mercy Ogochukwu Ahuekwe 
•	Daniel Okraku - Kwame Essel Mensah 
•	KINGSTONE ODHIAMBO - Emmanuel Kiprono 
•	Bernard Muinde - Michael Eshetu 
•	Yelo Malaye - Izuchukwu Onuegbu 
•	Nick Logos - Shannon Simiyu 
•	Faruq Oreoluwa - JOSHUA TAIWO 
•	Yared Nigatu - Eyob Assayie 
•	Lidya Amare Asfaw - Ismael Mohammed 
•	Wuonam ODERA - Sammy Kariuki 
•	Charlespaul wabomba - Gloria Kaluma 
•	Isaac Ajani - Abraham Tesfalem Belete Tesfalem 
•	Rasheedat Olufunke Yusuf - Cheick Ahmed Touré 
•	Abubakar Audu - Patience Achebo 
•	Zehara Yassin Aman Yassin - mubark Badawi 
•	Moses Thliza - Mfoniso Robert 
•	Truth Osiriame - Baithicia Baithicia 
•	Kennedy Mkapa Mkapa - Sylvia Karani 
•	Ademiju Taiwo - Increase Uwadiale 
•	Daniel Mwaura - Abasifreke Peters 
•	Hydaline-code Hydaline Charlene - Victor Odebunmi 
•	Olanrewaju Awoyele - Mintesnot Yohannies 
•	Nesisa Moyo - Tawanda Rundu 
•	Bemnet admassu Admassu - Kalid Shikur 
•	Tochukwu Maduka - Chibuzor Ehiemere 
•	Joseph Utuedeye - Peace Issa 
•	Cosmus Cosmus - Theophilus Ebenyi 
•	Samuel Amiaka - Uzziah Osia 
•	Zekarias Hurisa - Bereket Haileslassie 
•	Tejiri Origbo - Isaiah Ikharona Ikharona 
•	Beulah Igboanugo 
•	David Adejumo - Gabriel Omeke 
•	Tope Koya - Emmanuel Enahoro 
•	Afia Eneji - Sisay Assefa 
•	Hadiza Sani - MUHAMMED JAMI'U AGARAWU 
•	Shiphrah Mergold - SUNDAY George 
•	Einstein cheruiyot - Greg Foulkes 
•	Val Omondi - Micah Othino 
•	Cynthia Maina - Joy Chebet 
•	chioma Nwankwo - Joseph Akowuah 
•	Nathan Omeri - Tracy Muya 
•	Wisdom Koudama 
•	Zulfat Muhammad - Gracian Maseko 
•	Brenda Wanyonyi - Kevin Oluoch 
•	Carl Osore - Oladimeji Akinlolu 
•	Timothy Taremwa - Rose Mwangi 
•	Yida YIDA - Daniel Iroanya 
•	Yimage Ahmed - Ealwaafy Wafy 
•	Yohannes Mekonen - Tomas Yimenu 
•	Iqmat Olaniyan - Abiola Ajibowu 
•	Joseph Alikah - Maximillian Amanoipo 
•	Abel yohannes - Danayt Deboch 
•	Negassi Tesfay - Comfort Oluwapelumi 
•	Chris Muroka - Kilonzo Mutui 
•	Kesse Ahante - Adesina Dhikrullah 
•	Natnael Tadesse - Dawit Gebremedhin 
•	Chidozie David - Francis Asemota 
•	Keabetswe MONTSHO - Julius Ochai 
•	Henry msechu - Michelle Chatikobo 
•	Ibrahim Odhiambo - Alvin Otanga 
•	Juliet Chiagozie - Genesis Mangibo 
•	Debisa Abebe - Zerihun Abune 
•	Mercy AUPAT - LWIIGO JOEL 
•	Hope Iyamu - Tochukwu Onyeze 
•	Mark varu - Jared Obare 
•	Tehmi Ashaolu - Abel Misiocha 
•	Wycliffe Kerich - IAN Kerich 
•	Marvelous Egbe - Oluwaseun Afolabi 
•	Christine Waituika - Abdulrahman Abedi 
•	Bright Folorunsho - yilkal Adal 
•	Mohammed hanin - Moyosore Ajayi 
•	Paul WILLIE - Joshua Onwuemene 
•	OLAANY Adesanya - Victor Iwegbulem 
•	Abiola Olaleye - Chinedum Oliver-Ugwi 
•	Jamal Njeru Kitheka Njeru - Ambrose Opio 
•	Lydia Nyamanyi - Samuel Tucker 
•	Joshua Oluwafemi - Renish Okago 
•	Ubong Umoette - ABRAHAM Benson 
•	Charles Karanja - ASILA IGESA 
•	Shingirai Shoko - Victor Egbulefu 
•	Fred Ankomah - jonas Mwansa 
•	Meseret Gonche - Caleb Marani 
•	Bunmi whesu - Damilola Adesina 
•	Augustine Otieno - Eyoel Hailemichael 
•	Akpevweoghene Unuakpa - Richard Rang'ondi 
•	Ajibade Adekola - Abdulwasii Rufai 
•	Busayo Ologunleko - Joyful Daphnes 
•	Doye Solomon - Edwin Enjo 
•	Abel Hassen - Rose Alivitsa 
•	Samantha KISSIME BAMBI - Moe Sed 
•	Iwegbu Jeddy - Puseletso Mohlaodi 
•	Jeffrey Uwenor - Life Davidking 
•	Ebimoboere Claudius - spencer Onyango 
•	Marcus Imagwe - Abdullahi Abdullahi 
•	Lee Nduati - Harry Mwaura 
•	Tawfik NADA-ABI - FELIX OMORE 
•	Olasunkanmi Popoola - Ifeanyi Azogu 
•	teddy Alemayehu - Tesfamichael Gebre 
•	Lolade Akinloye - Adebusola Ayo-Olaoye 
•	Segun Fashina - Stanley Osagie 
•	Chiamaka Onyia - Henry Sylvester 
•	Carlymax Kuria - Marybliss Famous 
•	Adaeze Atuanya - Nnennia Atuanya 
•	Mawunyo Yao Mawunyo - Brian Mangitsa 
•	Paul Adegbiran-Ayinoluwa - George Nduka 
•	Faith Jacob - James Larbie 
•	Abduljawwad Salihu - OLUWASOJI Lebi 
•	Yosef Sahle - Ralph Osekre 
•	Hellen Wanja Waithaka - Charles Wanjiku 
•	Stephen Gusanu - Johnson Adenowo 
•	Nebiyou Metaferia - Elias Dewa Ahmed 
•	Aniekan Titus - Anuoluwapo Adegun 
•	Degefom Berhe - Berhanu Haylie 
•	Michael Getachew Dadi - Onyekachi Igbo-Obiakor 
•	Ugbede-Ojo Sani - Damilare Komolafe 
•	Marvin Mbithi - Nkatha Nkatha 
•	MUSANA YUSUF - Victor Okeke Okeke 
•	Sudi Murindanyi - Lourdes Alexandra 
•	Bongi Mona - Mpilo Mafu 
•	Bethelhem Ashenafi - Mikyas Bekele 
•	James Katiwa - Mike Monaru 
•	Bode Olaleye - Evance Ojukwu 
•	Lawrence Mugwena Mugwena - Stephen Azosike 
•	Joy Oluwafemi - Peter Turay 
•	Dharren Makoha - Moswazi Malatji 
•	Birhane Gulilat - Kaleab Gulilat 
•	Hamzah Ibrahim - Nafiu Abdulsalam 
•	Ibukunoluwa Akintola - Ngarari Wanjohi 
•	Oluwatimilehin Fasanmi - Alhussain Ibrahim 
•	Azarel Besser - Kosi Chibueze 
•	Chineze Ogugua - Nonso Godson Onyedumekwu 
•	Theo Paintsil - Ejomafuvwe Ofonodo 
•	Awulehan Ekpokeme - andu Alemayehu 
•	David Kinuthia - sam Kariuki 
•	ABIKE OGUNMOLA - Philemon Philemon 
•	Abdimalik Muhumed - mahamed hassen Tahir 
•	Collins Nyakundi - Benazir Ali 
•	Jide Igbalaye - Edwin Umana 
•	anita Kiranto - Alfred Agbenyenu 
•	Mark Oori - BiatoYahweh Emerenini 
•	Derick Kinoti - Mary Monari 
•	Audrey Ogambo Ogambo - Njiraini Njiraini 
•	daniel muema - Monicah Wanjiru Murira Wanjiru 
•	Rhoda Adigun - Ibraheem Abdulwakeel 
•	Oluwatobi Saubana - Ted Gera 
•	Abdulhakim Ibrahim - Bantewalu Dukamo 
•	Mercy Oriaku - tigist Bekele 
•	Memory Zulu - Mohamed Suliman 
•	Lielit Teklay - Alvin O Mike 
•	DANIEL SUCCESSFUL Successful - ahmed abdirahman yosef 
•	James Arong'o - BRIAN Mugendi 
•	Allen Sibanda - Mnqobi Dlamini 
•	Opeyemi Moriyonu - Toritsemugbone Asifor 
•	Martin Yeboah - Matex Moseti 
•	Harun Owino - Amir Alamin 
•	Smart Mba - Joseph Ariyo 
•	Abenezer Tekle - Abdulsobur Sadiq 
•	Chiagozie Ikeji - Oluwaseyi Adekoya 
•	Yoel Fshatsion - Bright Ogo 
•	Esther Marubu - Andrew Kamau 
•	David Luvai - Laura Bolade 
•	Olukoya Mdlolose - Ishmael Mafole 
•	NEBYU MEKONNEN - Yidu Goitom 
•	Alvyn Otieno - Rediet Firew 
•	Eyasu Mekonnen - Kyle robins 
•	Victoria Ezenwobi - Nicholas Dragudi 
•	Obinna Nkemjika - neba Gashaw 
•	Samirah Usman - Desnet Girum 
•	Boulou10 Arnaud - Solomon Feyi 
•	Bright Gawu - Bikila Debelo 
•	Sunday Adigun - Juicio Ochiche 
•	Emily Kamiti - Kennedy Kiogora 
•	Chika Ndubuisi - Chiamaka Adaobi 
•	NGANTCHOU FARIX-KILIEN - Peter Wambulwa 
•	EMMANUEL OYELAMI - Manal Ghamir 
•	Farouk Akinsanya - Mathew Ogunmefun 
•	Michael Onuekwusi - Romaric MAZNA 
•	Zelalem fiseha gelaye Gelaye - Isaac Kiarie 
•	Kosisochukwu Ozue - Salah seid 
•	Matumbai Binale - Charles Njagi 
•	Blessing Udiong - Uchenna Obi 
•	Slindokuhle Duma - JAPSON Ajayi 
•	Jashon Osala - Verah MOKAYA 
•	Clinton Mokaya - Omojuwa Emmanuel Oluwagbenga 
•	Mercy Ade-Ige - Samuel Adeyemi 
•	Manuel Emmanuel - DONALD KARGBO 
•	Lesley OGBEY - Tariku Wendimagegn 
•	ian Gitau - Mickay Aderibigbe 
•	Yawa GERALDO - Rodolf Rodolf Séderis 
•	Bulelani Botman - Impact World Aigbiremhon 
•	Gideon Igbon - Siyabonga Shabalala 
•	Tryphena Abimiku - TEYIRA GEO-NEEDAM 
•	Naomi Kimata - Norbert Offor 
•	Philomena Kawira - Desmond Koikai 
•	Lukhee Balogun - Obehi Okoduwa 
•	Ochieng' Odongo - Mersha Mamo 
•	Abel Mekonen neguse neguse - Obiajulu Ezike 
•	Okechukwu Emordi - Listowel Adolwin 
•	Joshua Daramola - Obed Asamoah 
•	Samuel Oyebamiji - Habib Hamza 
•	DAVID Mbacha - Jacky Hlongo 
•	Jackson Ekai - Yibe Woldekidan 
•	Peculiar Iguodeyala - Nnamdi Akpa 
•	Geoffrey Musweu - Tomisin Ajide 
•	Tapiwa Chiremba - Opeoluwa Afolayan 
•	Justice Merrick - Iruoma Onyia 
•	John Aina Aina - Abdulrahman Oyetade 
•	Olawale Onabanjo - Hendrick Malatji 
•	Ugochukwu Nwaorgu - Ngetich Kiprotich 
•	Martin Ogunjemilsi - Mihlali Faku 
•	Emmanuel Kolawole - Abdulbasit Adeoye 
•	soumahoro Soumahoro - REMI GNAMIEN 
•	Najah El-yakubu - Adebisi Olayinka Ayoola 
•	Hassan KYANZI - Hillary Ezema 
•	Mutanu Musalu - DERRICK OMONDI ODHIAMBO Omondi 
•	Lily Mihanjo - Lukindo Kikunt'e 
•	Mayowa Dada - Esther Adeyemi 
•	Vick Chidi - Alehegn Tesfaye 
•	Aminat AJOGE - Adebayo Kanmi 
•	Michael Kitili - Debbie Indah 
•	ohanyere uchechukwu - sosa Okoromi 
•	Opeyemi Adedigba - Chinedu Ihedioha 
•	Ajibola Osunkoya - Ishaya Solomon 
•	Alex Indimuli Absolom Indimuli - Ahmed MOHAMMED 
•	Tito Osadebe - Precious Uzoma 
•	Mubarak Opadayo - Theresa Bazudde 
•	Abiodun Ogunremi - Taiwo Taiwo 
•	Kelvin Efui Djokotoe - Juliana Aggrey 
•	Moses Bett - Fatima Sani 
•	Jared Keago - Endris Yassin 
•	Precious Okebugwu - Denis Kathuri 
•	Zee Odebamike - Georginia Nwaneri 
•	David ADU-POKU - Evan Chaun 
•	Chizoba ODINAKA - Akinlabi Folashade 
•	Kevin Mwaura - Horace Okoth 
•	Godwin Owusu - Eric Turkson 
•	Ifunaya Odiase - Abednego Emonena 
•	Olatunji David - HARUNA Abdulmajid 
•	Kevin Wettaka - Okediji Ayanfe 
•	AHMED ABUBAKAR - Diamond Daniel 
•	Tshepiso Gitonga - Shadrack. Otieno 
•	Edoh Kindness Ibrahim - Mustapha Aliyu 
•	Nelson Alexander - Omotola Deji Omotola 
•	Christian Dirisu - MARTINS Martins 
•	Favour Ayeni - David Adama ADAMA 
•	marytriza oira - Wilson Muriuki 
•	Abdallah Ismael - DAVID Onifade 
•	Chisom Epunam - Bilal Abdelkadir 
•	Saruni Saruni - Kenny Mwangi 
•	Psych Ahmed - Nathan Makhombe 
•	Alex Njiru - Mikasa Asukwo 
•	Erica Boahemaa - PEREZ YEBOAH 
•	Precious Oranye - Islamiat Okedele 
•	Zuwaira Sadiq - Abdulhakeem Muhammed 
•	Eric Kabira - Pauline Nanjala 
•	Joel Inyang - Kennedy Okeke 
•	Gloria Cherotich - Mutai Mutai 
•	Shawn Kiplagat - David Kinyua Gathu Gathu 
•	Wangechi Agnes Gichuhi - Davy Mutua 
•	Momohemi Williams - McDonald Njoku 
•	Kabir Atoyebi - WonderWoman Idika 
•	Abdurhaman Adem - Asiwaju Joshua 
•	Cally Nweke - Olamide Solomon 
•	Giphty Mensah - Michael Nwanolue 
•	Mussie Abebe - Lawrence NAHORY 
•	Jude saleh - Favour Kolapo 
•	Emmanuel Ufiah - Francis Musyoka 
•	Freda Appiagyei - Salman Hassan 
•	Oswin Justine Ayonoadu Justine Ayonoadu - Deborah David 
•	Vuyani Ndayi - Charles Arsène Oma Betow 
•	Samson Amtataw Geberhana Gebrehana - yodit Ayalew 
•	Mahbub Asifatu - Raphael Simba 
•	Oluwatobiloba Ayodele - Glory Ola 
•	Susan Wangari - Brivia Odunga 
•	ETINOSA Igbinevbo - David Morah 
•	TERENCE Onyeweke - Tatiane ASSATSE 
•	Wakuma Tekalign - Nat Mekonnen 
•	Tracy Okorie - Kenneth Onogwu 
•	Sharon Adimula - Emaido Essien 
•	Pauline John - Vince kimani 
•	Adediran Divineflourish Adetomiwa Adetomiwa - LAUREN MOGUCHE 
•	Rahwa Berhe - Adewale Azeez 
•	Blessing Gominah - Moureen Gituma 
•	Mphoma Matseke - John Uko 
•	Chris Munga - Nesbit OTIENO 
•	Keziah Ongangi - Pauline Onyango 
•	Ibrahim Waheed - Yusuf Mohammed 
•	Kevin WASONGA - Emmanuel Olorunfemi 
•	Scholastica Muigai - Chibuikem Ifezue 
•	ELIE MBAV KABANGU - Edwin mwangi 
•	Racheal mwikali Kasia - Martin Maina 
•	Derejarra Jara - Isaac Eguaoje 
•	Lewis Njuguna Mwangi Mwangi - Donald Brooks 
•	COSMAS Nweke - bwanatemba Temba 
•	Solomon Zinabu - Wubsera Melaku 
•	Teresa Mutua - Frankline Ongeri 
•	Rodgers Otom - Rukky Atife 
•	Precious Akintobi - Acelaxxy Anibire 
•	Victor MUTHURI - Florence MBOGO 
•	HALLEY Nicholas - Ralph Njuguna 
•	Michael Saviour - Enenche Jeremiah Adoga 
•	Johnstone Njuguna - Omondi Jeff 
•	Annette Katua - Clement Kimuhu 
•	Oluwatosin Wahab - Augustina Eza 
•	Miracle Ndubuisi - FRANKLIN Anyika 
•	Titus Ojediran - McDonald Amure 
•	Milkiyas Siyum - Naod Ararsa 
•	Olawale taoheed - Nick Chirchir 
•	KAWISO KENETH GODFREY - Adeniyi Adejumo 
•	Abiodun Shittu - Erica Onyegwu 
•	Kingsley Botchway - ishaq musah 
•	Faith Mmeka - FEROUZE OCHIENG 
•	Harrison Kariuki - VINCENT Odima 
•	Abdullah ADEOYE - James Olamoyegun 
•	Ednah Chukwuka - Suleiman Suleiman 
•	Samuel Igbinovia - Naomi Osunde 
•	Dagmawi Kassaye - kelvin Ahante 
•	Salem Ladhari - Game Balcha 
•	Habibat Adetoro - Oluyimide Onaolapo 
•	Olusheyi Akinbobola - Bunmi Ogunnowo 
•	Luke Welman - Ian Olwero Olwero 
•	Oruche Ugochukwu - Olajumoke Ogunleke 
•	mustapha mustapha - Amine draoui Draoui 
•	Madelé Theron - Mahmud Abdulazeez 
•	Mehary ALEMU - Abreham Eshetu 
•	Anet Ndwiga - Emperor Fowotade 
•	SUMAYA NANSUBUGA - Ssozi Malik 
•	Olamide Adebisi - Precious Ogundana-Akinola 
•	Biruke Lemma - Linda Matunga 
•	Akinbusuyi Jegede - Nicky Gouws 
•	Vincent Onyango - Lucy Ann WAHITO 
•	Israel Ilori - Samuel Olatunji 
•	PETER OLWANDE - Oluwapelumi Igbinlade 
•	Gilbert Maina - NICHOLAS Kool 
•	Najjibcode Mutyaba - Mubarak Wantimba 
•	Osborn Essien - Olajumoke Kolawole 
•	Desnos Yechi - Henry Igwe 
•	Odhiambo Felix - Opeyemi Abdurrahman 
•	Ridwan Azeez - Adeyemo Oluwadamilare 
•	Josse Wasonga - Dennis Mkalama 
•	Kolade Olanipekun - Somto Eze 
•	KINGSLEY Ohene - Jane Okeke 
•	Syomiti Mutui - Joseph musembi mukula musembi 
•	Oyindamola Banjoko - Ahmed Ibrahim 
•	Damilola Richard - Ezekiel Okeagu 
•	Adrien Bouzeko zangue - Grin Issa 
•	Bridget Idam - Josie Olagunju 
•	Darrel Omondi - Salathiel Wekesa 
•	Emeka Chukwudozie - Henry Ozomgbachi 
•	Sid Ogunbanjo - Wizetoons Toritseju 
•	Temitope Shittu - Alex Owoade 
•	Adebobola Bamise - Chara Ude 
•	Jonah Jockthan - Marv' Ikejiama 
•	Tewedaj Olkeba - Andima Geoffrey 
•	Tiberius Nyaega - Caleb Arodu 
•	Gbolahan Balogun - Ibrahim Busari 
•	Isheanesu Constantine Kahonde - Andrew Hove 
•	Emmanuel Weh - Yoseph Seyoum 
•	Akanjipen Abdullahi - Oluwadare Adeneye 
•	Emmanuel Kolade - Oluwadunsin Olonitola 
•	Tamara-kuro Alale - Pelumi Adesokan 
•	Bruk lemma Bruk - Amdom Hailu 
•	Abdulmalik Aberejo - Ololade Popoola 
•	Oladotun Osasuyi - Jeremiah Obuseri 
•	Alyakbar Sheikh - Maureen Kodoosi 
•	Ibrahim Yusuf - Milli Haile 
•	Daisy Wangenga - Brian Otieno 
•	innocent Nwakaku - Chukwudi Okpala 
•	Ugochukwu Okaro - Benjamin Izuagbachukwu 
•	Leule Haylay - Mihret Ghebregzabher 
•	Melvine Juma - Mikiyas Alemu 
•	Abdirezak Mundino Datago - Venk Ogunniran 
•	Kehinde Bandipo - Francis Nwoke 
•	Ayomide Ayodele-Soyebo - Kingsley Odim 
•	Charles chikelu - Marv Adesanya 
•	Emmanuel Atikese - Mohamed Fadel Sow 
•	NELSON Idehai - Chinonso Obaji 
•	Gift Victor - Hillary Owowo 
•	Williams Tchapga - Bryan Obiorah 
•	Eyob Tasew - Fasika Melese 
•	Godwin Musa - Oluwatomisin Isogun 
•	Oluwarotimi Bankole - Thomas Tesfay 
•	Anwar Endris - Rahmah Alhassan Larry 
•	Amili Mugigayi - Boipelo Selebano 
•	Andrew Ayala - Isaac Okarevu 
•	Toluwalase Omokayode - Taiwo Francis 
•	Mugabi Joseph - Chebet Daniel 
•	Samuel Lateef - Dennis Botwe 
•	TAPHLINE MATUNGA - Vincent Saiwa 
•	Robina Miles - Uko Udo Udo 
•	Elyon Omidiora - Mohammed Tegegne 
•	Jamal eldin Mokhtar - khaled yassin 
•	yonas Defar - Fitun Woldemeskel 
•	Owuraku Manu-Marfo - otobong Edoho 
•	Maurice Haro - Wisdom Dzontoh 
•	Mustafa Abdi Abdi - ABDIAZIZ SHEIKHALI 
•	Umoh Andem - Emma Okon 
•	Hillary Kitel - Fredrick Ndung'u 
•	Joshua Alana - Maxbobo Ebobo 
•	Keriane Nzabampema - Dradriga Patrick Patrick 
•	Olamide Ogunmakin - Muhammad Sherif 
•	Emmanuel Nnam - Ibrahim Ilyasu 
•	Nicks GITOBU - Musa Parsanka 
•	Oyekunle Samuel - John Oyekunle 
•	Victor Oraekwuotu - Adewale Aderoju 
•	Bantamlak Tilahun - Macmatthew Ahaotu 
•	Nkululeko Maqoboza - IHEANYICHUKWU Kalu 
•	Safiya Shariif Shariif - Mohamed Abdullahi Hassan Hassan 
•	Christian Chi - Melba Gitau 
•	Saudat Karaye - Eden DAMESSA 
•	Everlyne Ahono - Surafel Melese 
•	Thami Gumede - Godlives Patrick 
•	Eyuel Deribe - Omobolaji Olusanya 
•	Cheick KONE - KOULA Amanie Ange Carelle KOULA 
•	Aaron Obeng-Kyei - Eric Arthur 
•	Peter Akerele - Afolabi Adepena 
•	Gizachew Tessema - Suleiman Suleiman 
•	TSHEGOFATSO MOKAA - Ammar Abd Alsattar 
•	Toyin Fashemore - Ogunsote Ayotunde 
•	olubukola Adeyemi - Antenehalx SISAY 
•	Maryam Musa - Amina Musa 
•	Vince Kiprop - Chukwunonso Obiakor 
•	Olumide Ayeromara - Joshua Ogungbenro 
•	Kirub getachew - Victor Adebiyi 
•	Kunle Oni - DANIEL Anyigbanya Nelson 
•	Chidubem Okafor - Ajayi Timileyin 
•	Chinecherem Nduka - Peter Macharia 
•	Abisola Popoola - Abayomi Adebayo 
•	Morayo Agunbiade - Enoch Olatunbosun 
•	Peter Oluwagbemiga - Rev-LET Ligom 
•	Minister Yerima - Eric Bolade 
•	Dej Mengesha - Tumi Porotloane 
•	Arnold Ocen - Sean Muzungu 
•	Habeeb Hassan Dindi - Victor Nyaberi 
•	Tochukwu Ugochukwu - Tobi Adeleye 
•	Lenny Teghe - Badamosi Oluwatobi 
•	moses Aiyidu - Emmanuel Great 
•	Mathius Kassagga - SAMUEL BEZABIH SANBI Bezabih 
•	Rocco Junior Venter - Raheem Amer 
•	Getahun Zeberga Birda - Joseph Matimba 
•	Vivian Ezigbo - Bonolo Atong 
•	Graig Selewan Selewan - Godday OJIJEVWE 
•	Brian Kirimi - Kevin Kioko 
•	Oluwaseun Lawal - Emmanuel Omokhegbe 
•	DERIC Masiga - Jason Kesa 
•	Righteous Ifada - Tosin Tosin 
•	Bobo Tonweriyai - Precious Diala 
•	Kenechukwu Nnaka - Eugene Appiagyei 
•	Maswi Chacha Chogo - Francisco Kubagwa 
•	Joseph Kamau - Wahome Maina 
•	Jude Obuo Unah - Daggy Yohannes 
•	Theophilus Nkwuda - Sylvanus Nkama 
•	Biniyam Asfaw - Alexander Sibhatu 
•	Rita Onwudiwe - Rahel Abera 
•	Emeka Stanley - Oluwaseyi Egunjobi 
•	Efosa Aideyan - Minasseh Alaro 
•	SOSPETER KARIUKI ndegwa - Brenda Oduor 
•	MOSES CHIOKO - Monday Oko 
•	Ibiye Charles Charles - Patra Nomaka 
•	Yinka Adigun - Aya gamal 
•	Oyewole Tosin Ayodele - Itayi Tafirenyika 
•	Basil Bassey - Headply Ogedengbe Ogedengbe 
•	Paul Muguro - Brian Mutea 
•	Hayder Mohammed - Ibukun Ibukun 
•	Joseph Mwangi - Eugene Odhiambo 
•	Po Gbadebo - Nana Kofi Mantey 
•	Anteneh Tadesse - Noble Mutoko 
•	Isaiah Omoboriowo - George KYAMBADDE 
•	Joseph Oyelami - Chang Gatdet 
•	Nicholas Ikiroma - Martin Agoha 
•	Iyiola Jimoh - Nifemi Abiodun 
•	Guzorochi Confidence Confidence - Gideon Obiasor 
•	Fawaz Babaodutayo - Brenda Ekemezie 
•	mary Zelalem - Michael Akinpelumi 
•	APHIWE Ngowapi - Brenda Wogbe 
•	ROLVA Mashale - Edreen Mukwaya 
•	Oge Ndubuisi - Gerald Mwangi 
•	Tonie Antoinette Ohene - ABDULRAHMAN DAUD MIRAJ MIRAJ 
•	KEPNANG PEBEU Maxime Fabrice - Christian DJOMAGA 
•	Ephrem Habteselassie - Hibi Bekele 
•	Eseosa Erhabor - Akorede Emiola 
•	devMoki Daniel - Ebenezery IPEREPOLU 
•	Dominic Sengo - Ayodele Adeniyi 
•	X Chauke - Manthole Maila 
•	Telma Farida - gideon Wangui 
•	Olesso Kisia - Ashley Owaya 
•	Otwoma Otwoma - Caleb Caleb 
•	Chika Chijioke - Reubenspain36 Sunday 
•	Damilola Olugbemiga - Tife Ekundayo 
•	Rose Njeri Njuguna - John Gitahi 
•	Airat Omolola - Chetachi Maduabuchi 
•	Charles Misheal - Anuli-Amara Opara 
•	Ifeoluwa Mistura Salami - Bash Akanbi 
•	Paminus Orenge - seyram DOLA 
•	Dagi Seme - Sami Yisehak 
•	PeterBrian Ruthuthi - Beauter Maraji 
•	Vashty Kuria - Silvester Kilungya 
•	Meklit Tsegu - Christopher Idunoba 
•	Ian Okoth - Jane Ikwuegbu 
•	Henschel Zulu - Ajayi Blessing Tope 
•	Reuben Enahoro - Amina Umar 
•	Linda Willis - Mathias Kwikiriza 
•	Ghartey Ghartey - Ziga Victor 
•	Meklit Engda - Lee Mwaniki 
•	Chinye Azike - Barasa Misiko 
•	Henry Deya - George Nyamema 
•	Richard Chukwuma - Benson Kigoci 
•	Divine Asim - Tsega Teklemariam 
•	Anteneh Yirga - Abraham Shimelis 
•	Edem Aheto - Michael Dela Sape 
•	Tuoyo Chukwuemeka - Jossy Chidi 
•	Nnaemeka Okoli - Annette kimwere 
•	Joseph Ingio - Bereket Wodajo 
•	Samuel Nunsin Doe - Mawuli azameti 
•	Wandile Mawelela - Matlotlo Mokomane 
•	Bravo joseph Mutale - Joshua Akhidenor 
•	Derrick Murimi - David Olanrewaju 
•	Oliver Bada - BERNICE Muturi 
•	Aderibigbe Ayomide Oluwabusayo Oluwabusayo - Emmanuel Fenyi 
•	Benedicta Ohene-Amadi - JUSKING ADJEI NYARKO 
•	Aghogho Bogare - MULUKEN Kebede 
•	Jovis Duru - Dandison Opara 
•	Kue KEN-AMINIKPO - HARISSOU Koini 
•	Sarah Kugblenu - Asnath Kimathi 
•	Afolabi oluwaferanmi - Rachel Ndungu 
•	RICHARD MWAHUNGA - Benoni Esckinder 
•	Chinedu OKAFOR - Oyeinkurokakemo Azebi 
•	Daniel Mwenda mwenda - Biruck Getu 
•	Fitsum Kifle - Gerry Aballa 
•	Yaa Darko - Chidi Sunday 
•	Ben Orumah - Richard Mba 
•	Ashenafi Debella - Wasiu Ogunkoya 
•	Irene Mungai - Jackson Mobe maina 
•	Precious ENOCH - Leon Nyakundi 
•	Michael Atere - Unyime Abai 
•	Francis Adegbe - Oluwatoyin Christiana 
•	Perfection Adewusi - Chika Ugwuanyi 
•	May Ben - Lucky Ogheneruona Hope 
•	Nuwabiine Bonaventure - Asteraye Tsigehymanot Molla Molla 
•	Queen Queen - Christabel Gwani 
•	Oluwaseyi Idowu - LIGHT ENYINNAH 
•	kouame abraham - Ingrid Koumayeb Pamegny 
•	Keith Chad Chad - Ian Alindi 
•	Sulayman Nezir - Huguette Ebu 
•	Carey Fynface - Lawrence mugwe 
•	Waris Kazeem - Aliu Lawal 
•	Mulukal Dema - Ntina Ntina 
•	Oluwaseun Aladejana - Johnson Omotunde 
•	Aminu Rabiu - Lateef Odufeso 
•	Agape Okonta - Faith Amuda 
•	Mogau Ngwatle - Chima Ihueze 
•	OLUWAGBENGA Adeleye - Thozama Ngwenya 
•	Amimo Jackie - Forester Kisiara 
•	Goshu Kenea - Tobi Fasasi 
•	Dapo Oladapo - Awoyemi Victor A. Awoyemi 
•	Prisca Maduka - Adokiye Richard Ayisimaka 
•	Scotney Shitakha - Rowland Agbahime 
•	Kabiru Umar - Temidayo Adeyemi 
•	Ruthy Agatha Namaganda - Isaac Katusabe 
•	David Adokuru - Abdulhameed Yunusa 
•	Sola Lawal - Amanuel Habtamu 
•	Imran Suleiman - El faruq Adam 
•	Emmanuel Amubieya - Aishino Biliyoung 
•	Omowunmi Iyaomolere - Captainc Oluwadamilare 
•	Thomas Kankam - Abdul-Mumin Awinaba 
•	Wondmagegn Abriham Chosha Chosha - binyame Gebreegziabher 
•	Muyiwa Fatunsin - Samson Oluwasegun 
•	Sheila Otuko - Runo Mercy Runo 
•	Abdulquadir Hassan - David Onyango John 
•	crown Ahonye - Nicole Kaswa 
•	Saheed Salawu - Lary Yusuf 
•	Dwalker Akpan - Sam Gombah Ouma 
•	Hazem Ben Abdallah - Ivan Epou 
•	Abidemi Oluwaseyi - Favour Baruch 
•	Samuel Eshiet - John Isah 
•	Alvin Mutuku - Charity Muteti 
•	zaccheaus gachamba Mathenge - Megfirah Mohammad 
•	Ben-Gurion Zanus - Temitope Popoola 
•	Agatha Mathuva - nduva Nduva 
•	Joy MUGAMBI Mugambi - Kyle Terik 
•	Kadubabari Piaro - Naol Bulti 
•	IAN OKEYO - Olamide Ogunrinola 
•	Maxwell Omondi Ondiek - Ruth Akuoko 
•	VINCENT Tommi - Felix Miriti 
•	Adedolapo-marian Akinwunmi - JOSH Aladeboyeje 
•	Chukwunonso Anawana - Ferdinand raphael 
•	Essie Ngugi - Divie Aluebho 
•	Nsisong Akpakpan - Nelly Munene 
•	Mutairu Onaido - Peter Onwuzuruigbo 
•	Yoftahe Seid - Haruna Kwairanga 
•	Ekhator Marvellous - Duke Okojie 
•	Stellah Mbao - Gloria Oyoo 
•	Emmanuel Monday - Mustapha Tunau 
•	Luts Enoch - Aishat Bello 
•	Success Nnadozie - Susan Ndambuki 
•	Olumide Ogunrinde - Joseph Aiyegbusi 
•	CHIBUIKE Anene - Goodness Ada-okungbowa 
•	Olayemi Olakanmi - SAMUEL Alaba 
•	Emmanuel Botchway - Manuel Boampong 
•	Solomon Terngu - Ermiyas Amete 
•	Akoy Jacob - Abdullah Qaasim 
•	Joshua Mekuriaw - Timo Kamau 
•	Brian Njuguna - Onesmas Kariuki 
•	CONFIDENCE Ahuekwe - Edoga Chimdi Alfred Alfred 
•	Imani Nderitu - Vaud Kagong 
•	Emmanuel Osifo - Edwin Onyegbuna 
•	Shah Tanya Daniel - Greenbel Eleghasim 
•	Muthomi Wanjohi - Twine Brightson 
•	Valentine Kiguli - John Opiyo 
•	Jude Ehimigbai - Yonas getaneh 
•	David KAHARI 
•	Beth Njoroge - Derrill Kennoly 
•	Samuel Odiase-Omoighe - Nigel Marungu 
•	Daniel Eze - Emmanuella Ogbodu 
•	Michael Alabi - Precious Onovayen 
•	Ikechukwu Nwafor - Abigail Adeboga 
•	Godsgift Sombinyerechukwu - Sanna Bah 
•	Johnathan Holder - Enoch Madehin 
•	Juwon Iroayo - Ruth Ogadina 
•	Mephic Wambui - Monisola Keshiro 
•	Christelle Arielle Mbouteu Megaptche - Robert Peter Mrema Mrema 
•	Peter Nyongesa - Jerry Fidel 
•	Moses Ojo - Oluwabunmi David-Orugun 
•	Samuel Tadele - Wendo Githaka Wanjiru 
•	Martins Ugwu - Mariam Abdulrazaq 
•	Nosakhare Jesuorobo - Freedom Dike 
•	Yohannes Jo - Ivor Hammond 
•	Tade Akingbade - Yinka Ogungbe 
•	Somto Onu - Legendary.god aka 
•	Nokuphiwa Ngema - Michelle Piper 
•	Daniel Anyetewen - Derrick Azameti 
•	Ibrahim Sserunkuuma - King Ayinde 
•	Emmanuel Emmanuel - Victor Akor 
•	Adrian Mwangi - Tegegn Yadate 
•	Bereket Tezera - Edugie Odigie 
•	DENIS Mwangi - IRENE Mwangi 
•	Rehema Mwandembo - Nelson Otieno 
•	Yassine Boujarfaoui - Jared KIPLAGAT 
•	Daniel Mutua - Jefferson Georgewill 
•	Ibrahim Kaweti - ISAAC YEGON Yegon 
•	kaycee kelechi - Wandile Mlambo 
•	clement Mlozi - Nitsuhwork Wube 
•	Makai mark - Lourdel Kigudde 
•	Samuel Akwensivie - Bright Oghor 
•	ABDEL FADIL AFO - SODJI Kokou Seth 
•	Timothy Adekunle - LUCKY Ezealor 
•	Happiness kemuel - Sunday Gad 
•	Chiderah Okonkwo - Abdulwahab Sakariya 
•	Michael Kiplangat - Kisali Kisali 
•	Girmachew Redie - Shegaw Nigusie 
•	Shirley Akeso - Kipkemei Emmanuel 
•	Therry Adjei - Patricia Teye 
•	Ridwan Agunbiade - hamza Saili 
•	Biruk argaw - Abdurehman Abdela 
•	Brian Mudanya - Amarachi Okei 
•	Samuel Gekonge - Philip Toluwani 
•	Mihiret Birhie - Tsegaw1 Degefa 
•	Agara Dunbo Agara - Fikayo Soetan 
•	Akubo Akubo - Timothy Ekawu 
•	Godsfavour Omozusi - Abdoulaye Diop 
•	OLATUNDE Abodunrin - Favour Okorie 
•	Philip Ansah - Omilelewe Omotoyosi 
•	Teresiah Muhoi - Alice Awominure 
•	Dotun Balogun - EGBOCHE Udenyi 
•	Robert Loterh - Dannon Boluwatife Rebecca Dannon 
•	Anwar Mamudu - Amaka Ohakanu 
•	Emmanuel Ayaazok - IBUKUNOLUWA Aina 
•	Hope Makanga - reny kipkoech 
•	Kaleab Fkadie - Kidist Shiferaw Meshesha Meshesha 
•	Nigatu Shonore - Temitope Akinmegha 
•	Hlavutelo Ngobeni - Simanga Mchunu 
•	Chukwuebuka Agu - Usman Busari 
•	Winner Efeoghene - Precious Amaechi 
•	ayoni02 sakibu - Bill Konchellah 
•	Deborah Aruwajoye - Felix Anyanwu 
•	Grace Njoroge - Douglas Ndicho 
•	Niwamanya BRUNO - Sixtus Ikeme 
•	anania Tadesse - Amanuel Fenta Dejen 
•	Abdalla Ali - Raji Oluwatosin 
•	David Mandizera Mandizera - Enoch Aikpokpodion 
•	Edumaba Graham - Godspower Eneh 
•	Opee Odugbesan - gaston mendy 
•	Henok Tamirat - Siyamthanda Majali 
•	Davidson Ogaraku - Akeem Adedayo 
•	Mwaura Kariuki - Peter Ogutu 
•	Ermiyas Abera - Yusuf Yusuf 
•	faysel lalemda - irine chepngetich 
•	ELISHA KUJE - Ogechi Faustina 
•	Abdullateef Olawumi - Tife Olatunji 
•	Salome Wambere - kebron Abiy 
•	Jamal Guyo - Chris Gitonga 
•	Daniel Oyeniyi - Assefa Mekonen 
•	Abdul Gafar Akinsemoyin - abiola Oladunjoye 
•	Gerald Wafula - Daniel Asres 
•	Ngoni Towindo - Mashyrano Mutimbwa 
•	Josephat Onyekwelu - Andrews Nartey 
•	Christian Ojiezele Ojiezele - Zino Odah 
•	Ayinde Daniel Olumide - Idayat Adeyemo 
•	Beatrice Zana - Christopher Christopher 
•	Sana Omar - Abdou Aziz Ndiaye 
•	John Iweh - Mubaraq Babatunde 
•	Amakalu Vitalis - Chiemezie Agbo 
•	James Mwangi - Motselisi Leketa 
•	Isaac Irabor - Ekikere-abasi Ekere 
•	Leila Natasha - Omega Mudzviti 
•	Aghogho Ken-Erhimu - Orevaoghene Ekwa 
•	Joseph Macharia - Phylis Kiruri 
•	Silwane Mdluli - Katlego Pule 
•	A'ishah Abdulganiyu - Sofienne Boukhris Boukhris 
•	Williams agada - Victory Eki 
•	Rosemary Emmanuel - Sheggs Abiodun 
•	netshedz Dzhivhuho - Kayode OYINLOYE 
•	Cynthia Mugo - Elias Macharia 
•	Emmanuel Chukwuemeka - Lena Chiamaka 
•	Lucky Daniels - PraiseL Ozoko-Emmanuel 
•	Adeiye AKANDE - Adefiola KOLAJO 
•	Victor Ogunshola - Chuma Chibueze 
•	Charles Okoro - Kwesi Otoo 
•	Meekness Ekeze - Boluwatiwi Onakomaiya 
•	Katuramu Edgar - Richard Muthoni 
•	Ednah Osoro - Francis Kakooza 
•	Hanna Ashenafi Alemu Alemu - Mohammed Kedir 
•	Immaculate Baraza - Abigael Amuruon 
•	Stephen Chinyere - Victor Udeh 
•	Sheriffdeen Yusuf - Alexander Igho 
•	Chinwendu Eke - Ebube Favour 
•	Baiyewu Babawande - Nwokoye Onyinyechi Maryjane Nwokoye 
•	Romha Keneni - Amaled Shumeta 
•	Ayomide Solarin - Josiah Omoba 
•	Saheed Omotola - Hudhayfah Ismail 
•	Ganiyu Ganiyu - Catherine Otieno 
•	Onanefe Gilead Okotie Okotie - ALLAN Ayikanying 
•	Elizabeth Lukas - Mwangi Enoch 
•	Mohammed teha - Asma Baye 
•	Jay Allotei-Noah - Derrick Delali Azamalah 
•	QUADRI Akanbi - Abdulrashid Abdulrazaq 
•	Ropafadzo Munetsi - Victor Agese 
•	Queen Onuoha - HAKEEM GBAJABIAMILA 
•	Vincent Akachukwu - Mahamadou ADAMOU DJIBO 
•	Faith Adeoti - Jerry Chijioke 
•	Micheal Emeka - Elvis Onuoha 
•	Florence SYLVANUS - Abraham Oluremi 
•	Donna Govender - Japheth Namukuru 
•	Felix Arogo - Evans Njeru 
•	Samuel Adeoye - TIMOTHY Adeoye 
•	Trust Makhubele - Ronewa Mabila 
•	Ejaromedoghene Ogheneruona - Nwamaka Ugonma 
•	MICKY Migwi - daniel Leul 
•	Kingsley Tetteh - Daniel Nwakacha 
•	Abel Shitarek - DANIEL MWAI TSUMA Mwai 
•	IAN Mwenesi - Bill otieno 
•	Kris Ugwu Ugwu - Ratsoane Ratsoane 
•	Cymon Dunamis Boahen - Adedapo Taiwo Adeyemi Adeyemi 
•	Udeh Obeya - Christian Nwabiukwu 
•	Kenneth Onwuachu - Prosperity Egharevba 
•	Abdi Bekele Balcha - Raphael Okai 
•	Chiedozie Ikechukwu - Tionge Mughogho 
•	Felix Antwi-Asiedu Junior - Natnael asfaw atnafu Gebreselassie 
•	Veronica Emiola - Felix Savali 
•	Basim Yasin - Natnael Atnafu 
•	Simon Ngugi - Dawit Aseged 
•	Angel Onuoha - Bennet Ukoh 
•	Edwin Moses - Beamlak Shiferraw 
•	Ogochukwu Joboson - Emmanuel Amadi 
•	Divine AGAFIE - Trevour Jonnes 
•	Kalkidan Diro - Dejen Hailu 
•	Fidel Odey - Gabriel Ejeruke 
•	Josphat KITUKU - Adedotun Aderibigbe 
•	Wilfred Mbatia - Michael Mengesha 
•	CHRISTOPHER NGUNJIRI Ngunjiri - Nickson Mwaniki 
•	Abodunde Oluwatimileyin - Olawale Okegbile 
•	Samuel Osondu - Ncha-mwasu Elisha 
•	Mutai ELKANAH - Abimbola Olaide 
•	Olumide Joseph Agbomabiwon - Oluwatobi Oluwatobi 
•	Brenda Nyakio - Phoebe Muthoni 
•	Stanley Evuru - Fraser Nyale 
•	Theo Madikgetla - David Ejiobih 
•	Abu Bakarr Turay - Ibrahim Bakarr 
•	Iyanda Iyanda - Ayanri Ishiekwene 
•	Lanre Daramola - Eagles Okponobi 
•	Abrham Endale - Abrham Mengistu 
•	Ayobami isaac Ayobami - Ufonobong Essien 
•	Bayo Bayo - Bismark Bismark 
•	zeddy cherotich - M Kiige 
•	Sanctus Ejiofor - Mahadi Abuhuraira 
•	EMENIKE Nyema-Amadi - Cass Orji 
•	Kevin Kwanusu KWANUSU - Femi Sokoya 
•	Ahmad Youssef - Ogbule Nkiruka 
•	Robiu Olayinka Aliu Aliu - emajay Ogbonnaya 
•	Art Ndiema Ngotho - BRIAN Maina 
•	Ifeoluwa Alao - Nahom Teklewold 
•	Zewdie Habtie - yirga Molla 
•	Lyndah Katusiime - Andrew Andrew 
•	Oluwatoye Agbonjinmi - Sesay Sesay 
•	JACOB AIDOO - Yohanes Amare 
•	Kevin Gatimu - Chidinma Iheaturu 
•	CHRISTOPHER Jones - Mark Odah 
•	DJILO DJILO - Onyekachukwu Paschal Nwankwo 
•	Alinafe Isabelle Mpofu - King Joe Kima 
•	DANIEL OJIEZELE - Osamudiamen Benedict 
•	Ronald Mutegeki - Lukwago Lukwago 
•	Samuel Samuel - Ernest Philips 
•	Hamza Saidu Saidu - Abdulbarr SHONIBARE 
•	Abenezer Hailu - Seronu Pkiyach Denis 
•	Heaman Dejene - Praiselord Mensah-Anum 
•	Hailemichael Brhane - Justin Oseghale 
•	Samson Otori - Debbie Nyasetia 
•	Iseoluwadoyin Emmanuel - Eworitse Williams 
•	Tiisetso Sebata - Mary Fakunmoju 
•	Divinefavour David - Adedoyin Victoria Victoria 
•	Michael Okiri - Okenwa ukelonu 
•	Nihi Olusola Gabriel Gabriel - Uriel Awe-Obe 
•	NDICHU NDICHU - John James 
•	Patrick Boateng - Godfred Ababio 
•	Ndukwe Juliet - Ebede Victor 
•	Peace Igwudu - Shao Mashao 
•	Alex Gebremichael - Yoseph Tefera 
•	Joel David - Arnold Okey-Ehieze 
•	Edgar Godwin - DENIS Bollo 
•	Melekte Tamiru - Oluwatomi Epetimehin 
•	Peter Afolami - Favour Oluwatosin 
•	Emmanuel AZIAWOR - Senaga Osasenaga 
•	Blessing Manjozi - Takudzwa Michael Tsuro Tsuro 
•	Fana Alemayehu - YONATAN Addis 
•	Oyemike Chukuneku - Yusuf Isiaka 
•	Suleyman Fantahun - Naomi assefa 
•	Patrick Christopher - Barnabas Chukuka 
•	Clara Nkomo - PRISCILLAH Nyamhinda 
•	Chiamaka Anowai - Dechasa Gemeda 
•	keside ezeala - Adeniyi Obanla 
•	Onyinyechi Onwuakpa - Tamunomiebaka IBIYEDAWO 
•	Byron Odhiambo - Joseph Lweya Samwa 
•	Kazeem Ademola - Bug_101 Kipkemoi 
•	Hassan Ait oundjar - hamzaelfhil Elfhil 
•	Ahmed Swaleh - Sheila Ajock 
•	Ukeme Gabriel - Peter Keroti 
•	Mikal Mikal - Harriet Agwata 
•	Eleni Bekele - Olayode Yusuf 
•	Emmanuel Oppong - Oluwarotimi Alaka 
•	Moses Osoro - Samuel Dike 
•	george Weru - Abdul Aziz Osumanu 
•	Chioma Izuokwu - Empress Moses 
•	natan belachew - Cesar Mémoli Nomo 
•	Chidera Akubude - yonas Ferew 
•	Franklin Duru - Emmanuel Emmanuel 
•	Zachary Ochwangi - Wesley Kirui 
•	Modibbo Modibbo - Habtom Ekubay 
•	GiGi Tena - Eric Eric 
•	Timilehin Abidoye - Victoria Ituma 
•	Opeyemi Olasubomi - Jon Fekadu 
•	Lungelo August - Waringa Waringa 
•	Queenieabosede BOSE - Anthony Idyu 
•	Smart Smart - Abdulsalam Abdulsalam 
•	Meresia Opiyo - GEORGE Osodo 
•	Marc Hilarion AFFECHI - Fregis Koffi 
•	Obianuju okocha - Justice Anthony 
•	Beaty Kimeu - LOÏC MAURIAT DODJI Denon 
•	Cyrus KAMUNYA - AgaiMorara Morara 
•	Mr Shozi Shozi - ahmed Najash 
•	Goodness Fasan - Peter Abolude 
•	Benson Njuguna - Kinya Bundi 
•	Victor Emmanuel - Emmanuel Otitolaye 
•	Womi Otu - Chukwuemeka Orji 
•	victor koech - Brian Kimathi 
•	Hermon Haile - Mohammed Badr 
•	David Iyodo - Iyodo Michael Iyodo 
•	Chi Mofor - Kingsley Ndubuisi 
•	monday chukwumezirim Monday - Elijah Ayuba 
•	Emmanuel Sam - Abasi-Ikpuho Peter 
•	Ayilara Ayilara - Nsidibe Essang 
•	Debs Dada - Adetomiwa Adejumo 
•	Dora Rotich - Palvin Waithira 
•	Babatunde Fabode - Kolade Ogunlade 
•	Karen Chepngeno - Jonathan Uma 
•	Dereje Girma - Abenezer Tadesse Tadesse 
•	Nebiyou Yemam Ebrahim - Darik Demeke 
•	Awomolo Idowu - Omondi Alex Omieno Omondi 
•	Jonathan Kilonzo - Prince Kyeremeh 
•	Dennice Ndede - Rose Matu 
•	Idahosa Iyamu - Ephraim Igbinosa 
•	Joseph Odey - Yonas Aknaw 
•	Odun Adetunji - Juliet Chinwendu 
•	Mubaraq Uthman - Emmanuel Adim 
•	Wamaitha Karigi - Edwin Ndiritu 
•	Aminu Rabah Rabah - Felix Segun 
•	Emmanuel Maunga - Tabitha Moige Matara Matara 
•	Ibrahim Habideen - Kareem Raheem 
•	Becky Zenebe - Evans Kioko 
•	Kerry Chukwuma - Samuel Onoja 
•	Richard Otieno - Propser Collins 
•	Duke Nurrein - Abdulsalam Abdulsalam 
•	Nalon Grace Yaa - Mulualem Zewude 
•	Uche Esere - Victor Osedahunsi 
•	Ekuta Ekuta - Dabila Ouattara 
•	Daniel Egwaoje - Ayodele Oluwagbotemi 
•	Biche Chi - Omar Zairh 
•	WAKILI Kiruku - Joseph Juma 
•	Toheeb Abdullahi ABDULLAHI - Andrew Emaye 
•	Adeolu Adeeyo - Sedoo Bitto 
•	Chioma Jane - Eugene Kankam 
•	Sarah Yusuf - SOLOMON Niyi 
•	Faith Josephs - Ezechiel Ezechiel 
•	Tesla Oppong - Ebuka Simon 
•	Lizzie Pappoe - Deborah David 
•	Temitope Awe - Adel Mikhael 
•	Andrew Kakinda - BEZAWIT Edea 
"""
#clean the list by removing unwanted characters
student_list = re.split(r'•|-|\n|\t', students)
#itaret through the list 
while '' in student_list:
    student_list.remove('')
print(student_list)# pring the clean list
print(len(student_list))
matches = [match for match in student_list if "Queens Kisivuli" in match]
print(matches)