biolabQuestsExternal = ['Friendship Quest', 'Bio Lab Entrance Quest']
namelessIslandQuestsExternal = ['Lost Child Quest', 'Rachel Sanctuary Entrance Quest', 'Veins Siblings Quest', 'Curse of Gaebolg Quest', 'Nameless Island Entrance Quest']
ktullanaxQuestExternal = ['Ice Necklace Quest']
thanatosQuestExternal = ['Thanatos Tower Quest']
sealedShrineQuestExternal = ['Sealed Shrine Quest']
morrocQuestExternal = ['Continental Guard Quest']
gloomQuestExternal = ['Rachel Sanctuary Entrance Quest', 'Lost Child Quest']
niddhoggQuestsExternal = ['Tripatriate Unions Feud', 'Attitude To The New World', 'Ring Of The Wise King', 'New Surroundings', 'Two Tribes', 'Pursuing Rayan Moore', 'Report From The New World', 'Guardian Of Yggsdrasil Step 9', 'Onward To The New World']
EndlessTowerExternal = ['None']

cards_to_coins = { 
  4407 : 20.0, 
  4145 : 20.0,
  4430 : 20.0,
  4367 : 20.0,
  4363 : 12.0,
  4361 : 20.0,
  4357 : 12.0,
  4365 : 20.0,
  4359 : 12.0,
  4419 : 20.0,
  4145 : 20.0,
  4441 : 20.0, 
  4147 : 12.0,
  4408 : 20.0, 
  4407 : 20.0
}

#instance name, median_number, mob_id, mob_name, mob_drop_rate, quests
#added placeholder for ET mvps
instance_mob_item_mapping = [
  ('Sealed Shrine', 5, 1929, 'Greater Demon Baphomet', [(6004, .15), (2514, .7), (1181, .5), (1181, .01), (2513, .7), (2327, .7), (1466, .9), (4147, .0003)], sealedShrineQuestExternal),
  ('Niddhoggs Nest', 4, 2022, 'Nidhoggrs Shadow', [(6091, 1.0), (7444, 1.0), (2610, .5), (1484, .05), (1170, .05), (1417, .05), (2554, .1), (5467, .15)], niddhoggQuestsExternal)
  ('Ktullanax', 4, 1779, 'Ktullanux', [(7562, 1.0), (616, .9), (2509, .2), (2111, .2), (617, 1.0), (607, 1.0), (4419, .0003)], ktullanaxQuestExternal)
  ('Nameless - Beelzebub', 5, 1874, 'Beelzebub', [(7562, 1.0), (616, .9), (2509, .2), (2111, .2), (617, 1.0), (607, 1.0), (4419, .0003)], namelessIslandQuestsExternal)
  ('Nameless - Fallen Bishop', 3, 1871, 'Fallen Bishop Hibram', [(523, 1.0), (1420, .05), (2677, .05), (1422, .05), (985, 1.0), (1614, .2), (18538, .04), (4441, .0003)], namelessIslandQuestsExternal)
  ('Thanatos', 4, 1708, 'Memory of Thanatos', [(7444, .3), (2519, .1), (7450, 1.0), (2342, .5), (2412, .5), (2515, .1), (2655, .05), (5377, .1), (5462, .1), (4399, .0003)], thanatosQuestExternal)
  ('Gloom', 3, 1768, 'Gloom Under Night', [(7566, 1.0), (7023, 1.0), (7022, .6), (616, 1.0), (2513, .1), (1377, .01), (5306, .027), (4408, .0003)], gloomQuestExternal)
  ('Morroc', 6, 1917, 'Wounded Morroc', [(5808, .075), (2374, .1), (2375, .12), (2433, .25), (7799, 1.0), (7798, 1.0)], morrocQuestExternal)
  ('Valkyrie Randgris', 6, 1751, 'Valkyrie Randgris', [(7510, 1.0), (2357, .12), (2524, .15), (2421, .3), (2229, .5), (7024, .75), (2115, .16), (4407, .0003)], [])
  ('Bio - Sniper', 5, 1650, 'Sniper Cecil', [(1228, .35), (1236, .35), (617, 1.0), (1234, .15), (1237, .35), (1720, .15), (1724, .25), (4367, .0003)], biolabQuestsExternal),
  ('Bio - High Priest', 5, 1649, 'High Priest Margaretha', [(1814, .35), (2615, .25), (2513, .9), (1557, .35), (1527, .35), (1528, .25), (1560, .35), (4363, .0003)], biolabQuestsExternal),
  ('Bio - High Wizard', 5, 1651, 'High Wizard Kathryne', [(1241, .35), (1242, .35), (2616, .9), (2343, .25), (2513, .25), (1618, .3), (2319, .35), (4365, .0003)], biolabQuestsExternal),
  ('Bio - Whitesmith', 5, 1648, '1648', [(1138, .35), (1140, .25), (2318, .9), (1365, .35), (1364, .35), (1369, .25), (1368, .35), (4361, .0003)], biolabQuestsExternal),
  ('Bio - Assassin Cross', 5, 1647, 'Assassin Cross Eremes', [(1234, .15), (1230, .15), (2319, .9), (1233, .35), (1232, .35), (1265, .35), (13002, .35), (4359, .0003)], biolabQuestsExternal),
  ('Bio - Lord Knight', 10, 1646, 'Lord Knight Seyren', [(1132, .25), (2342, .35), (2412, .9), (1470, .35), (1469, .3), (1166, .25), (1415, .15), (4357, .0003)], biolabQuestsExternal),
  ('Endless Tower - Mistress', 10, 1059, 'Mistress', [(1413, .015), (518, 1.0), (2249, .025), (616, .30), (7018, .03), (985, 1), (16001, .01), (4132, .0003), (996, .15), (526, .40), (722, .30)], EndlessTowerExternal),
  ('Endless Tower - Golden Thief Bug', 10, 1086, 'Golden Thief Bug' [(969, .30), (1524, .015), (2246, .025), (10016, .15), (714, .09), (985, .60), (984, .45), (4128, .0003), (2160, .20), (701, .10)], EndlessTowerExternal),
  ('Endless Tower - Maya', 10, 1147, 'Maya' [(10006, .15), (2615, .02), (2234, .02), (639, .15), (7020, .03), (985, 1.0), (2005, .01), (8518, .027), (4146, .0003), (730, .20), (603, .30), (617, .20)], EndlessTowerExternal),
  ('Endless Tower - Moonlight Flower', 10, 1150 'Moonlight Flower' [(1477. .05), (1234, .01), (1525, .015), (10008, .15), (638, .195), (985, .78), (1648, .01), (5360, .027), (4131, .0003)], EndlessTowerExternal),
  ('Endless Tower - Phreeoni' , 10, 1159 'Phreeoni' [(1223, .05), (1236, .015), (1014, 1.0), (2288, .03), (985, .87), (13047, .01), (8522, .027), (4121, .0003), (1008, .05), (730, .10), (1000, .40)], EndlessTowerExternal),
  ('Endless Tower - Osiris ', 10, 1038 'Osiris' [(617, .60 ), (1232, .015), (2235, .02), (1255, .06), (1009, .30), (5053, .015), (1285, .01), (4144, .0003), (603, .40) (608, .30), (751, .05)], EndlessTowerExternal),
  ('Endless Tower - Turtle General', 10, 1312 'Turtle General' [(1306, .0005), (7480, .006), (1417, .0009), (7070, 1.0), (1141, .008), (658, .0003), (5611, .001), (4305, .0003), (967, .55), (607, .15), (617, .20)], EndlessTowerExternal), 
  ('Endless Tower - Naght Sieger', 10, 1956, 'Naght Sieger', [(13412, .5), (13413, .5), (2542, .5), (5017, .90), (616, 1.0), (2514, .9), (7294, 1.0)], EndlessTowerExternal),
  ('Endless Tower - Drake', 10, 1112, 'Drake', [{1127, .06), (1135, .015), (1128, .04), (5019, .035), (985, .096), (1189, .01), (5417, .024), (1127, .06)], EndlessTowerExternal),
  ('Endless Tower - Valkyrie Randgris' , 10, 1751, 'Valkyrie Randgris', [(7510, 1.0), (2357, .12), (2524, .15), (2421, .3), (2229, .5), (7024, .75), (2115, .16), (4407, .0003)], EndlessTowerExternal),
  ('Endless Tower - Beelzebub' , 10, 1874, 'Beelzebub', [(7756, 1.0), (2423, .2), (1565, .2), (2000, .2), (2702, .2), (985, 1.0), (742, 1.0), (4145, .0003) (607, .55), (617, .50), (617, .50)], EndlessTowerExternal),   

#mobs
#2022 - nidd
#1751 - valk
#1832 - ifrit
#1874 - beelzebub
#1956 - naght sieger
#1957 - Entweihen Crothen
#1650 - Sniper Cecil
#1649 - High Priest Margaretha,
#1651 - High Wizard Kathryne
#1648 - Whitesmith Howard
#1647 - Assassin Cross Eremes
#1646 - Lord Knight Seyren
#1956 - Naght Sieger

mobs_in_run = {
  'Niddhogg' : [2022],
  'ET' : [1059, 1086, 1751, 1112, 1874, 1832, 1874, 1956, 1957],
  'Bio' : [1650, 1649, 1651, 1648, 1647, 1646]
}

median_party_size = {
  'Niddhogg' : 4.0,
  'ET' : 10.0,
  'Bio' : 7.0  
}

mob_drop_rate = {
  2022 : [(6091, 1.0), (7444, 1.0), (2610, .5), (1484, .05), (1170, .05), (1417, .05), (2554, .1), (5467, .15)],
  1751 : [(7510, 1.0), (2357, .12), (2524, .15), (2421, .3), (2229, .5), (7024, .75), (2115, .16), (4407, .0003)],
  1832 : [(994, 1.0), (2677, .3), (12103, .0999), (13017, .005), (1471, .2), (1133, .2), (2345, .01), (5420, .1), (4430, .0003)],
  1874 : [(7754, 1.0), (2423, .2), (1565, .2), (2000, .2), (2702, .2), (985, 1.0), (742, 1.0), (4145, .0003)],
  1956 : [(13412, .5), (13413, .5), (2542, .5), (5017, .9), (616, 1.0), (2514, .9), (7294, 1.0)],
  1957 : [(1636, 1.0), (1631, 1.0), (2513, 1.0), (1624, 1.0), (616, 1.0), (1618, 1.0), (7291, 1.0)],
  1650 : [(1228, .35), (1236, .35), (617, 1.0), (1234, .15), (1237, .35), (1720, .15), (1724, .25), (4367, .0003)],
  1649 : [(1814, .35), (2615, .25), (2513, .9), (1557, .35), (1527, .35), (1528, .25), (1560, .35), (4363, .0003)],
  1651 : [(1241, .35), (1242, .35), (2616, .9), (2343, .25), (2513, .25), (1618, .3), (2319, .35), (4365, .0003)],
  1648 : [(1138, .35), (1140, .25), (2318, .9), (1365, .35), (1364, .35), (1369, .25), (1368, .35), (4361, .0003)],
  1647 : [(1234, .15), (1230, .15), (2319, .9), (1233, .35), (1232, .35), (1265, .35), (13002, .35), (4359, .0003)],
  1646 : [(1132, .25), (2342, .35), (2412, .9), (1470, .35), (1469, .3), (1166, .25), (1415, .15), (4357, .0003)]
}

search_items = { 
  607  : "Yggdrasil Berry",
  7321 : "Crystal Fragment",
  604  : "Dead Branch",
  578  : "Strawberry",
  582  : "Orange",
  12010 : "Wind Arrow Quiver",
  12012 : "Crystal Arrow Quiver",
  12013 : "Shadow Arrow Quiver",
  12014 : "Immaterial Arrow Quiver",
  2537 : "Diablos Manteau [1]",
  8900 : "Talon Coin", 
  6091 : "Red Scale", 
  7444 : "Treasure Box", 
  2610 : "Gold Ring", 
  1484 : "Carled", 
  1170 : "Katzbalger", 
  2554 : "Nydhorgg's Shadow Garb", 
  1417 : "Pole Axe", 
  5467 : "Helm of Dragon", 
  4407 : "Valkyrie Randgris Card", 
  2357 : "Valkyrja's Armor", 
  2524 : "Valkyrja's Manteau", 
  2421 : "Valkyrja's Shoes", 
  2229 : "Helm", 
  7024 : "Bloody Edge", 
  2115 : "Valkyrja's Shield", 
  7510 : "Valhalla's Flower",
  7754 : "Broken Crown",
  2423 : "Variant Shoes", 
  1565 : "Book of the Dead",
  2000 : "Staff of D
